<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="LogIn" @keyup.enter="logIn">
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
      email: null,
      password: null,
    }
  },
  methods: {
    LogIn() {
      const email = this.email
      const password = this.password

      const payload = {
        email, password
      }
      this.$store.dispatch('LogIn', payload)
      this.$router.push({ name: 'HomeView' })
    }
  }
  
}
</script>

<style>

</style>