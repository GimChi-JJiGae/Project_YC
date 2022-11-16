<template>
  <div>
    <img :src="this.top_movie_poster_list[8]" alt="">
    <carousel-3d>
    <slide :index="0">
      {{ this.top_movie_poster_list[0] }}
    </slide>
    <slide :index="1">
      {{ this.top_movie_poster_list[1] }}
    </slide>
    <slide :index="2">
      {{ this.top_movie_poster_list[2] }}
    </slide>
    <slide :index="3">
      {{ this.top_movie_poster_list[3] }}
    </slide>
    <slide :index="4">
      {{ this.top_movie_poster_list[4] }}
    </slide>
    <slide :index="5">
      {{ this.top_movie_poster_list[5] }}
    </slide>
    <slide :index="6">
      {{ this.top_movie_poster_list[6] }}
    </slide>
    <slide :index="7">
      {{ this.top_movie_poster_list[7] }}
    </slide>
    <slide :index="8">
      
      {{ this.top_movie_poster_list[8] }}
    </slide>
    <slide :index="9">
      {{ this.top_movie_poster_list[9] }}
    </slide>

  </carousel-3d>
    
  </div>
</template>

<script>
import axios from 'axios'
import { Carousel3d, Slide } from 'vue-carousel-3d'
import _ from 'lodash'


export default {
  name: 'HomeView',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  
  methods: {
    pick_top_poster_images: function () {
      for (let i = 0; i<10; i++) {
        let number = _.range(0, 979)
        this.top_movie_poster_list.push(this.$store.state.movies[number].poster_path)
      }
    },
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
    this.pick_top_poster_images()
    console.log(this.top_movie_poster_list)
  },
}
</script>

<style>

</style>