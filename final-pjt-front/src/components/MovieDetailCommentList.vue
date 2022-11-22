<template>
  <div>
    <hr>
    여기에 댓글목록 생성됨
    <div class="row">
      <div class="col-2">유저</div>
      <div class="col-8">내용</div>
      <div class="col-1"><font-awesome-icon icon="fa-regular fa-thumbs-up"/></div>
      <div class="col-1"><font-awesome-icon icon="fa-regular fa-thumbs-down"/></div>
    </div>
    <hr>
    <div class="comment-list">
   
      <ul class="list-group list-group-flush">
      <li class="list-group-item" v-for="(comment, idx) in comments" :key="idx">
        <div class="row text-start align-items-center">
          <div class="col-2"><!--<span style="cursor:pointer;" @click="moveToProfile(comment.user, comment.username)">--><strong>{{ user[idx] }}</strong></div>
          <div class="col-8">{{ comments[idx] }}</div>
          <div class="col-2"><small>{{ comments_date[idx] }}</small></div>
        </div>
        <!--
        <div class="text-end" v-if="user.username === comment.username">
          <button class="m-1 btn content-font border btn-sm" @click="deleteComment(comment)">삭제</button>
        </div>-->
      </li>
    </ul>
    </div>
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

export default {
  name: 'MovieDetailCommentList',
  components: {
    
  },
  data() {
    return {
      comment_content: null,
      comment_data: [],
      comments: [],
      user: [],
      comments_date: [],
      is_liked: null,
      like_numbers: 0,
      is_hated: null,
      hate_numbers: 0,
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
    createComment() {
      
      const commentItem = {
        content: this.comment_content,
        movie_id: this.$route.params.movie_pk,
        rank: 3
      }
      if (commentItem.content) {
        const config = this.getToken()
        console.log(commentItem)
        axios.post(`http://127.0.0.1:8000/movies/${this.$route.params.movie_pk}/comments/create/`, commentItem, config) 
          .then(() => {
            this.getComments()
            this.comment_content = null
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
    getComments() {
      
      axios.get(`http://127.0.0.1:8000/movies/${this.$route.params.movie_pk}/comments/`)
      .then(res => {
        console.log(res.data)
        this.comment_data = res.data
      })
      .catch(err => {
        console.log(err)
      })
      .then(
      axios.get(`http://127.0.0.1:8000/accounts/users/`)
      .then(res => {
        console.log(res)
        this.comments_date = []
        this.comments = []
        this.user = []
        for (let i = 0; this.comment_data.length; i++){
          this.comments.push(this.comment_data[i].content)
          this.comments_date.push(this.comment_data[i].created_at)
          for (let j = 0; res.data.length; j++){
            if(res.data[j].id === this.comment_data[i].user){
              this.user.push(res.data[j].username)
              break
            }
          }
        }
      })
      .catch(err => {
        
        console.log(err)
      })
      )
    }
  },
  created : function(){
    this.getComments()
  }

}
</script>

<style>

</style>