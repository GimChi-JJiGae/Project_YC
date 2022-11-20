<template>
  <div>
    <h2>Community</h2>
    <div class="">
      <div class="row">
        <div class="col-1">
        </div>
        <div class="col-10">
          <ArticleList/>
        </div>
        <div class="col-1">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <button class="m-1 btn content-font border">
            <router-link :to="{ name: 'ArticleCreateView' }" class="text-decoration-none text-black">게시글 생성</router-link>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ArticleList from '@/views/articles/ArticleList'
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleHomeView',
  components: {
    ArticleList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getArticles()
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
    getArticles() {
      const config = this.getToken()
      if (this.isLogin === true) {
        axios.get(`${SERVER_URL}/articles/`, config)
        .then(res => {
          this.$store.dispatch('getArticles', res.data)
        })
        .catch(err => {
          console.log(err)
          this.$store.dispatch('getArticles', [])
        })
      } else {
        alert('로그인이 필요한 서비스입니다.')
        this.$router.push({ name: 'LogInView' })
      }
    },
  }
}
</script>

<style>

</style>