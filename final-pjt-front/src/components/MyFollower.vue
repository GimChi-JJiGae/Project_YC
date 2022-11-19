<template>
  <div>
    <h4 @click="moveToProfile(myFollower)">{{ myFollower.username }}</h4>
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