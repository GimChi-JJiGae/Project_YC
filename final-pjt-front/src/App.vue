<template>
  <div id="app">
    <div class="container" style="min-width: 960px;">

    <nav>
      <span v-if="access_token">
        <router-link :to="{ name: 'HomeView' }">Home</router-link> |
        <router-link :to="{ name: 'ArticleHomeView' }">Community</router-link> |
        <router-link to="javascript:void(0)" @click.native="LogOut">logout</router-link> |
        <router-link :to="{ name: 'UsersView' }">Users</router-link> |
        <router-link :to="{ name: 'MyProfileView' }">My Profile</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'HomeView' }">Home</router-link> |
        <router-link :to="{ name: 'ArticleHomeView' }">Community</router-link> |
        <router-link :to="{ name: 'LogInView' }">Login</router-link> | 
        <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> | 
      </span>
    </nav>
    <router-view/>
  

    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'App',
  data() {
    return {
      isTrue: true,
      random_top_movie_list: [],
      popular_movie_list: [],
    }
  },
  computed: {
    access_token() {
      return this.$store.state.access_token
    },
    // username() {
    //   return jwt_decode(this.token).username
    // }
  },
  methods: {
    LogOut() {
      this.$store.dispatch('LogOut')
      this.$router.push({ name: 'HomeView' })

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
        }
      })
      
      .catch( (err) => {
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
      localStorage.setItem('random_top_movie_list', JSON.stringify(this.random_top_movie_list)) 
    },


    pick_popular_movies: function() {
      for (let i = 0; i<10; i++){
        this.popular_movie_list.push(this.$store.state.movies[i])
      }
      localStorage.setItem('popular_movie_list', JSON.stringify(this.popular_movie_list))
    }
  },
  created() {
    // console.log(this.$store.state.movies.length)
    if (this.$store.state.movies.length === 0) {
      
      this.getMovies()
      
      console.log('영화 데이터 생성됨')
    } else {
      console.log('영화 데이터 이미 있음')
    }
  },

 
}


</script>

<style>
#app {
  font-family: 'Do Hyeon', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
