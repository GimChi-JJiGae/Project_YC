<template>
  <div class="d-flex flex-column align-items-center" style="width:100%; min-width:770px;">
    <div class="row gap-3" style="height:700px; width:100%;">
      <div class="col-3 bg-secondary bg-opacity-25 rounded-3" style="min-width:240px;">
        <div class="mt-4">
          <div class='d-flex flex-column'>
            <div class="row" style="height:130px;">
              <div class="col-1"></div>
              <div class="col-3 p-0" style='height:100%; width:130px; border-radius:50%; overflow:hidden; '>
                <img v-if="image" :src="image" alt="" style="width: 100%; height:100%; object-fit: cover;">
                <img v-else :src="basic" alt="" style="width: 100%; height:100%; object-fit: cover;">
              </div>
              <div class="col row justify-content-center align-items-center">
                <h5 class="text-start"><strong>{{ user.username }}님</strong></h5>
              </div>
              <div class="col-1"></div>
            </div>
            <br>
            <div>
              <div class="row " style="width: 100%; height: 70px;">
                <p class="mb-1 ms-3 text-start"><strong>이메일</strong></p>
                <p class="text-start ms-3 mb-4">{{ user.email }}</p>
              </div>
              <div class="row " style="width: 100%; height: 70px;">
                <p class="mb-1 ms-3 text-start"><strong>성별</strong></p>
                <p class="text-start ms-3 mb-4">{{ this.sex }}</p>
              </div>
              <div class="row " style="width: 100%; height: 70px;">
                <p class="mb-1 ms-3 text-start"><strong>연령대</strong></p>
                <p class="text-start ms-3">{{ user.age }}</p>
              </div>
              <div class="row " style="width: 100%; height: 40px;">
                <p class="mb-1 ms-3 text-start">
                  <strong> 팔로잉 </strong><span>{{ this.followingsLength }}명</span>
                </p>
              </div>
              <div class="row " style="width: 100%; height: 40px;">
                <p class="mb-1 ms-3 text-start">
                  <strong> 팔로워 </strong><span>{{ this.followersLength }}명</span>
                </p>
              </div>
              <div v-if="me.username !== user.username" class="row" style="width: 100%;">
                <div class="text-start">
                  <button v-if="isFollowing" @click="follow" class="btn btn-secondary btn-block"><span class="fa fa-plus-circle"></span> UnFollow </button>
                  <button v-else @click="follow" class="btn btn-primary btn-block"><span class="fa fa-plus-circle"></span> Follow </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col bg-secondary bg-opacity-25 rounded-3 text-start d-flex flex-column p-3" style="min-width:420px; height:100%;">
        <div class="my-3" style="height:100%">
          <div class="" style="height:50%;">
            <h5 class='mb-0'><strong>{{user.username}}님이 좋아요 한 영화들</strong></h5>
            <div class=""><small>'좋아요'한 영화 수 : {{user.like_movies?.length}}</small></div>
            <div class="row  flex-nowrap" id="scollbar" style="height:75%">
              <span v-for="like_movie in like_movies" :key=like_movie.id style="width:190px;">
                <router-link :to="{name : 'MovieDetail', params : {movie_pk : like_movie.id }}">
                  <img :src='`https://image.tmdb.org/t/p/original/${like_movie.poster_path}`' alt="" style="height:230px; width:180px;" class="rounded-2">
                </router-link>
              </span>
            </div>
          </div>
          <div class="" style="height:50%;">
            <UserCommentList
            :comment_movies="comment_movies"
            :user="user"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"
import UserCommentList from "@/components/UserCommentList"

// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  components: {
    UserCommentList,
  },
  data() {
    return {
      user: {},
      me: [],
      comment_list: [],
      following: null,
      usersMovies: [],
      image: null,
      basic: null,
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
    getComment() {
      axios.get(`${SERVER_URL}/movies/comments/`)
        .then(res => {
          this.comment_list = res.data
        })
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
          if (this.me.followings.includes(this.user.id)) {
            this.following = true
          } else {
            this.following = false
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    getUserInfoSub: function () {
      const config = this.getToken()
      const username = this.$route.params.username
      const userItem = {
        username: username,
      }
      axios.post(`${SERVER_URL}/accounts/${username}/`, userItem, config)
        .then(res => {
          this.user = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    getUserInfo: function () {
      const config = this.getToken()
      this.getComment()
      const username = this.$route.params.username
      const userItem = {
        username: username,
      }
      axios.post(`${SERVER_URL}/accounts/${username}/`, userItem, config)
      .then( (res) => {
        this.user = res.data
        this.getMyName()

        // const item = this.user.like_movies
        // axios.post(`${SERVER_URL}/movies/${this.user.id}/like/`, item, config)
        // .then( (res) => {
        //   // console.log(res)
        //   this.usersMovies = res.data
        // })
        // .catch( (err) => {
        //   console.log(err)
        // })
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    follow: function () {
      const config = this.getToken()
      const item = {
        myId: this.me.id,
        userId: this.user.id,
      }
      axios.post(`${SERVER_URL}/accounts/follow/${this.me.id}/${this.user.id}/`, item, config)
      .then( () => {
        this.getMyName()
        this.getUserInfoSub()
      })
      .catch( (err) => {
        console.log(err)
      })
    },
  },
  computed: {
    like_movies() {
      const like_movie_list = []
      if (this.user.like_movies) {
          this.user.like_movies.forEach(like_movie => {
            const movie = JSON.parse(localStorage.getItem('movie_list'))[like_movie-1]
            like_movie_list.push(movie)
        });
      }
      return like_movie_list
    },
    isFollowing() {
      return this.following
    },
    followingsLength() {
      if (this.user.followings) {
        return this.user.followings.length
      } else {
        return 0
      }
    },
    followersLength() {
      if (this.user.followers) {
        return this.user.followers.length
      } else {
        return 0
      }
    },
    sex() {
      if (this.user.sex === 'male') {
        return '남성'
      } else {
        return '여성'
      }
    },
    comment_movies() {
      const comment_movie_list = []
      if (this.user.movie_comments) {
        this.user.movie_comments.forEach(comment_movie => {

          const movie = JSON.parse(localStorage.getItem('movie_list'))[this.comment_list[comment_movie-1].movie-1]
          comment_movie_list.push(movie)
        })
      }
      return comment_movie_list
    },
  },
  created() {
    this.getUserInfo()
    
  },
}
</script>

<style>

</style>