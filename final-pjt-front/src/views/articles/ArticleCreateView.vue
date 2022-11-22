<template>
  <div>
    <h2>게시글 작성</h2>
    <div class="border p-4">
      <form @submit.prevent="createArticle">
        <div class="row">
          <input class="border-dark p-2 border-opacity-10" type="text" id="title" v-model.trim="title" placeholder="제목을 입력하세요."><br>
        </div>
        <div class="row mt-4">
          <textarea class="border-dark p-2 border-opacity-10" id="content" style="width:100%; height:500px;" v-model="content" placeholder="내용을 입력하세요."></textarea><br>
        </div>
        <div class="row text-end mt-2">
          <div class="p-0">
            <button type="submit" class="m-1 btn content-font border btn-sm">작성</button>
          </div>
        </div>
      </form>
    </div>
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
        .then(() => {
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