<template>
  <div class="row align-items-center" style='cursor : pointer;' @click="moveToDetail" >
    <div class="col-3 text-center"><span style='cursor : pointer;' @click="moveToMovieDetail" >{{movies[article?.movie-1].title}}</span></div>
    <div class="col-4 text-center">{{article?.title}}</div>
    <div class="col-2 text-center"><span style='cursor:pointer;' @click= "moveToProfile" >{{article?.username}}</span></div>
    <div class="col-1 text-center">{{article?.like_users.length}}</div>
    <div class="col-1 text-center">{{article?.hate_users.length}}</div>
    <div class="col-1 text-center">{{article?.viewnums}}</div>
    <hr>
  </div>
</template>

<script>

export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
  data() {
    return {
      movies: JSON.parse(localStorage.getItem("movie_list")),
    }
  },
  methods: {
    moveToDetail() {
      this.$router.push({ name: 'ArticleDetailView', params: { id: this.article.id } })
    },
    moveToProfile() {
      this.$router.push({ name: "ProfileView", params: { username: `${this.article.username}` } })
    },
    moveToMovieDetail() {
      this.$router.push({name : 'MovieDetail', params : {movie_pk : `${this.article.movie}` } })
    }
  }
}
</script>

<style>

</style>