<template>
  <div>

    <!--<iframe width="560" height="315" :src="this.youtubeLink" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>-->
    <!--<iframe width="100%" height="700px" src="https://youtu.be/rrI7tOhoVzA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>-->
    
    <MovieDetailTop :movie="movie"/>
    <MovieDetailYoutube :movieYoutubeUrl="movieYoutubeUrl"/>
    <MovieDetailRelated/>
    
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetailYoutube from '@/components/MovieDetailYoutube.vue'
import MovieDetailTop from '@/components/MovieDetailTop.vue'
import MovieDetailRelated from '@/components/MovieDetailRelated.vue'

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
    MovieDetailYoutube,
    MovieDetailTop,
    MovieDetailRelated,
    
},
  methods : {
    
    getMovie : function(){
      const url = 'https://api.themoviedb.org/3/movie/'+ this.$route.params.movie_pk + '?api_key=5d2592924ae354925561438e12ee8888&language=ko-KR' 
      //let youtubeId = ''//첫번재 영상만 사용하기 하자. 값이 없을 경우도 있음.
      
      axios.get(url)
        .then((res) => {
        
          this.movie = res.data
          
          //this.movie = res.data['movie'][0]
          //console.log(this.movie)
          //this.same_genres = res.data.same_genres
          
          this.movieYoutubeUrl = `https://api.themoviedb.org/3/movie/${this.movie.id}/videos?api_key=5d2592924ae354925561438e12ee8888`
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
        
      
    }
  },

  created : function(){
    
    this.getMovie()
    
    
  }
}
</script>

<style>

</style>