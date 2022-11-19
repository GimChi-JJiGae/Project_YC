<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <label for="username">ID </label>
      <input v-model.trim="credential.username" id="id" type="text" placeholder="ID" required="required" data-validation-required-message="Please enter your username." /><br>

      <label style="margin-right: 15px" class="st-font" for="sex">나이 </label>
      <span class="select-wrapper" style="margin-right: 15px">            
        <select style="font-size: 20px" name="age" id="age" v-model="credential.age" class="st-font">
          <option :value="age" v-for="(age, idx) in this.$store.state.ages" :key="idx">{{ age }}</option>
        </select>
      </span><br>

      <label style="margin-right: 15px" class="st-font" for="sex">성별 </label>
      <span class="select-wrapper" style="margin-right: 15px">            
        <select style="font-size: 20px" name="sex" id="sex" v-model="credential.sex" class="st-font">
          <option :value="sex" v-for="(sex, idx) in this.$store.state.sex" :key="idx">{{ sex }}</option>
        </select>
      </span><br>

      <label for="email">Email </label>
      <input v-model.trim="credential.email" id="email" type="text" placeholder="email" required="required" data-validation-required-message="Please enter your email address." /><br>

      <label for="password1" >비밀번호 </label>
      <input v-model.trim="credential.password" @input="passwordValidation" id="password" type="password" placeholder="Password" required="required" data-validation-required-message="Please enter your password." /><br>
      <div v-if="caution1">{{ caution1 }}</div>

      <label for="password2">비밀번호 확인 </label>
      <input v-model.trim="credential.passwordConfirmation" @input="checkPW" @keypress.enter="signUp" id="passwordConfirmation" type="password" placeholder="passwordConfirmation" required="required" data-validation-required-message="Please confirm your password" />
      <div v-if="caution2">{{ caution2 }}</div>
      <br>
      <button id="Signup" type="submit">Signup</button>
    </form>
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