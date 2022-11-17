<template>
  <div>
    <div>
      <h2>Community</h2>
      <hr>
      <router-link :to="{ name: 'ArticleCreateView' }">[CREATE]</router-link>
      <ArticleList/>
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