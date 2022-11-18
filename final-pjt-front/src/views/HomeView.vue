<template>
  <div>
    
    <carousel-3d :width="400" :height="525">
    <slide :index="0">
      <img :src="this.top_movie_poster_list[0]" alt="">
    </slide>
    <slide :index="1">
      <img :src="this.top_movie_poster_list[1]" alt="">
    </slide>
    <slide :index="2">
      <img :src="this.top_movie_poster_list[2]" alt="">
    </slide>
    <slide :index="3">
      <img :src="this.top_movie_poster_list[3]" alt="">
    </slide>
    <slide :index="4">
      <img :src="this.top_movie_poster_list[4]" alt="">
    </slide>
    <slide :index="5">
      <img :src="this.top_movie_poster_list[5]" alt="">
    </slide>
    <slide :index="6">
      <img :src="this.top_movie_poster_list[6]" alt="">
    </slide>
    <slide :index="7">
      <img :src="this.top_movie_poster_list[7]" alt="">
    </slide>
    <slide :index="8">
      <img :src="this.top_movie_poster_list[8]" alt="">
    </slide>
    <slide :index="9">
      <img :src="this.top_movie_poster_list[9]" alt="">
    </slide>

  </carousel-3d>
  <button @click="pick_top_poster_images"></button>
  </div>
</template>

<script>
// import axios from 'axios'
import { Carousel3d, Slide } from 'vue-carousel-3d'
import _ from 'lodash'
import { onUpdated } from 'vue'

onUpdated(() => {
  // text content should be the same as current `count.value`
  console.log('wow')
})

export default {
  name: 'HomeView',

  data () {
    return {
      top_movie_poster_list: []
      
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
    pick_top_poster_images: function () {
      for (let i = 0; i<10; i++) {
        let number = _.random(0, 979)
        
        const movie_list_info = JSON.parse(localStorage.getItem("movie_list"))
        console.log("https://image.tmdb.org/t/p/original/" + movie_list_info[number].poster_path)
        if (this.$store.state.movies[number].poster_path){ // 포스터 패스가 없을 경우는 다른걸 찾는다
          this.top_movie_poster_list.push("https://image.tmdb.org/t/p/original/" + this.$store.state.movies[number].poster_path)
        }
        else {
          i = i - 1
        }
      }
    },
  },
}
</script>

<style>

</style>