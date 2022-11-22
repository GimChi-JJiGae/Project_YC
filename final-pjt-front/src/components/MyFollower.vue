<template>
  <div class="row align-content-center">
    <div class="col-3 p-0" style='height:100%; border-radius:50%; overflow:hidden; '>
      <img :src="myFollower.image" alt="" style="width: 100%; height:100%; object-fit: cover;">
    </div>
    <div class="col row align-content-center">
      <div class="row align-content-center">
        <span @click="moveToProfile(myFollower)" class="fs-5 fw-semibold">{{ myFollower.username }}</span>
      </div>
      <div class="row align-content-center">
        <span @click="moveToProfile(myFollower)" class="fs-6">{{ myFollower.email }}</span>
      </div>
    </div>
    <hr class="mt-2">
  </div>
</template>

<script>
import axios from "axios"
// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'
export default {
  name: "MyFollower",
  props: {
    follow: Number,
  },
  data: function () {
    return {
      users: [],
      myFollower: [],
    }
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('access_token')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    getUsers: function () {
      const config = this.getToken()
      axios.get(`${SERVER_URL}/accounts/users`, config)
      .then( (res) => {
        this.users = res.data
        const idx = this.users.findIndex((item) => {
          return item.id === this.follow
        })
        this.myFollower = this.users[idx]
        this.myFollower.image = SERVER_URL + this.myFollower.image
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    moveToProfile: function (user) {
      this.$router.push({ name: "ProfileView", params: { user_id: `${user.id}`, username: `${user.username}` }})
    },
  },
  created: function () {
    this.getUsers()
  },
}
</script>

<style>
</style>