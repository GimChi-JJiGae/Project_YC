<template>
  <div>


  <carousel-3d :width="450" :height="600" :autoplay="true" :autoplayHoverPause="true" :loop="true" background-size="cover">
    <slide v-for="(slide, i) in slides" :index="i" :key="slide">

      <div id="wrap_for_top">
      <img :src='`https://image.tmdb.org/t/p/original/${random_top_movie_list[i].poster_path}`' alt="">
      <div class="title">
        <h3 class="more">평점</h3>
        <router-link class="more" :to="{name : 'MovieDetail', params : {movie_pk : random_top_movie_list[i].id }}">Detail</router-link>
        <!--<a class="more" :href='`http://localhost:8080/movies/${random_top_movie_list[i].id}`'>Detail</a>-->
      </div>
    </div>
    </slide>
  </carousel-3d>



  <div>추천영화</div> <!-- 로그인시, 추천영화영화를 뽑을수있게 데이터가 설정된 경우만 보이게 하자-->
  <!--Carousel Wrapper-->
  
  <carousel-3d :width="300" :height="420" :disable3d="true" :space="365" :clickable="false" :controls-visible="true" >
    <slide v-for="(slide, i) in slides" :index="i" :key="slide">
    
    <div id="wrap">
    <img :src='`https://image.tmdb.org/t/p/original/${popular_movie_list[i].poster_path}`' alt="">
    <div class="title">
      <h3 class="more">평점</h3>
      <router-link class="more" :to="{name : 'MovieDetail', params : {movie_pk : popular_movie_list[i].id }}">Detail</router-link>
      <!--<a class="more" :href='`http://localhost:8080/movies/${popular_movie_list[i].id}`'>Detail</a>-->
    </div>
  </div>
    
    </slide>
  </carousel-3d>


  </div>
</template>

<script>
// import axios from 'axios'
import { Carousel3d, Slide } from 'vue-carousel-3d'
//import MovieDetail from '@/components/MovieDetail.vue'


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

#wrap_for_top {margin:0 auto; text-align:center; width:450px;}
.title {line-height:1; color:red; position:absolute; left:50%; transform:translateX(-50%); top:200px; height:120px; transition:0.5s all}
.title h3 {font-size:30px;  margin:0}
.title p {font-size:14px; margin-top:15px;}
.more {display:block; font-size:18x; color:#fff; background:red; line-height:40px; width:120px; margin-top:30px; opacity:0; transition:0.5s all}

#wrap_for_top:hover .more {opacity:1}
#wrap_for_top:hover .title {top:150px}

#wrap {margin:0 auto; text-align:center; width:300px;}

.title {line-height:1; color:red; position:absolute; left:50%; transform:translateX(-50%); top:200px; height:120px; transition:0.5s all}
.title h3 {font-size:30px;  margin:0}
.title p {font-size:14px; margin-top:15px;}
.more {display:block; font-size:18x; color:#fff; background:red; line-height:40px; width:120px; margin-top:30px; opacity:0; transition:0.5s all}

#wrap:hover .more {opacity:1}
#wrap:hover .title {top:150px}

</style>