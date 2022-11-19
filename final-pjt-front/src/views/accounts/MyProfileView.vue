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
                    <div>
                      <button @click="updateUser">회원정보수정</button>
                      <button @click="deleteUser">회원 탈퇴</button>
                    </div>
                  <!-- 절취선 -->
                  <!-- 절취선 -->
                </div>            
          </div>                 
      </div>
    </div>
    <b-modal
      hide-footer
      v-model="show2"
      id="review-modal"
      size="sm"
      title="My Follwings"
      :header-bg-variant="headerBgVariant"
      :header-text-variant="headerTextVariant"
      :body-bg-variant="bodyBgVariant"
      :body-text-variant="bodyTextVariant"
      :footer-bg-variant="footerBgVariant"
      :footer-text-variant="footerTextVariant"
    >
      <hr>
      <section class="page-section" id="contact">
        <div class="container">
            <!-- Contact Section Heading-->
            <h2 class="st-font page-section-heading text-center text-uppercase text-white mb-0">Followings</h2>
            <!-- Contact Section Form-->
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    <!-- To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19.-->
                  <div class="control-group">
                      <div v-for="(follow, idx) in user.followings" :key="idx" style="cursor:pointer" class="content-font form-group floating-label-form-group controls mb-0 pb-2">
                          <MyFollower :follow="follow" />
                      </div>
                  </div>
                </div>
            </div>
        </div>
      </section>
      <div class="text-white st-font form-group"><button @click="close2" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">창 닫기</button></div>
    </b-modal>
    <!-- 절취선 -->
    <b-modal
      hide-footer
      v-model="show1"
      id="review-modal"
      size="sm"
      title="My Follwers"
      :header-bg-variant="headerBgVariant"
      :header-text-variant="headerTextVariant"
      :body-bg-variant="bodyBgVariant"
      :body-text-variant="bodyTextVariant"
      :footer-bg-variant="footerBgVariant"
      :footer-text-variant="footerTextVariant"
    >
      <hr>
      <section class="page-section" id="contact">
        <div class="container">
            <!-- Contact Section Heading-->
            <h2 class="st-font page-section-heading text-center text-uppercase text-white mb-0">Followers</h2>
            <!-- Contact Section Form-->
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    <!-- To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19.-->
                  <div class="control-group">
                      <div v-for="(follower, idx) in user.followers" :key="idx" style="cursor:pointer" class="content-font form-group floating-label-form-group controls mb-0 pb-2">
                          <MyFollower :follow="follower" />
                      </div>
                  </div>
                </div>
            </div>
        </div>
      </section>
      <div class="text-white st-font form-group"><button @click="close" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">창 닫기</button></div>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"

import MyFollower from "@/components/MyFollower"

// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MyProfileView',
  components: {
    MyFollower,
  },
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
    updateUser() {
      this.$router.push({ name: 'UpdateUserView', params: { username: `${this.user.username}` } })
    },
    deleteUser() {
      const config = this.getToken()
      axios.delete(`${SERVER_URL}/accounts/${this.user.username}/delete/`, config)
        .then(() => {
          this.$store.dispatch('LogOut')
          this.$router.push({ name: 'HomeView' })
        })
    }
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