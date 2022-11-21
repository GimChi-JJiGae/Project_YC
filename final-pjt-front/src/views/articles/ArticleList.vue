<template>
  <div class="row">
    <div class="col-3">영화</div>
    <div class="col-4">제목</div>
    <div class="col-2">유저</div>
    <div class="col-1"><font-awesome-icon icon="fa-regular fa-thumbs-up"/></div>
    <div class="col-1"><font-awesome-icon icon="fa-regular fa-thumbs-down"/></div>
    <div class="col-1">조회</div>
    <hr>
    <div class="article-list">
      <ArticleListItem
      v-for="article in articles"
      :key="article.id"
      :article="article"
      />
    </div>
  </div>
</template>

<script>
import ArticleListItem from '@/views/articles/ArticleListItem'

export default {
  name: 'ArticleListView',
  components: {
    ArticleListItem
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>