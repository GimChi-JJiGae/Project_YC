<template>
  <div>
    <h1>Sign Up</h1>
    <form @submit.prevent="signUp">
      <label for="username">Username</label>
      <input v-model.trim="credential.username" id="username" type="text" placeholder="Username" required="required" data-validation-required-message="Please enter your username." /><br>

      <label style="margin-right: 15px" class="st-font" for="sex">Age </label>
      <div class="select-wrapper" style="margin-right: 15px">            
        <select style="font-size: 20px" name="age" id="age" v-model="credential.age" class="st-font">
          <option :value="age" v-for="(age, idx) in this.$store.state.ages" :key="idx">{{ age }}</option>
        </select>
      </div>

      <label style="margin-right: 15px" class="st-font" for="sex">Sex </label>
      <div class="select-wrapper" style="margin-right: 15px">            
        <select style="font-size: 20px" name="sex" id="sex" v-model="credential.sex" class="st-font">
          <option :value="sex" v-for="(sex, idx) in this.$store.state.sex" :key="idx">{{ sex }}</option>
        </select>
      </div>

      <label for="email">Email : </label>
      <input v-model.trim="credential.email" id="email" type="text" placeholder="email" required="required" data-validation-required-message="Please enter your email address." /><br>

      <label for="password1">password : </label>
      <input v-model.trim="credential.password" id="password" type="password" placeholder="Password" required="required" data-validation-required-message="Please enter your password." /><br>

      <label for="password2">password confirmation : </label>
      <input v-model.trim="credential.passwordConfirmation" @keypress.enter="signUp" id="passwordConfirmation" type="password" placeholder="passwordConfirmation" required="required" data-validation-required-message="Please confirm your password" />

      <button @click="signUp" id="Signup" type="submit">Signup</button>
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
    }
  },
  methods: {
    signUp() {
      axios.post(`${SERVER_URL}/accounts/signup/`, this.credential)
      .then( () => {
        // console.log(res)
        this.$router.push({ name: "LogInView" })
      })
      .catch( (err) => {
        console.log(err)
      })
    },
  }
}
</script>

<style>

</style>