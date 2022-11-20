<template>
  <div class="d-flex flex-column align-items-center">
    <h2>전체 유저 목록</h2>
    <hr style="width: 400px">
    <div class="">
      <ul class="list-group list-group-flush" style="width:200px;" >
        <li
         v-for="(user, idx) in users"
        :key="idx"
        class="list-group-item"
        >
          <span @click="moveToProfile(user)" style="cursor:pointer;">{{ user.username }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UsersView',
  data() {
    return {
      users: [],
    }
  },
  methods: {
    getToken() {
      const token = localStorage.getItem('access_token')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    getUsers() {
      const config = this.getToken()
      axios.get(`${SERVER_URL}/accounts/users`, config)
        .then(res => {
          this.users = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    moveToProfile(user) {
      this.$router.push({ name: "ProfileView", params: { username: `${user.username}` }})
    }
  },
  created() {
    this.getUsers()
  }
}
</script>

<style>

</style>