<template>
  <div style='cursor:pointer' @click="moveToDetail">
    <h5>{{ article.id }}</h5>
    <p>작성자 : {{ article.username }}</p>
    <p>{{ article.title }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
  methods: {
    moveToDetail() {
      this.$router.push({ name: 'ArticleDetailView', params: { id: this.article.id } })
    }
  }
}
</script>

<style>

</style>