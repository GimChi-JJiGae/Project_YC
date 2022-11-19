<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="LogIn" >
      <label for="username">ID</label>
      <input v-model.trim="credential.username" id="username" type="text" placeholder="ID" required="required" data-validation-required-message="Please enter your username." />
      <br>
      <label for="password">password : </label>
      <input v-model.trim="credential.password" id="password" type="password" placeholder="Password" required="required" data-validation-required-message="Please enter your password." />

      <input type="submit" value="LogIn">
    </form>
    <h3>Sign up</h3>
    <button @click="moveToSignUp" id="Signup" type="submit">Signup</button>
  </div>
</template>

<script>
import axios from 'axios'
// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'LogInView',
  data() {
    return {
      credential: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    LogIn() {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credential)
        .then((res) => {
          // console.log(res)
          localStorage.setItem('access_token', res.data.token)
          this.$store.dispatch('LogIn', res.data.token)
          this.$router.push({ name: "HomeView" }).catch(()=>{})
          // location.reload()
        })
        .catch( (err) => {
          alert("올바른 아이디와 비밀번호를 입력해주세요.")
          console.log(err)
      })
    },
    moveToSignUp() {
      this.$router.push({ name: 'SignUpView' })
    }
  }
  
}
</script>

<style>

</style>