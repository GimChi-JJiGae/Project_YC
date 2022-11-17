<template>
  <div class="container">
    <h1 class="title-font" style="margin-bottom:40px">My Profile</h1>
    <div class="containter" style="margin-bottom:30px">
      <div class="row">
          <div class="well profile containerSpecial" style="position:relative;">
                <div class="col-sm-12">
                    <div class="col-xs-6 col-sm-8 center" style="margin-bottom:20px">
                        <h2 class="title-font" style="margin-bottom: 10px"><strong>{{ user.username }}님의 프로필</strong></h2>
                        <div><button @click="open2" class="m-1 btn content-font">Following <span>{{ this.followingsLength }}명</span></button> <button @click="open1" class="m-1 btn content-font">Follower <span>{{ this.followersLength }}명</span></button></div>
                        <p class="content-font" style="font-size: 20px"><strong>Email: </strong> {{ user.email }} </p>
                        <p class="content-font" style="font-size: 20px"><strong>Info: </strong>
                            <span class="tags" style="margin-right:5px">{{user.age}}</span> 
                            <span class="tags" style="margin-right:5px">{{user.sex}}</span>
                        </p>
                    </div>
                    <br>             
                    <div class="col-xs-12 col-sm-4 text-center">
                        <figure>
                            <!-- <img src="@/assets/미니언즈.jpg" alt="" class="img-circle img-responsive"> -->
                        </figure>
                    </div>
                  <!-- 절취선 -->
                  <!-- 절취선 -->
                </div>            
          </div>                 
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"

// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MyProfileView',
  data() {
    return {
      user: [],
      users: [],
      myFollowings: [],
      myMovies: [],
      show1: false,
      show2: false,
      variants: ["light", "dark"],
    headerBgVariant: "dark",
    headerTextVariant: "white",
    bodyBgVariant: "dark",
    bodyTextVariant: "white",
    footerBgVariant: "danger",
    footerTextVariant: "dark",
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
    getMyName: function () {
      const config = this.getToken()

      const hash = localStorage.getItem('access_token')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
      .then( (res) => {
        this.user = res.data

        // const item = this.user.like_movies
        // axios.post(`${SERVER_URL}/movies/${this.user.id}/like/`, item, config)
        // .then( (res) => {
        //   // console.log(res)
        //   this.myMovies = res.data
        // })
        // .catch( (err) => {
        //   console.log(err)
        // })

      })
      .catch( (err) => {
        console.log(err)
      })
    },
    open1: function () {
      this.show1 = true
    },
    open2: function () {
      this.show2 = true
    },
    close: function () {
      this.show1 = false
    },
    close2: function () {
      this.show2 = false
    },
  },
  created() {
    this.getMyName()
  },
  computed: {
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
  },
}
</script>

<style>

</style>