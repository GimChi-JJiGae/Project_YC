<template>
  <div>
    <div>
      <div id="container" class="box" ><!--style="padding-bottom:20px;">-->
        <div v-for="(idx, k) in genre_list" :index="idx" :key="k">
          <button :id="genre_list[k][`id`]" class="btn btn-outline-secondary" @click="recommend">{{ genre_list[k]["name"] }}</button>
        </div>
      </div>
      <div id="recommendedmovies" class="row">
        <div id="loop" v-for="movie in paginatedData" :movie="movie" :key="movie.id" class="col-3">
          <div class="my-2">
            <a :href='`http://localhost:8080/movies/${movie[`id`]}`'>
              <img :src="`https://image.tmdb.org/t/p/original/${movie[`poster_path`]}`" alt="" height="280" width="180">
            </a>
          </div>
        </div>
      </div>
      <div id="paganation">
        <button :disabled="pageNum === 0" @click="prevPage" class="btn content-font border btn-sm me-1">
          이전
        </button>
        <span class="page-count"><small>{{ pageNum + 1 }} / {{ pageCount }} 페이지</small></span>
        <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="btn content-font border btn-sm ms-1">
          다음
        </button>
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
      pageNum: 0,
      pageSize: 20,
    }
  },
  computed: {
    pageCount () {
      let listLeng = this.movie_list.length,
        listSize = this.pageSize,
        page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      if (page === 0) page = 1
      
      /*
      아니면 page = Math.floor((listLeng - 1) / listSize) + 1;
      이런식으로 if 문 없이 고칠 수도 있다!
      */
      return page;
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
        end = start + this.pageSize;
      return this.movie_list.slice(start, end);
    },
  },
  methods: {
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },
    get_data() {
      this.genre_list = JSON.parse(localStorage.getItem('genres'))
      this.movie_list = JSON.parse(localStorage.getItem('movie_list'))
    },
    recommend: function(event) {
      const recommendedmovies = document.querySelector('#recommendedmovies')
      const paganation = document.querySelector('#paganation')
      const genreId = event.target.id
      axios ({
        method : 'get',
        url : `http://127.0.0.1:8000/movies/recommended/${genreId}/`,
      })
        .then ((response) => {
          while ( recommendedmovies.hasChildNodes() ) {
            recommendedmovies.removeChild( recommendedmovies.firstChild );       
          }
          while ( paganation.hasChildNodes() ) {
            paganation.removeChild( paganation.firstChild );       
          }
          //const as = document.querySelectorAll('a')
          //as.forEach(function(a){
          //      a.remove()
          //  })
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