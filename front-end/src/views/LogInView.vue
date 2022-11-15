<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="LogIn" @keyup.enter="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="email">email : </label>
      <input type="text" id="email" v-model="email"><br>

      <label for="password">password : </label>
      <input type="password" id="password" v-model="password">

      <input type="submit" value="LogIn">
    </form>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      email: null,
      password: null,
    }
  },
  methods: {
    LogIn() {
      const username = this.username
      const email = this.email
      const password = this.password

      const payload = {
        username, email, password
      }
      this.$store.dispatch('LogIn', payload)
      this.$router.push({ name: 'HomeView' })
    }
  }
  
}
</script>

<style>

</style>