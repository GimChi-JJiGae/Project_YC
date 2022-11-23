<template>
  <div class="row justify-content-center">
    <div class="border p-3 rounded-3" style="width:500px; height:350px">
      <div>
        <router-link :to="{ name: 'HomeView' }"><img src="@/assets/logo5.png" alt="" style="width:150px;"></router-link>
      </div>
      <div class="mt-5">
        <form @submit.prevent="LogIn">
          <div class="mt-4">
            <input v-model.trim="credential.username" id="username" class="border-0 border-bottom" type="text" placeholder="아이디" required="required" data-validation-required-message="Please enter your username." style="width:300px;"/>
          </div>
          <div class="mt-4">
            <input v-model.trim="credential.password" id="password" class="border-0 border-bottom" type="password" placeholder="비밀번호" required="required" data-validation-required-message="Please enter your password." style="width:300px;"/>
          </div>
          <div class="mt-4">
            <button type="submit" style="width:300px; height:45px;" class="btn content-font border">로그인</button>
          </div>
        </form>
      </div>
    </div>
    <div class="row">
      <div>
        <button @click="moveToSignUp" class="m-1 btn content-font border btn-sm" type="submit">Signup</button>
      </div>
    </div>
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