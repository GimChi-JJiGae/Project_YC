<template>
  <div>
    <h2>전체 유저 목록</h2>
    <hr>
    <div class="container">
      <div class="row">
        <div
         v-for="(user, idx) in users"
        :key="idx"
        >
          <div class="[ info-card ]">
            <div class="[ info-card-details ] animate">
              <div class="[ info-card-header ]">
                <h1 @click="moveToProfile(user)" style="cursor:pointer;">{{ user.username }}</h1>
                <h3>{{ user.email }}</h3>
              </div>
              <div class="[ info-card-detail ] st-font">
                <p>나이: {{user.age}}</p>
                <p>성별: {{user.sex}}</p>
                <p v-if="user.like_movies.length">좋아요 한 영화 개수: {{user.like_movies.length}}</p>
                <p v-else>{{user.username}}님은 아직 좋아요를 누른 영화가 없습니다.</p>
              </div>
            </div>
          </div>
          <hr>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UsersView',
  data() {
    return {
      users: [],
    }
  },
  methods: {
    getToken() {
      const token = localStorage.getItem('access_token')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    getUsers() {
      const config = this.getToken()
      axios.get(`${SERVER_URL}/accounts/users`, config)
        .then(res => {
          this.users = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    moveToProfile(user) {
      this.$router.push({ name: "ProfileView", params: { username: `${user.username}` }})
    }
  },
  created() {
    this.getUsers()
  }
}
</script>

<style>

</style>