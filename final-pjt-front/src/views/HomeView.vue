<template>
  <div>

    <carousel-3d :width="400" :height="570" :autoplay="true" :autoplayHoverPause="true" :loop="true">
    <slide :index="0">
      <img :src='`https://image.tmdb.org/t/p/original/${this.random_top_movie_list[0].poster_path}`' alt="">
    </slide>
    <slide :index="1">
      <img :src='`https://image.tmdb.org/t/p/original/${this.random_top_movie_list[1].poster_path}`' alt="">
    </slide>
    <slide :index="2">
      <img :src='`https://image.tmdb.org/t/p/original/${this.random_top_movie_list[2].poster_path}`' alt="">
    </slide>
    <slide :index="3">
      <img :src='`https://image.tmdb.org/t/p/original/${this.random_top_movie_list[3].poster_path}`' alt="">
    </slide>
    <slide :index="4">
      <img :src='`https://image.tmdb.org/t/p/original/${this.random_top_movie_list[4].poster_path}`' alt="">
    </slide>
    <slide :index="5">
      <img :src='`https://image.tmdb.org/t/p/original/${this.random_top_movie_list[5].poster_path}`' alt="">
    </slide>
    <slide :index="6">
      <img :src='`https://image.tmdb.org/t/p/original/${this.random_top_movie_list[6].poster_path}`' alt="">
    </slide>
    <slide :index="7">
      <img :src='`https://image.tmdb.org/t/p/original/${this.random_top_movie_list[7].poster_path}`' alt="">
    </slide>
    <slide :index="8">
      <img :src='`https://image.tmdb.org/t/p/original/${this.random_top_movie_list[8].poster_path}`' alt="">
    </slide>
    <slide :index="9">
      <img :src='`https://image.tmdb.org/t/p/original/${this.random_top_movie_list[9].poster_path}`' alt="">
    </slide>

  </carousel-3d>
  <div>추천영화</div> <!-- 로그인시, 추천영화영화를 뽑을수있게 데이터가 설정된 경우만 보이게 하자-->
  <!--Carousel Wrapper-->
  
  <carousel-3d :width="300" :height="420" :disable3d="true" :space="365" :clickable="false" :controls-visible="true" >
    <slide v-for="(slide, i) in slides" :index="i" :key="slide">
      <img :src='`https://image.tmdb.org/t/p/original/${popular_movie_list[i].poster_path}`' alt="">
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
      popular_movie_list: JSON.parse(localStorage.getItem("popular_movie_list")),
      random_top_movie_list: JSON.parse(localStorage.getItem("random_top_movie_list")),
      

      slides: 10
      
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  components: {
    Carousel3d,
    Slide,
  
  },
  methods: {
    
  },
}
</script>

<style>



</style>