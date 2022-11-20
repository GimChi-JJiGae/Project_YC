<template>
  <div class="row">
    <div class="col-3 text-center">영화</div>
    <div class="col-4 text-center" style='cursor:pointer;' @click="moveToDetail" >{{article?.title}}</div>
    <div class="col-2 text-center" style='cursor:pointer;' @click="moveToProfile" >{{article?.username}}</div>
    <div class="col-1 text-center">{{like_numbers}}</div>
    <div class="col-1 text-center">{{hate_numbers}}</div>
    <div class="col-1 text-center">조회수</div>
  <hr>

  </div>
</template>

<script>
import axios from 'axios'
// import VueJwtDecode from 'vue-jwt-decode'
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
  data() {
    return {
      like_numbers: 0,
      hate_numbers: 0,
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    moveToDetail() {
      this.$router.push({ name: 'ArticleDetailView', params: { id: this.article.id } })
    },
    getToken() {
      const token = localStorage.getItem('access_token')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    getArticleDetail() {
      const config = this.getToken()
      axios.get(`${SERVER_URL}/articles/${this.article.id}/`, config)
        .then(res => {
          console.log(res)
          this.is_liked = res.data.is_liked
          this.like_numbers = res.data.likes_count
          this.is_hated = res.data.is_hated
          this.hate_numbers = res.data.hates_count
        })
        .catch(err => {
          console.log(err)
        })
    },
    moveToProfile() {
      this.$router.push({ name: "ProfileView", params: { username: `${this.article.username}` } })
    },
  }
}
</script>

<style>

</style>