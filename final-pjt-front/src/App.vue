<template>
  <div id="app" class="m-0">
    <div style="position:fixed; bottom:5px; right:5px;">
      <a href="#app">TOP</a>
    </div>
    <div class="container">
      <b-navbar type="light" class="d-flex justify-content-between pb-0">
        <b-navbar-nav class="d-flex align-items-center">
          <b-nav-item :to="{ name: 'HomeView' }"><img src="@/assets/logo5.png" alt="" style="width:150px;"></b-nav-item>
  
          <b-nav-item :to="{ name: 'ArticleHomeView' }">Community</b-nav-item>
          <b-nav-item :to="{ name: 'GenreMovies' }">Genres</b-nav-item>
          <!-- Navbar dropdowns -->
        </b-navbar-nav>
        
        <b-navbar-nav class="d-flex align-items-center">
          <b-nav-item >
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
                  <ul class="list-group list-group-flush" style="width:100%;">
                    <li
                      v-for="(movie, idx) in Movies"
                      :key="idx"
                      class="list-group-item"
                      style="height: 100%; cursor:pointer;"
                    >
                      <div class="row" @click="moveToDetail(movie)">
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
          </b-nav-item>
          <b-nav-item-dropdown text="User" right >
            <span v-if="access_token">
              <b-dropdown-item to="javascript:void(0)" @click.native="LogOut">로그아웃</b-dropdown-item>
              <b-dropdown-item :to="{ name: 'MyProfileView' }">내 프로필</b-dropdown-item>
              <b-dropdown-item :to="{ name: 'UpdateUserView', params: { username: `${user?.username}` } }">회원정보수정</b-dropdown-item>
              <b-dropdown-item :to="{ name: 'UsersView' }">유저 찾기</b-dropdown-item>
            </span>
            <span v-else>
              <b-dropdown-item opdown-item :to="{ name: 'LogInView' }">로그인</b-dropdown-item>
              <b-dropdown-item opdown-item :to="{ name: 'SignUpView' }">회원가입</b-dropdown-item>
            </span>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-navbar>
    </div>
    <hr>
    <div class="container" style="min-width: 960px;">
      <router-view/>
    </div>
    <hr>
    <div class="container">
      <div class="row justify-content-center align-items-center" style="height:30px;">
        <div class="row">
          <div class="col text-end">
            <img src="@/assets/logo5.png" alt="">
          </div>
          <div class="col text-start">
            <div class="text-start">
              개발자 : 윤도현, 최형규
            </div>
            <div class="text-start">
              문의 사항 : 010-8565-5971
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import VueJwtDecode from "vue-jwt-decode"

// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',
  data() {
    return {
      isTrue: true,
      random_top_movie_list: [],
      popular_movie_list: [],
      high_vote_movie_list: [],
      user: null,
      me: null,
      search: null,
      filteredMovies: [],
      show: false,
      movies: JSON.parse(localStorage.getItem("movie_list")),
    }
  },
  computed: {
    Movies() {
      return this.filteredMovies
    },
    access_token() {
      return this.$store.state.access_token
    },
    // username() {
    //   return jwt_decode(this.token).username
    // }
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
    getImage(url) {
      this.image = SERVER_URL + url
    },
    getMyName: function() {
      const config = this.getToken()

      const hash = localStorage.getItem('access_token')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
        .then(res => {
          this.me = res.data
          if (this.user.image) {
            this.getImage(this.user.image)
          } else {
            const url = '/media/basic.png'
            this.getImage(url)
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    LogOut() {
      this.$store.dispatch('LogOut')
      this.$router.push({ name: 'HomeView' })
    },
    updateUser() {
      this.getMyName()
      this.$router.push({ name: 'UpdateUserView', params: { username: `${this.user.username}` } })
    },
    /*
    getMovies: function () {
      axios.get(`http://127.0.0.1:8000/movies/`)
      .then( (res) => {
        if (this.$store.state.movies.length === 0) {
          this.$store.state.movies = res.data
          console.log(this.$store.state.movies)
          console.log("check")
        }
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    getRelatedMovies: function() {
      axios.get(`https://api.themoviedb.org/3/movie/${this.$store.state.movies[0].original_id}/recommendations?api_key=5d2592924ae354925561438e12ee8888&language=ko-KR&page=1`)
    .then( (res) => {
      console.log(res.data)
    })
    .catch( (err) => {
      console.log(err)
    })
    }
    */
    getMovies: function () {
      if (this.isLogin) {
        // this.$store.dispatch('getMovies')
      } else {
        // 로그인 안했을 때 페이지 보여주기
      }
      axios.get(`http://127.0.0.1:8000/movies/`)
      
      .then( (res) => {
        if (this.$store.state.movies.length === 0) {
          this.$store.state.movies = res.data         // 다른곳에 잠시 활용하기 위해 vuex에도 저장해두자
          
          localStorage.setItem('movie_list',JSON.stringify(this.$store.state.movies) )
          this.pick_random_top_movies()
          this.pick_popular_movies()
          this.pick_high_vote_movies()
        }
      })
      
      .catch( (err) => {
        console.log(err)
      })
    },
    getGenres: function() {
      axios.get(`http://127.0.0.1:8000/movies/genres/`)
      .then( (res) => {
        localStorage.setItem('genres', JSON.stringify(res.data))
      })
    
      .catch((err) => {
        console.log(err)
      })
    },
    pick_random_top_movies: function () {   // 여기서 영화 목록 열개를 골라서 잠시 vuex에 저장하고 포스터 패스가 존재하는지 확인한 후 로컬 스토리지에 저장한다.
      
      for (let i = 0; i<10; i++) {
        let number = _.random(0, 979)

        if (this.$store.state.movies[number].poster_path){ // 포스터 패스가 없을 경우는 다른걸 찾는다
          this.random_top_movie_list.push(this.$store.state.movies[number])
        }
        else {
          i = i - 1
        }
      }
      localStorage.removeItem('random_top_movie_list')
      localStorage.setItem('random_top_movie_list', JSON.stringify(this.random_top_movie_list)) 
    },
    


    pick_popular_movies: function() {
      for (let i = 0; i<10; i++){
        this.popular_movie_list.push(this.$store.state.movies[i])
      }
      localStorage.setItem('popular_movie_list', JSON.stringify(this.popular_movie_list))
    },

    pick_high_vote_movies: function() {
      let temp = this.$store.state.movies.slice()
      temp.sort(function(a, b) { // 내림차순
        return a.vote_average > b.vote_average ? -1 : a.vote_average < b.vote_average? 1 : 0;
    // 형돈, 재석, 명수, 광희
      
      });
      for (let i = 0; i<10; i++){
        this.high_vote_movie_list.push(temp[i])
      }
      localStorage.setItem('high_vote_movie_list', JSON.stringify(this.high_vote_movie_list))
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
    open() {
      this.show = true
    },
    close() {
      this.show = false
    },
    moveToDetail(movie) {
      this.$router.push({ name: 'MovieDetail', params: { 'movie_pk': movie.id }})
      location.reload()
    }
  },
  created() {
    this.getGenres()
    if (this.$store.state.movies.length === 0) {
      this.getMovies()
    } else {
      this.pick_random_top_movies()
      this.pick_popular_movies()
      this.pick_high_vote_movies()
    }
  },

 
}


</script>

<style scoped>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css');
#app *{
  font-family: 'Pretendard Variable';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  /* font-weight: bold; */
  color: grey;
  text-decoration: none;
}

nav a.router-link-exact-active {
  /* color: #42b983; */
  font-weight: 600;
}
</style>
