<template>
  <div class="border p-2 rounded-3 row align-items-center justify-content-center">

    <!--<iframe width="560" height="315" :src="this.youtubeLink" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>-->
    <!--<iframe width="100%" height="700px" src="https://youtu.be/rrI7tOhoVzA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>-->
    <div class="row">
      <MovieDetailTop :movie="movie"/>
    </div>
    <div class="row">
      <MovieDetailCommentList/>
    </div>
    <div class="row">
      <MovieDetailRelated/>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetailTop from '@/components/MovieDetailTop.vue'
import MovieDetailRelated from '@/components/MovieDetailRelated.vue'
import MovieDetailCommentList from '@/components/MovieDetailCommentList.vue'
//const youtube = document.getElementById("youtube");




export default {
  name: 'MovieDetail',
  data : function(){
    return {
      movie : {},
      youtubeLink : '안...',
      same_genres : '',
      movieYoutubeUrl : '',
    }
  },
  components : {
    MovieDetailTop,
    MovieDetailRelated,
    MovieDetailCommentList,
  },
  methods : {
    
    getMovie : function(){
      const movie_data = JSON.parse(localStorage.getItem('movie_list'))[this.$route.params.movie_pk - 1]
     
      const movie_original_id = movie_data.original_id
      const url = 'https://api.themoviedb.org/3/movie/' + movie_original_id + '?api_key=5d2592924ae354925561438e12ee8888&language=ko-KR' 
      //let youtubeId = ''//첫번재 영상만 사용하기 하자. 값이 없을 경우도 있음.
      axios.get(url)
        .then((res) => {
        
          this.movie = res.data
          
          //this.movie = res.data['movie'][0]
          //console.log(this.movie)
          //this.same_genres = res.data.same_genres
        })
        .catch(() => {
          alert("없는 영화 정보입니다.")
          //this.$router.push({name : 'HomeView'})
        })
          /*
           fetch(movieUrl)
                .then(res => res.json())
                .then((res) => {
                    
                    
                    if(res.results.length > 0){
                        youtubeId = res.results[0].key//첫번재 영상만 사용하기 하자. 값이 없을 경우도 있음.
                        console.log(youtubeId)
                        //this.youtubeLink = `<iframe width="100%" height="100%" src="https://www.youtube.com/embed/${youtubeId}?autoplay=1"></iframe>`;
                        this.youtubeLink = `https://www.youtube.com/embed/${youtubeId}?autoplay=1`  
                        
                    } else {
                        //output = `<h3 class="noVideo">재생할 예고편이 없습니다.</h3>`;
                        //console.log(output);
                    }
                    
                    //youtube.innerHTML = output;
                })
                .catch(erro => console.log(erro));
        })
       
        .catch(() => {
          alert("없는 영화 정보입니다.")
          //this.$router.push({name : 'HomeView'})
        })
         */
        
      
    },
    
  },

  created : function(){
    
    this.getMovie()
    
    
  }
}
</script>

<style>

</style>