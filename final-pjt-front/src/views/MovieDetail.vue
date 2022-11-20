<template>
  <div>

    <iframe width="560" height="315" :src="this.youtubeLink" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <!--<iframe width="100%" height="700px" src="https://youtu.be/rrI7tOhoVzA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>-->
    <div>{{ movie.id }}</div>
  </div>
</template>

<script>
import axios from 'axios'
//const youtube = document.getElementById("youtube");

export default {
  name: 'MovieDetail',
  data : function(){
    return {
      movie : '',
      youtubeLink : '',
      same_genres : '',
      movie_url : '',
    }
  },
  methods : {
    getMovie : function(){
      const url = 'https://api.themoviedb.org/3/movie/'+ this.$route.params.movie_pk + '?api_key=5d2592924ae354925561438e12ee8888&language=ko-KR' 
      // let youtubeId = ''//첫번재 영상만 사용하기 하자. 값이 없을 경우도 있음.
      console.log(url)
      axios.get(url)
        .then((res) => {
          console.log(res.data)
          this.movie = res.data
          console.log(this.movie)
          //this.movie = res.data['movie'][0]
          //console.log(this.movie)
          //this.same_genres = res.data.same_genres
          this.movie_url = `https://api.themoviedb.org/3/movie/${this.movie.id}/videos?api_key=5d2592924ae354925561438e12ee8888`
          console.log(this.movie_url)
          console.log(this.movie.id)
          
        })
        .then(()=>{
          fetch(this.movieUrl)
                .then(res => res.json())
                .then((res) => {
                    
                    
                    if(res.results.length > 0){
                        const youtubeId = res.results[0].key//첫번재 영상만 사용하기 하자. 값이 없을 경우도 있음.
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
          //this.getYoutubeLink()
        })
          /*
          const movieUrl = `https://api.themoviedb.org/3/movie/${this.movie.id}/videos?api_key=5d2592924ae354925561438e12ee8888`
          
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
        */
        .catch(() => {
          alert("없는 영화 정보입니다.")
          this.$router.push({name : 'HomeView'})
        })
        
        
      }
  },
  getYoutubeLink : function(){
    axios.get(this.movie_url)
    .then((res) => {
      console.log(res.data)
      if(res.results.length > 0){
        this.youtubeId = res.results[0].key//첫번재 영상만 사용하기 하자. 값이 없을 경우도 있음.
        console.log(this.youtubeId)
                        //this.youtubeLink = `<iframe width="100%" height="100%" src="https://www.youtube.com/embed/${youtubeId}?autoplay=1"></iframe>`;
        this.youtubeLink = `https://www.youtube.com/embed/${this.youtubeId}?autoplay=1`  
                        
      } else {
                        //output = `<h3 class="noVideo">재생할 예고편이 없습니다.</h3>`;
                        //console.log(output);
                    }
                    
                    //youtube.innerHTML = output;
      })
      .catch(() =>{
        alert("유튜브 링크 실패")
      })
  },



  created : function(){
    this.getMovie()
    
  }
}
</script>

<style>

</style>