<template>
  <div>
    <div class="bg-secondary bg-opacity-25 rounded-3 mx-3" style="height:600px;">
      <div class="test-center p-5" style="height:100%;">
        <div class="d-flex flex-column align-items-center" style="width: 100%; ">
          <div class="row" style="width: 100%; height: 150px;">
            <div class="col-2 p-0" style='height:100%; width: 150px; border-radius:50%; overflow:hidden; '>
              <img v-if="image" :src="image" alt="" style="width: 100%; height:100%; object-fit: cover;">
              <img v-else :src="basic" alt="" style="width: 100%; height:100%; object-fit: cover;">
            </div>
            <div class="col row justify-content-center align-items-center">
              <h5 class="text-start"><strong>{{ user.username }}님</strong></h5>
            </div>
            <div class="col-1"></div>
          </div>
          <div class="row " style="width: 100%; height: 70px;">
            <p class="my-1  text-start"><strong>이메일</strong></p>
            <p class="text-start">{{ user.email }}</p>
          </div>
          <div class="row " style="width: 100%; height: 70px;">
            <p class="mb-1  text-start"><strong>성별</strong></p>
            <p class="text-start">{{ this.sex }}</p>
          </div>
          <div class="row " style="width: 100%; height: 70px;">
            <p class="mb-1  text-start"><strong>연령대</strong></p>
            <p class="text-start ">{{ user.age }}</p>
          </div>
          <div class="row " style="width: 100%; height: 40px;">
            <p class="mb-1  text-start">
              <strong> 팔로잉 </strong><span>{{ this.followingsLength }}명</span>
            </p>
          </div>
          <div class="row " style="width: 100%; height: 40px;">
            <p class="mb-1  text-start">
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
        <div>                
          <!-- <p class="ms-3"><small>'좋아요'한 영화 수 : {{user.like_movies.length}}</small></p> -->
        </div>
      </div>

      <!-- <h2 >{{ user.username }}님이 좋아요 한 영화</h2>    
      <ul v-if="usersMovies">
        <MovieCard 
          :movies="usersMovies"
        />
      </ul> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"

// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',

  data() {
    return {
      user: [],
      me: [],
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
  },
  created() {
    this.getUserInfo()
    
  },
}
</script>

<style>

</style>