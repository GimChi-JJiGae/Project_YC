<template>
  <div class='row justify-content-center'>
    <div class="border p-3 rounded-3 row justify-content-center" style="width:500px; height:400px">
      <div class='row' style="height: 50px; width: 100%;">
        <h2>비밀번호변경</h2>
      </div>
      <form @submit.prevent="changePassword">
        <div class="text-start mb-3" style="height: 70px;">
          <label for="currentPW" class="st-font form-label"><strong>현재 비밀번호</strong></label>
          <input v-model.trim="currentPassword" id="password" type="password" placeholder="Password" required="required" data-validation-required-message="Please enter your password." class="form-control"/>
        </div>

        <div class="text-start mb-3">
            <label for="password1" class="st-font form-label"><strong>새 비밀번호</strong></label>
            <input v-model.trim="newPassword" @input="passwordValidation" id="newpassword" type="password" placeholder="Password" required="required" data-validation-required-message="Please enter your password." class="form-control"/>
            <div v-if="caution1" id="emailHelp" class="form-text">{{ caution1 }}</div>
          </div>

        <div class="text-start mb-4">
          <label for="password2" class="st-font form-label"><strong>새 비밀번호 확인</strong></label>
          <input v-model.trim="newPasswordConfirmation" @input="checkPW" @keypress.enter="changePassword" id="passwordConfirmation" type="password" placeholder="passwordConfirmation" required="required" data-validation-required-message="Please confirm your password" class="form-control"/>
          <div v-if="caution2" id="emailHelp" class="form-text">{{ caution2 }}</div>
        </div>

        <div class="mt-3">
          <button class="btn content-font border" type="submit">비밀번호변경</button>
        </div>
      </form>
    </div>
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
      caution1: '',
      caution2: '',
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
      const token = this.getToken().headers.Authorization
      const formdata = new FormData()
      formdata.append('username', this.user.username)
      formdata.append('age', this.user.age)
      formdata.append('sex', this.user.sex)
      formdata.append('email', this.user.email)
      formdata.append('newPassword', this.newPassword)
      formdata.append('newPasswordConfirmation', this.newPasswordConfirmation)
      formdata.append('password', this.currentPassword)
      // axios.put(`${SERVER_URL}/accounts/${this.user.username}/change_password/`, data, config)
      axios({
        method: 'put',
        url: `${SERVER_URL}/accounts/${this.user.username}/change_password/`,
        headers: {
          'Content-Type':'multipart/form-data',
          'Authorization': `${token}`,
        },
        data: formdata
      })
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
    },
    passwordValidation() {
      const pw = this.newPassword
      let num = pw.search(/[0-9]/g)
      let eng = pw.search(/[a-z]/ig)
      let spe = pw.search(/[`~!@@#$%^&*|₩₩₩'₩";:₩/?]/gi)
      if (!pw.length) {
        this.caution1 = null
      } else if (pw.length < 8 || pw.length > 16){
        this.caution1 = "8자리 ~ 16자리 이내로 입력해주세요."
        return false
      } else if(pw.search(/\s/) != -1){
        this.caution1 = "비밀번호는 공백 없이 입력해주세요."
        return false
      } else if(num < 0 || eng < 0 || spe < 0 ){
        this.caution1 = "영문, 숫자, 특수문자를 혼합하여 입력해주세요."
        return false
      } else {
        this.caution1 = null
        return true
      }
    },
    checkPW() {
      const pw = this.newPasswordConfirmation
      if (pw === this.newPassword) {
        this.caution2 = null
      } else if (!pw) {
        this.caution2 = null
      } else {
        this.caution2 = '비밀번호가 일치하지 않습니다.'
      }
    },
  }
}
</script>

<style>

</style>