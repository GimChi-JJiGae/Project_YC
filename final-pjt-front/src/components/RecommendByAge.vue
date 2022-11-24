<template>
  <div>
      <div class="row flex-nowrap" id="scollbar">
          <span v-for="pick_movie in picked_movie_show_list" :key=pick_movie.id style="width:190px;">
            <a :href='`http://localhost:8080/movies/${pick_movie.id}`'>
            <img :src='`https://image.tmdb.org/t/p/original/${pick_movie.poster_path}`' alt="" style="height:230px; width:180px;" class="rounded-2">
            <!--<router-link :to="{name : 'MovieDetail', params : {movie_pk : pick_movie.id }}">
              <img :src='`https://image.tmdb.org/t/p/original/${pick_movie.poster_path}`' alt="" style="height:230px; width:180px;" class="rounded-2">
            </router-link>-->
          </a>
        </span>
    </div>
  </div>
  
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'RecommendByAge',
  props: {
    age_to_recommend: String,
    like_movies: Array,
  },
  data() {
    return {
      slides: 10,
      users_list: [],
      genre_dict: {'12': 0, '14': 0, '16': 0, '18':0, '27':0, '28': 0,
                  '35': 0, '36': 0, '37': 0, '53': 0, '80': 0, '99': 0,
                  '878': 0, '9648': 0, '10402': 0, '10749': 0, '10751': 0,
                  '10752': 0, '10770': 0},
      all_movie_data: [],
      list_for_calculate: [],
      recommend_movie_list: [],
      picked_movie: [],
      picked_movie_show_list: [],
    }
  },
  methods: {
    makeRecommendation() {
      axios.get(`${SERVER_URL}/accounts/users/`)
      .then((res)=>{
        
        this.users_list = res.data
        this.all_movie_data = JSON.parse(localStorage.getItem('movie_list'))
      })
      .catch((err) => {
        console.log(err)
      })
      .then(() =>
        this.putDictData()
      )
      .then(() => 
        this.getMychart()
      )
      .then(()=>
        this.cal_movies()
      )
      .then(()=>
        this.pick_movies()
      )
    


    },
    putDictData() {
      for(let i = 0; i < this.users_list.length; i++){
        if (this.users_list[i].age === this.age_to_recommend) {
          for(let j = 0; j < this.users_list[i].like_movies.length; j++){
            
            for(let k = 0; k < this.all_movie_data[this.users_list[i].like_movies[j] - 1]['genres'].length; k++){
              
              this.genre_dict[String(this.all_movie_data[this.users_list[i].like_movies[j] - 1]['genres'][k])] = this.genre_dict[String(this.all_movie_data[this.users_list[i].like_movies[j] - 1]['genres'][k])] + 1
              //console.log(this.genre_dict[String(this.all_movie_data[this.users_list[i].like_movies[j] - 1].gernes[k])])
            }
          }
        }
      }
     
    },
    getMychart() {
      
      //const out = Object.fromEntries(
      //  Object.entries(this.genre_dict).sort(([,a],[,b]) => a > b? -1: 1 )
      //);
      //console.log(out)

      let for_sort = [];
      for (let num in this.genre_dict){
        for_sort.push([num, this.genre_dict[num]])
      }
      for_sort.sort(function(a, b){
        return b[1] - a[1];
      })
      for(let i = 0; i < 3; i++){
        this.list_for_calculate.push(for_sort[i])
      }
    },
    cal_movies(){
      
      for(let i = 0; i < this.all_movie_data.length; i++){
        let sum_of_this_movie = 0
        for(let j = 0; j < 3; j++){
          for(let k = 0; k < this.all_movie_data[i]['genres'].length; k++){
            
            if(Number(this.list_for_calculate[j][0]) === this.all_movie_data[i]['genres'][k]){
              sum_of_this_movie = sum_of_this_movie + ((this.list_for_calculate[j][1] * this.all_movie_data[i]['popularity']) / 90)
              break
            }
          }
        }
        this.recommend_movie_list.push([i,sum_of_this_movie])
      }
    },
    pick_movies(){
      this.recommend_movie_list.sort((prev, cur) => {  // 2번째 배열 요소를 기준으로 오름차순
        if (prev[1] < cur[1]) return 1;
        if (prev[1] > cur[1]) return -1;
      });
      
      for(let i = 0; i < this.all_movie_data.length; i++){
        let check = false
        for(let j = 0; j < this.like_movies.length; j++){
        
          if(this.like_movies[j].id === this.recommend_movie_list[i][0]){
            check = true
          }
        }
        if (check === false){
          this.picked_movie.push(this.recommend_movie_list[i][0])
        }
        if(this.picked_movie.length === 40){
          break
        }
      }
      
      this.picked_movie.sort(() => Math.random() - 0.5)
      
      this.picked_movie = this.picked_movie.slice(0, 10)
 
      for(let i = 0; i < 10; i++){
        this.picked_movie_show_list.push(this.all_movie_data[this.picked_movie[i]])
      }



    }
    

  },
  created() {
    this.makeRecommendation()
  }
}
</script>

<style>
#scollbar {
  overflow: auto;
  width: 100%;
}
#scollbar::-webkit-scrollbar {
  width: 5px;
  height: 10px;
  /* display: none; */
}
#scollbar::-webkit-scrollbar-thumb {
  background-color: #2f3542;
  border-radius: 10px;
  background-clip: padding-box;
  border: 1px solid transparent;
}
#scollbar::-webkit-scrollbar-track {
  background-color: grey;
  border-radius: 10px;
  box-shadow: inset 0px 0px 5px white;
}
</style>