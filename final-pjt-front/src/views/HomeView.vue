<template>
  <div>

  </div>
</template>

<script>
export default {
  name: 'HomeView',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    getMovies() {
      if (this.isLogin) {
        // this.$store.dispatch('getMovies')
      } else {
        // 로그인 안했을 때 페이지 보여주기
      }
    }
  },
  created() {

  }
}
</script>

<style>

</style>