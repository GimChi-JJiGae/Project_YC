<template>
  <div class="container">
    <div class="row">
      <div class="col-10"><h4>{{ article?.title }}</h4></div>
      <div class="col-1">좋아 {{ like_numbers }}</div>
      <div class="col-1">싫어 {{ hate_numbers }}</div>
    </div>
    <div class="row">
      <div class="col" @click="moveToProfile(article.user, article.username)" style="cursor:pointer;">작성자 : {{ article?.username }}</div>
      <div v-if="article.created_at === article.updated_at" class="col">작성시간 : {{ created }}</div>
      <div v-else class="col">수정시간 : {{ updated }}</div>
      <div class="col-1">
        <button @click="deleteArticle(article)">삭제</button>
      </div>
      <div class="col-1">
        <button @click="moveToUpdate(article)">수정</button>
      </div>
    </div>
    <div class="row">
      <div class="">{{ article?.content }}</div>
    </div>
    <hr>
    <div>
      좋아요 : <button @click="likeArticle(article)">{{ is_Like }}</button>
      싫어요 : <button @click="hateArticle(article)">{{ is_Hate }}</button>
    </div>
    <hr>
    <div>
      <div class="container" v-for="(comment, idx) in commentsList" :key="idx">
        <div>{{ comment.content }}</div>
        <span>{{ comment.created_at }}   </span>
        <span style="cursor:pointer;" @click="moveToProfile(comment.user, comment.username)">{{ comment.username }}    </span>
        <div>
          <button @click="deleteComment(comment)">댓글 삭제</button>
        </div>

      </div>
      <textarea name="createComment" id="createComment" cols="50" rows="2" placeholder="댓글을 작성하세요" v-model="comment_content"></textarea>
      <button type="submit" @click="createComment">댓글 작성</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from 'vue-jwt-decode'
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetailView',
  data() {
    return {
      article: null,
      comment_content: null,
      comments: [],
      user: [],
      is_liked: null,
      like_numbers: 0,
      is_hated: null,
      hate_numbers: 0,
    }
  },
  computed: {
    commentsList() {
      return this.comments
    },
    is_Like() {
      return this.is_liked ? '좋아요' : '좋아요 취소'
    },
    is_Hate() {
      return this.is_hated ? '싫어요' : '싫어요 취소'
    },
    created() {
      let js_date = new Date(this.article.created_at)
      const year = js_date.getFullYear()
      let month = js_date.getMonth() + 1
      let day = js_date.getDate()
      let hour = js_date.getHours()
      let min = js_date.getMinutes()
      if (min < 10) {
        min = '0' + min;
      }
      if (hour < 10) {
        hour = '0' + hour;
      }
      if(month < 10){
        month = '0' + month;
      }
      if(day < 10){
        day = '0' + day;
      }
      return year + '-' + month + '-' + day + '  ' + hour + ':' + min
    },
    updated() {
      let js_date = new Date(this.article.updated_at)
      const year = js_date.getFullYear()
      let month = js_date.getMonth() + 1
      let day = js_date.getDate()
      let hour = js_date.getHours()
      let min = js_date.getMinutes()
      if (min < 10) {
        min = '0' + min;
      }
      if (hour < 10) {
        hour = '0' + hour;
      }
      if (month < 10) {
        month = '0' + month;
      }
      if (day < 10) {
        day = '0' + day;
      }
      return year + '-' + month + '-' + day + '  ' + hour + ':' + min
    },

  },
  created() {
    this.getArticleDetail()
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
    getArticleDetail() {
      const config = this.getToken()
      axios.get(`${SERVER_URL}/articles/${this.$route.params.id}/`, config)
        .then(res => {
          this.article = res.data.article
          this.is_liked = res.data.is_liked
          this.like_numbers = res.data.likes_count
          this.is_hated = res.data.is_hated
          this.hate_numbers = res.data.hates_count
          this.getComments()
          this.getMyName()
        })
        .catch(err => {
          console.log(err)
        })
    },
    getMyName() {
      const config = this.getToken()
      const hash = localStorage.getItem('access_token')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
        .then(res => {
          this.user = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    getComments() {
      const config = this.getToken()
      const article_pk = this.article.id
      axios.get(`${SERVER_URL}/articles/comments/${article_pk}`, config)
      .then(res => {
          this.comments = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    createComment() {
      const article_pk = this.article.id
      const config = this.getToken()
      const commentItem = {
        content: this.comment_content
      }
      if (commentItem.content) {
        axios.post(`${SERVER_URL}/articles/${article_pk}/comments/`, commentItem, config)
          .then(() => {
            this.getComments()
            this.comment_content = null
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
    deleteComment(comment) {
      const config = this.getToken()
      if (this.user.username === comment.username) {
        axios.delete(`${SERVER_URL}/articles/comments/detail/${comment.id}/`, config)
          .then(() => {
            this.getComments()
          })
          .catch(err => {
            console.log(err)
          })
      } else {
        alert("본인이 작성한 댓글만 삭제 가능합니다")
      }
    },
    deleteArticle(article) {
      const config = this.getToken()
      if (this.user.username === article.username) {
        axios.delete(`${SERVER_URL}/articles/${article.id}`, config)
        .then(() => {
            this.$router.push({ name: 'ArticleHomeView' })
        })
        .catch(err => {
          console.log(err)
        })
      } else {
          alert("본인이 작성한 글만 삭제 가능합니다.")
      }
    },
    // updateToggle() {
    //   let updateToggle = document.querySelector('.updateToggle')
    //   updateToggle.classList.toggle("active")
    // },
    // updateComment() {
      
    // },
    moveToUpdate(article) {
      if (this.user.username === article.username) {
        this.$router.push({ name: 'ArticleUpdate', params: { id: `${article.id}` } })
      } else {
        alert("본인이 작성한 글만 수정 가능합니다.")
      }
    },
    moveToProfile(user, username) {
      console.log(username)
      this.$router.push({ name: "ProfileView", params: { username: `${username}` } })
    },
    likeArticle(article) {
      const config = this.getToken()
      axios.post(`${SERVER_URL}/articles/${article.id}/likes/`, this.is_Like, config)
        .then(res => {
          this.is_liked = res.data.is_liked
          this.like_numbers = res.data.likes_count
          this.getArticleDetail()
        })
        .catch(err => {
          console.log(err)
        })
    },
    hateArticle(article) {
      const config = this.getToken()
      axios.post(`${SERVER_URL}/articles/${article.id}/hates/`, this.is_hate, config)
        .then(res => {
          this.is_hated = res.data.is_hated
          this.hate_numbers = res.data.hates_count
          this.getArticleDetail()
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
}
</script>

<style>

</style>