<template>
  <div>
    <h2>{{ user.username }}님의 Profile</h2>
    <p class="content-font" style="font-size: 20px"><strong>Email: </strong> {{ user.email }} </p>
    <p class="content-font" style="font-size: 20px"><strong>Info: </strong>
      <span class="tags" style="margin-right:5px">{{user.age}}</span> 
      <span class="tags" style="margin-right:5px">{{user.sex}}</span>
    </p>
    <!-- <p v-if="isFollowing" class="st-font">{{ user.username }}님을 팔로우 중 입니다.</p> -->
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"

// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  props: {
    user_pk: Number,
    username: String,
  },
  data() {
    return {
      user: [],
      me: [],
      following: null,
      usersMovies: [],
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
    getMyName: function() {
      const config = this.getToken()

      const hash = localStorage.getItem('access_token')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
        .then(res => {
          this.me = res.data
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
      const user_pk = this.$route.params.user_pk
      const username = this.$route.params.username
      const userItem = {
        user_pk: user_pk,
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
      const user_pk = this.$route.params.user_pk
      const username = this.$route.params.username
      const userItem = {
        user_pk: user_pk,
        username: username,
      }
      axios.post(`${SERVER_URL}/accounts/${username}/`, userItem, config)
      .then( (res) => {
        // console.log(res.data)
        // console.log(res)
        this.user = res.data
        const item = this.user.like_movies

        axios.post(`${SERVER_URL}/movies/${this.user.id}/like/`, item, config)
        .then( (res) => {
          // console.log(res)
          this.usersMovies = res.data
        })
        .catch( (err) => {
          console.log(err)
        })
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
        // console.log(res)
        // console.log(this.me)
        this.getMyName()
        this.getUserInfoSub()
      })
      .catch( (err) => {
        console.log(err)
      })
    },
  },
  created() {
    this.getUserInfoSub()
  },
}
</script>

<style>

</style>