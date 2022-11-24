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
                  <a @click="open2" class="content-font text-decoration-none text-black" style="cursor:pointer;"><strong> 팔로잉 </strong><span>{{ this.followingsLength }}명</span></a>
                </p>
              </div>
              <div class="row " style="width: 100%; height: 40px;">
                <p class="mb-1 ms-3 text-start">
                  <a @click="open1" class="content-font text-decoration-none text-black" style="cursor:pointer;"><strong> 팔로워 </strong><span>{{ this.followersLength }}명</span></a>
                </p>
              </div>
            </div>
          </div>
          <div class="mt-4" style="height: 70px;">
            <button @click="updateUser" class="m-1 btn content-font">회원정보수정</button>
          </div>
        </div>
        <b-modal
          hide-footer
          v-model="show2"
          id="review-modal"
          size="sm"
          title="My Follwings"
          hide-header-close
        >
          <section class="page-section my-2" id="contact">
            <div class="container">
              <!-- Contact Section Heading-->
              <!-- <h5 class="st-font page-section-heading text-center text-uppercase text-white mb-0">Followings</h5> -->
              <!-- Contact Section Form-->
              <br>
              <div class="row">
                <div class="col mx-auto">
                    <!-- To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19.-->
                  <div class="control-group">
                      <div v-for="(follow, idx) in user.followings" :key="idx" style="cursor:pointer" class="content-font form-group floating-label-form-group controls mb-0 pb-2">
                          <MyFollower :follow="follow" />
                      </div>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <button @click="close2" class="m-1 btn content-font border btn-sm" type="submit">닫기</button>
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
 
          hide-header-close
        >
          <section class="page-section" id="contact">
            <div class="container">
                <!-- Contact Section Heading-->
                <!-- <h5 class="st-font page-section-heading text-center text-uppercase text-white mb-0">Followers</h5> -->
                <!-- Contact Section Form-->
              <br>
              <div class="row">
                <div class="col mx-auto">
                    <!-- To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19.-->
                  <div class="control-group">
                      <div v-for="(follower, idx) in user.followers" :key="idx" style="cursor:pointer" class="content-font form-group floating-label-form-group controls mb-0 pb-2">
                          <MyFollower :follow="follower" />
                      </div>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <button @click="close1" class="m-1 btn content-font border btn-sm" type="submit">닫기</button>
            </div>
          </section>
          <!-- <div class="text-white st-font form-group"><button @click="close" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">창 닫기</button></div> -->
        </b-modal>
      </div>

      <div class="col bg-secondary bg-opacity-25 rounded-3 text-start d-flex flex-column p-3" style="min-width:420px; height:100%;">
        <div class="my-3" style="height:100%">
          <div class="" style="height:50%;">
            <h5 class='mb-0'><strong>내가 좋아요 한 영화들</strong></h5>
            <span class=""><small>'좋아요'한 영화 수 : {{user.like_movies?.length}}</small></span>
            <div class="row  flex-nowrap" id="scollbar">
              <span v-for="like_movie in like_movies" :key=like_movie.id style="width:190px;">
                <router-link :to="{name : 'MovieDetail', params : {movie_pk : like_movie.id }}">
                  <img :src='`https://image.tmdb.org/t/p/original/${like_movie.poster_path}`' alt="" style="height:230px; width:180px;" class="rounded-2">
                </router-link>
              </span>
            </div>
          </div>
          <div class="" style="height:50%;">
            <h5><strong>추천 영화 목록</strong></h5>
          </div>
        </div>
      </div>
    </div>
    <div class="row" style="width:100%">
      <DoughnutChart
        :movies="like_movies"
        :chartData="chartData"
      />
    </div>
    <RecommendByAge
      :age_to_recommend="age_to_recommend"
      :like_movies="like_movies"
      
    />
    <ReconmmendBySex
      :sex_to_recommend="sex_to_recommend"
      :like_movies="like_movies"
    />
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"

import MyFollower from "@/components/MyFollower"
import DoughnutChart from "@/components/DoughnutChart"
import RecommendByAge from '@/components/RecommendByAge.vue'
import ReconmmendBySex from '@/components/ReconmmendBySex.vue'
// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MyProfileView',
  components: {
    MyFollower,
    DoughnutChart,
    RecommendByAge,
    ReconmmendBySex,
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
      lawData : {},
      age_to_recommend : null,
      sex_to_recommend : null,
      chartData: {
        labels: [],
        datasets: [
          { // backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
            // data: [40, 20, 80, 10]
            backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16', '#3dda4a', '#daca3d',
                              '#e65d5d', '#daca3d', '#daca3d', '#daca3d', '#daca3d', '#daca3d', 
                              '#daca3d', '#daca3d', '#daca3d', '#daca3d', '#daca3d', '#daca3d', 
                              '#daca3d',],
            data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
          }
        ]
      },
      
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
          
          this.age_to_recommend = res.data['age']
          this.sex_to_recommend = res.data['sex']
          console.log(this.age_to_recommend)
          if (this.user.image) {
            this.getImage(this.user.image)
          } else {
            const url = '/media/basic.png'
            this.getImage(url)
          }
          this.getData()
          console.log(this.chartData)
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
    close1: function () {
      this.show1 = false
    },
    close2: function () {
      this.show2 = false
    },
    updateUser() {
      this.$router.push({ name: 'UpdateUserView', params: { username: `${this.user.username}` } })
    },
    getData() {
      const genres = JSON.parse(localStorage.getItem('genres'))
      for (const gen of genres) {
        this.lawData[gen['name']] = 0
        this.chartData.labels.push(gen['name'])
      }
      for (const movie of this.like_movies) {
        for (const genre of movie.genres) {
          for (const gen of genres) {
            if (gen['id'] === genre) {
              this.lawData[gen['name']] += 1
            }
          }
        }
      }
      for (const com in this.lawData) {
        if (this.lawData[com]) {
          this.chartData.datasets[0]['data'][this.chartData.labels.indexOf(com)] = this.lawData[com]
        } else {
          this.chartData.datasets[0]['data'][this.chartData.labels.indexOf(com)] = 0
        }
      }
    },
  },
  created() {
    this.getMyName()
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
}
</script>

<style>
#scollbar {
  overflow: auto;
  width: 100%;
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