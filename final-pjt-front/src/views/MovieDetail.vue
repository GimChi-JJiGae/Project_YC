<template>
  <div>
    <iframe width="100%" height="700px" :src="movie | videoURL" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieDetail',
  data : function(){
    return {
      movie : '',
      same_genres : ''
    }
  },
  methods : {
    getMovie : function(){
      const url = 'https://api.themoviedb.org/3/movie/'+ this.$route.params.movie_pk + '?api_key=5d2592924ae354925561438e12ee8888&language=ko-KR' 
      console.log(url)
      axios.get(url)
        .then((res) => {
          console.log(res.data)
          //this.movie = res.data['movie'][0]
          //console.log(this.movie)
          //this.same_genres = res.data.same_genres
        })
        .catch(() => {
          alert("없는 영화 정보입니다.")
          this.$router.push({name : 'HomeView'})
        })
    }
  },
  filters : {
    videoURL : function(movie) {
      const youtubeURL = "https://www.youtube.com/embed/"
      return youtubeURL+movie.video_path
    }
  },
  created : function(){
    this.getMovie()
  }
}
</script>

<style>

</style>