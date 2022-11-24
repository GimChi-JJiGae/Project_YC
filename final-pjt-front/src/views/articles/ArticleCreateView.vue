<template>
  <div>
    <h2>게시글 작성</h2>
    <div class="border p-4">
      <div class="row">
        <input class="border-dark p-2 border-opacity-10" type="text" id="title" v-model.trim="title" placeholder="제목을 입력하세요."><br>
      </div>
      <div class="row mt-4">
        <input class="border-dark p-2 border-opacity-10" id="movie" v-model.trim="movie_title" placeholder="영화 검색" disabled><br>
        <button class="btn content-font border btn-sm" style="height:36px;" @click="open">
          <span style="font-size: 16px;">영화 검색</span>
        </button>
        <b-modal
          hide-footer
          v-model="show"
          id="review-modal"
          size="lg"
          title="영화 검색창"
          hide-header-close
        >
          <section class="page-section" id="contact">
            <div class="col row m-0" style="width: 100%">
              <input class="stage-search border-opacity-10 rounded-2" type="text" v-model="search" placeholder="영화명" @input="handleSearchInput" style="width:100%; height:36px;"/>
            </div>
            <div>
              <ul class="list-group list-group-flush" style="width:100%;" id="scollbar">
                <li
                  v-for="(movie, idx) in Movies"
                  :key="idx"
                  class="list-group-item"
                  style="height: 100%; cursor:pointer;"
                >
                  <div class="row" @click="getMovie(movie)">
                    <div class="col">
                      {{movie.title}}
                    </div>
                    <div class="col-2">
                      {{movie.release_date}}
                    </div>
                  </div>
                </li>
              </ul>
            </div>
            <div>
              <button @click="close" class="m-1 btn content-font border btn-sm" type="submit">닫기</button>
            </div>
          </section>
        </b-modal>
      </div>
      <div class="row mt-4">
        <textarea class="border-dark p-2 border-opacity-10" id="content" style="width:100%; height:500px;" v-model="content" placeholder="내용을 입력하세요."></textarea><br>
      </div>
      <div class="row text-end mt-2">
        <div class="p-0">
          <button type="submit" class="m-1 btn content-font border btn-sm" @click="createArticle">작성</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000'


export default {
  name: 'ArticleCreateView',
  data() {
    return { 
      title: null,
      content: null,
      movies: JSON.parse(localStorage.getItem("movie_list")),
      movie: null,
      movie_title: null,
      show: false,
      search: null,
      filteredMovies: [],
    }
  },
  computed: {
    Movies() {
      return this.filteredMovies
    }
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('access_token')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    createArticle() {
      const config = this.getToken()

      const data = {
        title: this.title,
        movie: this.movie.id,
        content: this.content,
      }
      if (!this.title) {
        alert('제목을 입력해주세요')
        return
      } else if (!data.movie) {
        alert('영화를 입력해주세요')
        return
      } else if (!this.content) {
        alert('내용을 입력해주세요')
        return
      } 
      axios.post(`${SERVER_URL}/articles/`, data, config)
        .then(() => {
          this.$router.push({ name: 'ArticleHomeView' }).catch(()=>{})
        })
        .catch(err => {
          console.log(err)
        })
    },
    handleSearchInput() {
      if (this.search !== 0) {
        clearTimeout(this.debounce)
        this.debounce = setTimeout(() => {
          let filteredMovies = []
          filteredMovies = this.movies.filter(movie => movie.title.includes(this.search) | movie.original_title.includes(this.search))
          this.filteredMovies = filteredMovies
        }, 500)
      } else {
        clearTimeout(this.debounce)
        this.debounce = setTimeout(() => {
          this.filteredMovies = []
        }, 500)
      }
    },
    getMovie(Movie) {
      this.movie = Movie
      this.movie_title = this.movie.title
      console.log(this.movie)
      this.close()
    },
    open() {
      this.show = true
    },
    close() {
      this.show = false
    }
  }

}
</script>

<style>
#scollbar {
  height:800px; 
  overflow-x:hidden; 
  overflow-y:auto; 
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