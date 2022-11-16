<template>
  <div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  
  methods: {
    getMovies: function () {
      if (this.isLogin) {
        // this.$store.dispatch('getMovies')
      } else {
        // 로그인 안했을 때 페이지 보여주기
      }
      axios.get(`http://127.0.0.1:8000/movies/`)
      .then( (res) => {
        if (this.$store.state.movies.length === 0) {
          this.$store.state.movies = res.data
          console.log(this.$store.state.movies)
        }
      })
      .catch( (err) => {
        console.log(err)
      })
    },
  },
  created() {
    if (this.$store.state.movies === []) {
      this.getMovies()
    }
  },
}
</script>

<style>

</style>