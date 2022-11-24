<template>
  <div class="row align-items-center justify-content-center" style="width: 100%;">
    <hr>
    <div class="row" style="width:100%;">
      <div class="col-1">유저</div>
      <div class="col-2">별점</div>
      <div class="col">내용</div>
      <div class="col-2">생성시간</div>
      <div class="col-1"><font-awesome-icon icon="fa-regular fa-thumbs-up"/></div>
      <div class="col-1"><font-awesome-icon icon="fa-regular fa-thumbs-down"/></div>
    </div>
    <hr>
    <div class="comment-list row" style="width:100%;">
   
      <ul class="list-group list-group-flush px-0">
      <li class="list-group-item p-0 mb-1" v-for="(comment, idx) in comments" :key="idx" >
        <div class="row m-0" style="width:100%;">
          <div class="col-1"><span style="cursor:pointer;" @click="moveToProfile(user[idx])"><strong>{{ user[idx] }}</strong></span></div>
          <div class="col-2">
            <star-rating :rating="comment_rank_list[idx]" :read-only="true" :increment="0.01" :star-size="15" class="justify-content-center"></star-rating>
          </div>
          <div class="col">{{ comment.content }}</div>
          <div class="col-2"><small>{{ comments_date[idx] }}</small></div>
          <div :id="`like` + idx" class="col-1" style="cursor:pointer;"  @click="likeComment(comments_id[idx])">{{ like_numbers[idx]}}</div>
          <div :id="`hate` + idx" class="col-1" style="cursor:pointer;" @click="hateComment(comments_id[idx])"> {{ hate_numbers[idx]}}</div>
        </div>
        <!--
        <div class="text-end" v-if="user.username === comment.username">
          <button class="m-1 btn content-font border btn-sm" @click="deleteComment(comment)">삭제</button>
        </div>-->
      </li>
    </ul>
    </div>
    <hr>
    <div @mouseleave="showCurrentRating(0)" style="display:inline-block;">
              <star-rating :show-rating="false" @current-rating="showCurrentRating" @rating-selected="setCurrentSelectedRating" :increment="0.5" active-color="#e1bad9"></star-rating>
            </div>
            <div style="margin-top:10px;font-weight:bold;">{{currentRating}}</div>
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
import StarRating from "vue-star-rating";

const SERVER_URL = 'http://127.0.0.1:8000'



export default {
  name: 'MovieDetailCommentList',
  components: {
    StarRating,
  },
  data() {
    return {
      comment_content: null,
      comments_id : [],     // 순서대로 배열에 집어넣으면 몇 번째 댓글의 pk를 알수있음
      comment_data: [],
      comments: [],
      user: [],
      comments_date: [],
      is_liked: null,
      like_numbers: [],
      is_hated: null,
      hate_numbers: [],
      rating: "No Rating Selected",
      currentRating: "No Rating",
      currentSelectedRating: "No Current Rating",
      //boundRating: 3,
      final_rate: 0,
      comment_rank_list: [],
    }
  },
  computed: {
    //comment_like_list() {
    //  return this.like_numbers
    //},
    isLogin() {
      const checkToken = localStorage.getItem('access_token')
      if(checkToken === null){
        return false
      }
      else {
        return true
      }
    }
  },
  methods: {
    setRating: function(rating) {

      this.final_rate = rating
      this.rating = "You have Selected: " + rating + " stars";
    },
    showCurrentRating: function(rating) {
      this.currentRating = (rating === 0) ? this.currentSelectedRating : "Click to select " + rating + " stars"

    },
    setCurrentSelectedRating: function(rating) {
      this.currentSelectedRating = "You have Selected: " + rating + " stars";
      this.final_rate = rating
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
    likeComment(comment_pk) {
      const config = this.getToken()
      this.is_liked = !this.is_liked
      axios.post(`${SERVER_URL}/movies/${comment_pk}/comments/like/`,this.is_liked, config)
        .then(res => {
          
          const idx = this.comments_id.indexOf(comment_pk)
          //this.is_liked = res.data.is_liked
          this.like_numbers[idx] = res.data.likes_count
         
          
          // this.getArticleDetail()

          for (let i = 0; i < this.comment_data.length; i++){
            document.getElementById(`like${i}`).innerHTML = this.like_numbers[i]
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    hateComment(comment_pk) {
      const config = this.getToken()
      this.is_liked = !this.is_liked
      axios.post(`${SERVER_URL}/movies/${comment_pk}/comments/hate/`, this.is_liked, config)
        .then(res => {
          
          const idx = this.comments_id.indexOf(comment_pk)
          //this.is_hated = res.data.is_hated
          this.hate_numbers[idx] = res.data.hates_count

          
          // this.getArticleDetail()
          for (let i = 0; i < this.comment_data.length; i++){
            document.getElementById(`hate${i}`).innerHTML = this.hate_numbers[i]
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    createComment() {
      if (!this.isLogin){
        alert("댓글을 적으시려면 로그인을 해주세요!")
        this.$router.push({ name: 'LogInView' })
        return
      }

      if (this.currentSelectedRating === "No Current Rating"){
        alert("별점을 매겨주세요!")
        return
      }
      const commentItem = {
        content: this.comment_content,
        movie_id: this.$route.params.movie_pk,
        rank: this.final_rate,
      }
      if (commentItem.content) {
        const config = this.getToken()
        axios.post(`http://127.0.0.1:8000/movies/${this.$route.params.movie_pk}/comments/create/`, commentItem, config) 
          .then(() => {
            this.getComments()
            
          })
          .then(() => {
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
        this.comment_data = res.data
      })
      .catch(err => {
        console.log(err)
      })
      .then(
      axios.get(`http://127.0.0.1:8000/accounts/users/`)
      .then(res => {
        // 여기서 새로고침마다 초기화 시켜주자
        this.comments_id = []
        this.comments_date = []
        this.comments = []
        this.user = []
        this.like_numbers = []
        this.hate_numbers = []
        this.comment_rank_list = []
        for (let i = 0; i < this.comment_data.length; i++){
          this.comments.push(this.comment_data[i])
          let timeinfo = this.comment_data[i].created_at
          let year_month_day = timeinfo.split('T')
          let hour_minuite = year_month_day[1].split(':')
          this.comments_date.push(year_month_day[0] + ' ' + hour_minuite[0] + ':' + hour_minuite[1])
          this.comments_id.push(this.comment_data[i].id)
          this.like_numbers.push(this.comment_data[i].like_movie_comment_users.length)
          this.hate_numbers.push(this.comment_data[i].hate_movie_comment_users.length)
          this.comment_rank_list.push(this.comment_data[i].rank)
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
    },
    moveToProfile(username) {
      this.$router.push({ name: "ProfileView", params: { username: username} })
    },
  },
  created : function(){
    this.getComments()
  },
  mounted: function(){
    
  },
  beforeDestroy : function() {
    
  },
  

}
</script>

<style>

</style>