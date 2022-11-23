<template>
  <div>여기는 장르 영화 탐색용
    <div id="app">
    <div id="container" class="box" ><!--style="padding-bottom:20px;">-->
        <div v-for="(idx, k) in genre_list" :index="idx" :key="k">
            <button :id="genre_list[k][`id`]" class="btn btn-outline-secondary" @click="recommend">{{ genre_list[k]["name"] }}</button>
        </div>
    </div>
    <div id="recommendedmovies" class="row">
        <div id="loop" v-for="(idx, j) in movie_list" :index="idx" :key="j" class="col-3">
          <div class="my-2">
            <a :href='`http://localhost:8080/movies/${movie_list[j][`id`]}`'>
              
            <img :src="`https://image.tmdb.org/t/p/original/${movie_list[j][`poster_path`]}`" alt="" height="280" width="180">
            </a>
        </div>
        </div>
    </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'GenreMovies',
    data: function() {
      return {
        genre_list: [],
        movie_list: [],
        recommended_movie_list: [],
      }
    },
    methods: {
      get_data() {
        this.genre_list = JSON.parse(localStorage.getItem('genres'))
        this.movie_list = JSON.parse(localStorage.getItem('movie_list'))
      },
      recommend: function(event) {
        const recommendedmovies = document.querySelector('#recommendedmovies')
        const genreId = event.target.id
        axios ({
                    method : 'get',
                    url : `http://127.0.0.1:8000/movies/recommended/${genreId}/`,
                })
                .then ((response) => {
                  
                  while ( recommendedmovies.hasChildNodes() )
                  {
                      recommendedmovies.removeChild( recommendedmovies.firstChild );       
                  }
                  const as = document.querySelectorAll('a')
                  as.forEach(function(a){
                        a.remove()
                    })
                    const forIdCheck = JSON.parse(localStorage.getItem('movie_list'))
                    this.recommendedmovies = []
                    this.recommendedmovies.push(response.data)
                    this.recommendedmovies[0].forEach(movie => {
                        let movieId = null
                        const imgTag = document.createElement('img')
                        const aTag = document.createElement('a')
                        for(let i=0; i < forIdCheck.length; i++){
                          if (movie.original_id === forIdCheck[i].original_id){
                            movieId = forIdCheck[i].id
                            break
                          }
                        }
                        
                        aTag.setAttribute('href', `http://localhost:8080/movies/${movieId}/`)
                        aTag.setAttribute('class', 'col-3')
                        imgTag.setAttribute('src', `https://image.tmdb.org/t/p/original/${movie.poster_path}`)
                        imgTag.setAttribute('style','width:180px; height:280px; margin:1rem;')
                        aTag.appendChild(imgTag)     
                        recommendedmovies.appendChild(aTag)
                    })
                })
      }
    },
    created() {
      this.get_data()
    }
}
</script>

<style>
#app {
    font-family: 'Noto Sans KR', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #424242;
    margin-top: 60px;
}
#container {
    display : grid;
    grid-template-columns: 150px 150px 150px 150px 150px ;
    grid-template-rows: 50px 50px 50px 50px ;
}
.box {
    display: flex;
    justify-content: center;
}
</style>