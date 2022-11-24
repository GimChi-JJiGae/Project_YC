<template>
  <div>


  <carousel-3d :width="450" :height="630" :autoplay="true" :autoplayHoverPause="true" :loop="true" background-size="cover">
    <slide v-for="(slide, i) in slides" :index="i" :key="slide">

      <div id="wrap_for_top">
      <img :src='`https://image.tmdb.org/t/p/original/${random_top_movie_list[i].poster_path}`' alt="">
      <div class="title">
        <StarRating class="more justify-content-center"
            active-color="#FF8C0A"
            :show-rating="false"
            :rating="parseFloat(random_top_movie_list[i].vote_average) / 2"
            :read-only="true"
            :increment="0.01"
            :star-size="40"
            />
        <router-link class="more" :to="{name : 'MovieDetail', params : {movie_pk : random_top_movie_list[i].id }}">상세 페이지</router-link>
        <!--<a class="more" :href='`http://localhost:8080/movies/${random_top_movie_list[i].id}`'>Detail</a>-->
      </div>
    </div>
    </slide>
  </carousel-3d>



  <div>인기순</div> <!-- 로그인시, 추천영화영화를 뽑을수있게 데이터가 설정된 경우만 보이게 하자-->
  <!--Carousel Wrapper-->
  
  <carousel-3d :width="300" :height="420" :disable3d="true" :space="365" :clickable="false" :controls-visible="true" >
    <slide v-for="(slide, i) in slides" :index="i" :key="slide">
    
    <div id="wrap">
    <img :src='`https://image.tmdb.org/t/p/original/${popular_movie_list[i].poster_path}`' alt="">
    <div class="title">
      <StarRating class="more justify-content-center"
            active-color="#FF8C0A"
            :show-rating="false"
            :rating="parseFloat(popular_movie_list[i].vote_average) / 2"
            :read-only="true"
            :increment="0.01"
            :star-size="40"
            />
      <router-link class="more" :to="{name : 'MovieDetail', params : {movie_pk : popular_movie_list[i].id }}">상세 페이지</router-link>
      <!--<a class="more" :href='`http://localhost:8080/movies/${popular_movie_list[i].id}`'>Detail</a>-->
    </div>
  </div>
    
    </slide>
  </carousel-3d>

  <div>평점순</div>

  <carousel-3d :width="300" :height="420" :disable3d="true" :space="365" :clickable="false" :controls-visible="true" >
    <slide v-for="(slide, i) in slides" :index="i" :key="slide">
    
    <div id="wrap">
    <img :src='`https://image.tmdb.org/t/p/original/${high_vote_movie_list[i].poster_path}`' alt="">
    <div class="title">
      <StarRating class="more justify-content-center"
            active-color="#FF8C0A"
            :show-rating="false"
            :rating="parseFloat(high_vote_movie_list[i].vote_average) / 2"
            :read-only="true"
            :increment="0.01"
            :star-size="40"
            />
      <router-link class="more" :to="{name : 'MovieDetail', params : {movie_pk : high_vote_movie_list[i].id }}">상세 페이지</router-link>
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
import StarRating from "vue-star-rating";

export default {
  name: 'HomeView',
  random_num: null,

  data () {
    return {
      popular_movie_list: JSON.parse(localStorage.getItem("popular_movie_list")),
      random_top_movie_list: JSON.parse(localStorage.getItem("random_top_movie_list")),
      high_vote_movie_list: JSON.parse(localStorage.getItem("high_vote_movie_list")),
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
    StarRating,
 
  },
  methods: {
    getNumber() {
      let rand = 0
      while(rand < 20){
        rand = Math.floor(Math.random() * 19)
        if (rand !== 8){
          break
        }
      }
    }
  },
  created() {
    this.getNumber()
  }
}
</script>

<style>


#wrap_for_top {margin:0 auto; text-align:center; width:450px;}
.title {line-height:1; color:#E6FFE6; position:absolute; left:50%; transform:translateX(-50%); top:200px; height:120px; transition:0.5s all}
.title h3 {font-size:30px;  margin:0}
.title p {font-size:14px; margin-top:15px;}
.more {display:block; font-size:18x; color:#FF8C0A; background:#E6FFE6; line-height:60px; width:220px; margin-top:30px; opacity:0; transition:0.5s all}

#wrap_for_top:hover .more {opacity:0.7}
#wrap_for_top:hover .title {top:150px}

#wrap {margin:0 auto; text-align:center; width:300px;}

.title {line-height:1; color:#E6FFE6; position:absolute; left:50%; transform:translateX(-50%); top:200px; height:120px; transition:0.5s all}
.title h3 {font-size:30px;  margin:0}
.title p {font-size:14px; margin-top:15px;}
.more {display:block; font-size:18x; color:#FF8C0A; background:#E6FFE6; line-height:60px; width:220px; margin-top:30px; opacity:0; transition:0.5s all}

#wrap:hover .more {opacity:0.7}
#wrap:hover .title {top:150px}

</style>