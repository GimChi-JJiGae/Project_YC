<template>
  <div class="container test-center" style="height:600px; min-width:770px;">
    <div class="row gap-3" style="height:600px;">
      <div class="col-4 bg-secondary bg-opacity-25 rounded-3" style="min-width:240px;">
        <div class="mt-4">
          <div class='d-flex flex-column'>
            <div class="row" style="height:150px;">
              <div class="col-1"></div>
              <div class="col-3 p-0" style='height:100%; width:150px; border-radius:50%; overflow:hidden; '>
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
              <div>
                <p class="mb-1 ms-3 text-start"><strong>이메일</strong></p>
                <p class="text-start ms-3 mb-4">{{ user.email }}</p>
              </div>
              <div>
                <p class="mb-1 ms-3 text-start"><strong>성별</strong></p>
                <p class="text-start ms-3 mb-4">{{ this.sex }}</p>
              </div>
              <div>
                <p class="mb-1 ms-3 text-start"><strong>연령대</strong></p>
                <p class="text-start ms-3">{{ user.age }}</p>
              </div>
              <div>
                <p class="mb-1 ms-3 text-start">
                  <a @click="open2" class="content-font text-decoration-none text-black" style="cursor:pointer;"><strong> 팔로잉 </strong><span>{{ this.followingsLength }}명</span></a>
                </p>
              </div>
              <div>
                <p class="mb-1 ms-3 text-start">
                  <a @click="open1" class="content-font text-decoration-none text-black" style="cursor:pointer;"><strong> 팔로워 </strong><span>{{ this.followersLength }}명</span></a>
                </p>
              </div>
            </div>
          </div>
          <div class=''>
            <button @click="updateUser" class="m-1 btn content-font">회원정보수정</button>
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
          hide-header-close
        >
          <section class="page-section my-2" id="contact">
            <div class="container">
                <!-- Contact Section Heading-->
                <!-- <h5 class="st-font page-section-heading text-center text-uppercase text-white mb-0">Followings</h5> -->
                <!-- Contact Section Form-->
                <br>
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
          <!-- <div class="text-white st-font form-group"><button @click="close2" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">창 닫기</button></div> -->
        </b-modal>
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
          hide-header-close
        >
          <section class="page-section" id="contact">
            <div class="container">
                <!-- Contact Section Heading-->
                <!-- <h5 class="st-font page-section-heading text-center text-uppercase text-white mb-0">Followers</h5> -->
                <!-- Contact Section Form-->
                <br>
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
          <!-- <div class="text-white st-font form-group"><button @click="close" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">창 닫기</button></div> -->
        </b-modal>
      </div>

      <div class="col-7 bg-secondary bg-opacity-25 rounded-3 text-start d-flex flex-column" style="min-width:420px;">
        <div class="m-3" style="height:100%">

          <div class="" style="height:50%;">
            <h5><strong>내가 좋아요 한 영화들</strong></h5>
          </div>
          <div class="" style="height:50%;">
            <h5><strong>추천 영화 목록</strong></h5>
          </div>
          
        </div>
      </div>

    </div>

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
      image: null,
      basic: null,
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
    getImage(url) {
      this.image = SERVER_URL + url
    },
    getMyName: function () {
      const config = this.getToken()

      const hash = localStorage.getItem('access_token')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
        .then( (res) => {
          this.user = res.data
          if (this.user.image) {
            this.getImage(this.user.image)
          } else {
            const url = '/media/basic.png'
            this.getImage(url)
          }

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
    sex() {
      if (this.user.sex === 'male') {
        return '남성'
      } else {
        return '여성'
      }
    }
  },
}
</script>

<style>

</style>