<template>
  <div>
    <h5><strong>내가 리뷰 남긴 영화들</strong></h5>
    <span class=""><small>'리뷰 작성한' 영화 수 : {{user.movie_comments?.length}}</small></span>
    <div class="row  flex-nowrap" id="scollbar">
      <span v-for="comment_movie in comment_movies" :key=comment_movie.id style="width:190px;">
        <router-link :to="{name : 'MovieDetail', params : {movie_pk : comment_movie.id }}">
          <img :src='`https://image.tmdb.org/t/p/original/${comment_movie.poster_path}`' alt="" style="height:230px; width:180px;" class="rounded-2">
        </router-link>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyCommentList',
  props: {
    user: Object,
    comment_movies: Array,
  },
}
</script>

<style>

</style>