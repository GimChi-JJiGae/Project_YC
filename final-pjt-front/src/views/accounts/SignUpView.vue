<template>
  <div class="container row justify-content-center">
    <div class="border p-3 rounded-3 row justify-content-center align-items-center" style="width:500px; height:600px">      
      <div style="width:300px;" class="my-3">
        <form @submit.prevent="signUp">
          <div class="text-start my-3 ">
            <label for="username" class="st-font form-label"><strong>아이디</strong></label>
            <input v-model.trim="credential.username" id="id" type="text" placeholder="아이디" required="required" data-validation-required-message="Please enter your username." class="form-control"/>
          </div>

          <div class="text-start">
            <label style="margin-right: 15px" class="st-font form-label" for="sex"><strong>나이</strong></label>
            <span class="select-wrapper" style="margin-right: 15px">            
              <select style="font-size: 20px" name="age" id="age" v-model="credential.age" class="st-font form-select">
                <option :value="age" v-for="(age, idx) in this.$store.state.ages" :key="idx">{{ age }}</option>
              </select>
            </span>
          </div>

          <div class="text-start">
            <label style="margin-right: 15px" class="st-font form-label" for="sex"><strong>성별</strong></label>
            <span class="select-wrapper" style="margin-right: 15px">            
              <select style="font-size: 20px" name="sex" id="sex" v-model="credential.sex" class="st-font form-select">
                <option :value="sex" v-for="(sex, idx) in this.$store.state.sex" :key="idx">{{ sex }}</option>
              </select>
            </span>
          </div>

          <div class="text-start mb-3">
            <label for="email" class="st-font form-label"><strong>Email</strong></label>
            <input v-model.trim="credential.email" id="email" type="text" placeholder="email" required="required" data-validation-required-message="Please enter your email address." class="form-control"/>
          </div>

          <div class="text-start mb-3">
            <label for="password1" class="st-font form-label"><strong>비밀번호</strong></label>
            <input v-model.trim="credential.password" @input="passwordValidation" id="password" type="password" placeholder="Password" required="required" data-validation-required-message="Please enter your password." class="form-control"/>
            <div v-if="caution1" id="emailHelp" class="form-text">{{ caution1 }}</div>
          </div>

          <div class="text-start mb-3">
            <label for="password2" class="st-font form-label"><strong>비밀번호 확인</strong></label>
            <input v-model.trim="credential.passwordConfirmation" @input="checkPW" @keypress.enter="signUp" id="passwordConfirmation" type="password" placeholder="passwordConfirmation" required="required" data-validation-required-message="Please confirm your password" class="form-control"/>
            <div v-if="caution2" id="emailHelp" class="form-text">{{ caution2 }}</div>
          </div>
          <div class="mt-3">
            <button class="btn content-font border" type="submit">Signup</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'
export default {
  name: 'SignUpView',
  data() {
    return {
      credential : {
        username: null,
        age: null,
        sex: null,
        email: null,
        password: null,
        passwordConfirmation: null,
      },
      caution1: '',
      caution2: '',
    }
  },
  computed: {
  },
  methods: {
    signUp() {
      axios.post(`${SERVER_URL}/accounts/signup/`, this.credential)
      .then( () => {
        const login_credential = {
          username: this.credential.username,
          password: this.credential.password,
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
    passwordValidation() {
      const pw = this.credential.password
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
      const pw = this.credential.passwordConfirmation
      if (pw === this.credential.password) {
        this.caution2 = null
      } else if (!pw) {
        this.caution2 = null
      } else {
        this.caution2 = '비밀번호가 일치하지 않습니다.'
      }
    }
  },
}
</script>

<style>

</style>