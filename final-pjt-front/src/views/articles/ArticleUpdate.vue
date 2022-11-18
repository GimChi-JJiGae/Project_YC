<template>
  <div>
    <h2>Article Update</h2>
    <div>
      <label>Title</label>
      <input type="text" v-model="article.title" placeholder="Title" required="required" data-validation-required-message="Please enter your title">
      <p class="help-block text-danger"></p>
    </div>
    <div>
      <label>Content</label>
      <textarea v-model.trim="article.content" class="form-control" id="content" rows="5" placeholder="Content" required="required" data-validation-required-message="Please enter a message."></textarea>
      <p class="help-block text-danger"></p>
    </div>
    <div>
      <button @click="articleUpdate(article)" type="submit">Update</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleUpdate',
  props: {
    article_pk: Number,
  },
  data() {
    return {
      article: [],
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
    getArticle() {
      const config = this.getToken()
      const article_pk = this.$route.params.id
      axios.get(`${SERVER_URL}/articles/${article_pk}`, config)
        .then(res => {
          this.article = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    articleUpdate(article) {
      const article_pk = this.$route.params.id
      const config = this.getToken()
      const articleItem = {
        title: article.title,
        content: article.content
      }
      axios.put(`${SERVER_URL}/articles/${article_pk}/`, articleItem, config)
        .then(res => {
          if (res.data.message) {
            alert("본인이 작성한 글만 수정 가능합니다.")
          } else {
            console.log(article.id)
            this.$router.push({ name: 'ArticleDetailView', params: { id: `${article.id}`} })
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
    this.getArticle()
  }
  
}
</script>

<style>

</style>