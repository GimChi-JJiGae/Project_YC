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



  <div style="text-align:left; font: bold 1.5em/1em Pretendard Variable, serif ; color: orange;">인기순</div> <!-- 로그인시, 추천영화영화를 뽑을수있게 데이터가 설정된 경우만 보이게 하자-->
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

  <div style="text-align:left; font:  1.5em/1em Pretendard Variable, serif ; color: orange;">평점순</div>

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
  <p style="text-align:left; font: 1.5em/1em Pretendard Variable, serif ; color: orange;">오늘은 {{ genre_list[random_num] }} 장르 어떠신가요? </p>
  <carousel-3d :width="300" :height="420" :disable3d="true" :space="365" :clickable="false" :controls-visible="true" >
    <slide v-for="(slide, i) in slides" :index="i" :key="slide">
    
    <div id="wrap">
    <img :src='`https://image.tmdb.org/t/p/original/${TodayList[i].poster_path}`' alt="">
    <div class="title">
      <StarRating class="more justify-content-center"
            active-color="#FF8C0A"
            :show-rating="false"
            :rating="parseFloat(TodayList[i].vote_average) / 2"
            :read-only="true"
            :increment="0.01"
            :star-size="40"
            />
      <router-link class="more" :to="{name : 'MovieDetail', params : {movie_pk : TodayList[i].id }}">상세 페이지</router-link>
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
  

  data () {
    return {
      popular_movie_list: JSON.parse(localStorage.getItem("popular_movie_list")),
      random_top_movie_list: JSON.parse(localStorage.getItem("random_top_movie_list")),
      high_vote_movie_list: JSON.parse(localStorage.getItem("high_vote_movie_list")),
      slides: 10,
      random_num: null,
      genre_list: ['모험', '판타지', '애니메이션', '드라마', '공포', '액션', '코미디', '역사', '서부-이건안씀',
               '스릴러', '범죄', '다큐멘터리', 'SF', '미스터리', '음악', '로맨스', '가족', '전쟁', 'TV 영화'],
              
      genre_list2: [12, 14, 16, 18, 27, 28, 35, 36, 37, 53, 80, 99, 878, 9648, 10402, 10749, 10751, 10752, 10770],
      movie_list: [],
      TodayList: [],
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
    makeTodayList(){
      this.movie_list = JSON.parse(localStorage.getItem('movie_list'))
      for(let i = 0; i < this.movie_list.length; i++){
        if(this.movie_list[i]['genres'].includes(this.genre_list2[this.random_num])){
          this.TodayList.push(this.movie_list[i])
        }
        if(this.TodayList.length === 10){
          break
        }
      }
    },
    getNumber() {
      let rand = 0
      while(rand < 20){
        rand = Math.floor(Math.random() * 19)
        if (rand !== 8){
          break
        }
      }
      this.random_num = rand
      this.makeTodayList()
      //console.log(this.genre_list[this.random_num])
      //console.log(this.TodayList)
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