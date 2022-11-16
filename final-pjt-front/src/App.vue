<template>
  <div id="app">
    <nav>
      <span v-if="access_token">
        <router-link :to="{ name: 'HomeView' }">Home</router-link> |
        <router-link to="javascript:void(0)" @click.native="LogOut">logout</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'HomeView' }">Home</router-link> |
        <router-link :to="{ name: 'LogInView' }">Login</router-link> | 
        <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> | 
      </span>
    </nav>
    <router-view/>
    <button v-on:click="getMovies">11111</button>
    <button v-on:click="getRelatedMovies">22222</button>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      isTrue: true,
    }
  },
  computed: {
    access_token() {
      return this.$store.state.access_token
    },
    // username() {
    //   return jwt_decode(this.token).username
    // }
  },
  methods: {
    LogOut() {
      this.$store.dispatch('LogOut')
      this.$router.push({ name: 'HomeView' })

    },
    getMovies: function () {
      axios.get(`http://127.0.0.1:8000/movies/`)
      .then( (res) => {
        if (this.$store.state.movies.length === 0) {
          this.$store.state.movies = res.data
          console.log(this.$store.state.movies)
          console.log("check")
        }
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    getRelatedMovies: function() {
      axios.get(`https://api.themoviedb.org/3/movie/${this.$store.state.movies[0].original_id}/recommendations?api_key=5d2592924ae354925561438e12ee8888&language=ko-KR&page=1`)
    .then( (res) => {
      console.log(res.data)
    })
    .catch( (err) => {
      console.log(err)
    })
    }

  },

 
}


</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
