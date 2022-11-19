<template>
  <div>
    <h2>비밀번호변경</h2>
    <form @submit.prevent="changePassword">
      <label for="currentPW">현재 비밀번호</label>
      <input type="password" v-model="currentPassword"><br>

      <label for="newPW">새 비밀번호</label>
      <input type="password" v-model="newPassword"><br>

      <label for="newPW2">새 비밀번호 확인</label>
      <input type="password" v-model="newPasswordConfirmation"><br>

      <button type="submit">비밀번호변경</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"
// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UpdatePassword',
  data() {
    return {
      currentPassword: null,
      newPassword: null,
      newPasswordConfirmation: null,
      user: [],
    }
  },
  created() {
    this.getMyName()
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
    getMyName() {
      const config = this.getToken()

      const hash = localStorage.getItem('access_token')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
      .then( (res) => {
        this.user = res.data
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    changePassword() {
      const config = this.getToken()
      const data = {
        newPassword: this.newPassword,
        newPasswordConfirmation: this.newPasswordConfirmation,
        currentPassword: this.currentPassword,
        user: this.user,
      }
      // console.log(data.user)
      axios.put(`${SERVER_URL}/accounts/${this.user.username}/change_password/`, data, config)
        .then(() => {
          const login_credential = {
          username: this.user.username,
          password: this.newPassword,
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
    }
  }
}
</script>

<style>

</style>