<template>
  <div>

    
    
    <carousel-3d :width="400" :height="525">
    <slide :index="0">
      <img :src="this.random_top_movie_list[0]" alt="">
    </slide>
    <slide :index="1">
      <img :src="this.random_top_movie_list[1]" alt="">
    </slide>
    <slide :index="2">
      <img :src="this.random_top_movie_list[2]" alt="">
    </slide>
    <slide :index="3">
      <img :src="this.random_top_movie_list[3]" alt="">
    </slide>
    <slide :index="4">
      <img :src="this.random_top_movie_list[4]" alt="">
    </slide>
    <slide :index="5">
      <img :src="this.random_top_movie_list[5]" alt="">
    </slide>
    <slide :index="6">
      <img :src="this.random_top_movie_list[6]" alt="">
    </slide>
    <slide :index="7">
      <img :src="this.random_top_movie_list[7]" alt="">
    </slide>
    <slide :index="8">
      <img :src="this.random_top_movie_list[8]" alt="">
    </slide>
    <slide :index="9">
      <img :src="this.random_top_movie_list[9]" alt="">
    </slide>

  </carousel-3d>
  
  </div>
</template>

<script>
// import axios from 'axios'
import { Carousel3d, Slide } from 'vue-carousel-3d'



export default {
  name: 'HomeView',

  data () {
    return {
      top_movie_poster_list: [],
      random_top_movie_list: JSON.parse(localStorage.getItem("random_top_movie_list")),
      
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  components: {
    Carousel3d,
    Slide
  },
  methods: {
    
  },
}
</script>

<style>

</style>