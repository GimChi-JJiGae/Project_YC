<template>
  <div>
    <h2>게시글 작성</h2>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>

      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>

      <input type="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000'


export default {
  name: 'ArticleCreateView',
  data() {
    return { 
      title: null,
      content: null,
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
    createArticle() {
      const config = this.getToken()

      const data = {
        title: this.title,
        content: this.content,
      }
      if (!this.title) {
        alert('제목을 입력해주세요')
        return
      } else if (!this.content) {
        alert('내용을 입력해주세요')
        return
      } 
      axios.post(`${SERVER_URL}/articles/`, data, config)
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'ArticleHomeView' }).catch(()=>{})
        })
        .catch(err => {
          console.log(err)
        })
    }
  }

}
</script>

<style>

</style>