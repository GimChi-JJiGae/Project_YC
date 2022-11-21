<template>
  <div class="container border p-4" style="min-width: 960px;">
    <div class="row">
      <div class="col text-start fw-bold fs-2">{{ article?.title }}</div>
      <div class="col-2 row justify-content-center align-items-center ">
        <div class="col p-0 text-end" style="cursor:pointer;"  @click="likeArticle(article)" >
          <font-awesome-icon icon="fa-solid fa-thumbs-up" v-if="is_liked"/>
          <font-awesome-icon icon="fa-regular fa-thumbs-up" v-else/> {{ like_numbers }}
        </div>
        <div class="col-1">|</div>
        <div class="col p-0 text-start" style="cursor:pointer;" @click="hateArticle(article)">
          <font-awesome-icon icon="fa-solid fa-thumbs-down" v-if="is_hated"/>
          <font-awesome-icon icon="fa-regular fa-thumbs-down" v-else/> {{ hate_numbers }}
        </div>
      </div>
    </div>
    <hr class="m-0">
    <div class="row">
      <div class="col text-start m-1"><span @click="moveToProfile(article.user, article.username)" style="cursor:pointer;"><small>{{ article?.username }}님</small></span></div>
      <div class="col-8">
      </div>
      <div class="col"><small>{{ create_at }}</small></div>
    </div>
    <div class="row text-start my-4">
      <div class="">{{ article?.content }}</div>
    </div>
    <div class="row flex-row-reverse" v-if="user?.username === article?.username">
      <div class="col-2 row justify-content-start">
        <div class="col p-0 text-end">
          <button @click="moveToUpdate(article)" class="m-1 btn content-font border btn-sm">수정</button>
        </div>
        <div class="col p-0 text-start">
          <button @click="deleteArticle(article)" class="m-1 btn content-font border btn-sm">삭제</button>
        </div>
      </div>
    </div>
    <hr>
    <ul class="list-group list-group-flush">
      <li class="list-group-item" v-for="(comment, idx) in commentsList" :key="idx">
        <div class="row text-start align-items-center">
          <div class="col-2"><span style="cursor:pointer;" @click="moveToProfile(comment.user, comment.username)"><strong>{{ comment.username }}</strong></span></div>
          <div class="col-8">{{ comment.content }}</div>
          <div class="col-2"><small>{{ comment_create[idx] }}</small></div>
        </div>
        <div class="text-end" v-if="user.username === comment.username">
          <button class="m-1 btn content-font border btn-sm" @click="deleteComment(comment)">삭제</button>
        </div>
      </li>
    </ul>
    <div class="row">
      <div class="col">
        <textarea name="createComment" id="createComment" style="width: 100%; height: 6.25em;" placeholder="댓글을 작성하세요" v-model="comment_content"></textarea>
      </div>
    </div>
    <div class="row">
      <div class="col text-end">
        <button class="m-1 btn content-font border btn-sm" type="submit" @click="createComment">댓글 작성</button>
      </div>
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
    create_at() {
      let js_date = new Date(this.article?.created_at)
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
    update_at() {
      let js_date = new Date(this.article?.updated_at)
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
    comment_create() {
      let comments_created = []
      for (let i = 0; i < this.commentsList.length; i++) {
        let js_date = new Date(this.commentsList[i]?.created_at)
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
        comments_created.push(year + '-' + month + '-' + day + '  ' + hour + ':' + min)
      }
      return comments_created
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
          this.is_liked = !res.data.is_liked
          this.like_numbers = res.data.likes_count
          this.is_hated = !res.data.is_hated
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
      } else {	4
        alert("본인이 작성한 글만 수정 가능합니다.")
      }
    },
    moveToProfile(user, username) {
      console.log(username)
      this.$router.push({ name: "ProfileView", params: { username: `${username}` } })
    },
    likeArticle(article) {
      const config = this.getToken()
      this.is_liked = !this.is_liked
      axios.post(`${SERVER_URL}/articles/${article.id}/likes/`, this.is_Like, config)
        .then(res => {
          this.is_liked = res.data.is_liked
          this.like_numbers = res.data.likes_count
          // this.getArticleDetail()
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
          // this.getArticleDetail()
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