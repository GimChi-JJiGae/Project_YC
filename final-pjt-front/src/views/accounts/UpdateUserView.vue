<template>
  <div>
    <h2>회원정보수정</h2>
    <form @submit.prevent="update">
      <label for="username">ID </label>
      <input v-model.trim="user.username" id="id" type="text" placeholder="ID" required="required" data-validation-required-message="Please enter your username." /><br>

      <label for="email">Email </label>
      <input v-model.trim="user.email" id="email" type="text" placeholder="email" required="required" data-validation-required-message="Please enter your email address." /><br>

      <label for="password">Password </label>
      <input v-model.trim="password" id="password" type="password" placeholder="password" required="required" data-validation-required-message="Please enter your email address." /><br>

      <br>
      <button id="Update" type="submit">수정</button><br>
      <button @click="moveToChangePassword">비밀번호 변경하기</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"
// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UpdateUserView',
  data() {
    return {
      user: [],
      original_username: null,
      password: null,
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
    getMyName: function () {
      const config = this.getToken()

      const hash = localStorage.getItem('access_token')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
      .then( (res) => {
        this.user = res.data
        this.original_username = res.data.username
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    update() {
      const config = this.getToken()
      const data = {
        user : this.user,
        password : this.password,
      }
      axios.put(`${SERVER_URL}/accounts/${this.original_username}/update/`, data, config)
      .then( () => {
        const login_credential = {
          username: this.user.username,
          password: this.password,
        }
        axios.post(`${SERVER_URL}/accounts/api-token-auth/`, login_credential)
          .then((res) => {
            localStorage.setItem('access_token', res.data.token)
            this.$store.dispatch('LogIn', res.data.token)
            this.$router.push({ name: "HomeView" }).catch(()=>{})
          })
          .catch( (err) => {
            console.log(err)
          })
        })
      .catch( (err) => {
        console.log(err)
      })
    },
    moveToChangePassword() {
      this.$router.push({ name: 'UpdatePassword', params: { username: `${this.original_username}`} })
    }
  },
  created() {
    this.getMyName()
  }
}
</script>

<style>

</style>