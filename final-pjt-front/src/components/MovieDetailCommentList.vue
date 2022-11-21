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
      <MovieDetailCommentListItem
      />
    </div>
  </div>
</template>

<script>
import MovieDetailCommentListItem from './MovieDetailCommentListItem.vue';
export default {
  name: 'MovieDetailCommentList',
  components: {
    MovieDetailCommentListItem,
  }


}
</script>

<style>

</style>