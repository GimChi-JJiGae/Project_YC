<template>
  <div>
    <div class="row">
      <div class="col-3">영화</div>
      <div class="col-4">제목</div>
      <div class="col-2">글쓴이</div>
      <div class="col-1"><font-awesome-icon icon="fa-regular fa-thumbs-up"/></div>
      <div class="col-1"><font-awesome-icon icon="fa-regular fa-thumbs-down"/></div>
      <div class="col-1">조회</div>
      <hr class="border-top border-bottom border-dark border-2">
      <div class="article-list">
        <ArticleListItem
        v-for="article in paginatedData"
        :key="article.id"
        :article="article"
        />
      </div>
    </div>
    <div class="row mb-3">
      <div class="col-3"></div>
      <div class="col">
        <button :disabled="pageNum === 0" @click="prevPage" class="btn content-font border btn-sm me-1">
          이전
        </button>
        <span class="page-count"><small>{{ pageNum + 1 }} / {{ pageCount }} 페이지</small></span>
        <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="btn content-font border btn-sm ms-1">
          다음
        </button>
      </div>
      <div class="col-3 text-end p-0">
        <button class="btn content-font border btn-sm">
          <router-link :to="{ name: 'ArticleCreateView' }" class="text-decoration-none text-black">게시글 생성</router-link>
        </button>
      </div>
    </div>
    <div class="row align-items-center">
      <div class="col-3"></div>
      <div class="col row">
        <div class="col p-0 row justify-content-end me-1">
          <select style="font-size: 14px; width: 100px; height:36px;" v-model="keyword" class="st-font form-select">
            <option :value="keyword" v-for="(keyword, idx) in keywords" :key="idx">{{keyword}}</option>
          </select>
        </div>
        <div class="col p-0">
          <input class="stage-search border-opacity-10 rounded-2" type="text" v-model="search" placeholder="검색어" @keyup.enter="handleSearchInput" style="width:100%; height:36px;"/>
        </div>
        <div class="col-2 p-0 text-start">
          <button class="btn content-font border btn-sm" style="height:36px;" @click="handleSearchInput" type="sumbit">
            <span style="font-size: 11px;">검색</span>
          </button>
        </div>
      </div>
      <div class="col-3">
      </div>
    </div>
</div>
</template>

<script>
import ArticleListItem from '@/views/articles/ArticleListItem'

export default {
  name: 'ArticleListView',
  data() {
    return {
      search: null,
      keywords: ['제목', '글쓴이'],
      keyword: '제목',
      pageNum: 0,
      pageSize: 5,
    }
  },
  components: {
    ArticleListItem
  },
  computed: {
    articles() {
      if (this.$store.state.searchArticles.length) {
        return this.$store.state.searchArticles
      }
      return this.$store.state.articles
    },
    pageCount () {
      let listLeng = this.articles.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      if (page === 0) page = 1
      
      /*
      아니면 page = Math.floor((listLeng - 1) / listSize) + 1;
      이런식으로 if 문 없이 고칠 수도 있다!
      */
      return page;
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.articles.slice(start, end);
    },
  },
  methods: {
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },
    handleSearchInput() {
      if (this.search) {
        clearTimeout(this.debounce)
        this.debounce = setTimeout(() => {
          let filteredList = []
          if (this.keyword === '제목') {
            filteredList = this.$store.state.articles.filter(article => article.title.includes(this.search))
          } else if (this.keyword === '글쓴이') {
            filteredList = this.$store.state.articles.filter(article => article.username.includes(this.search))
          }
          this.$store.dispatch('searchArticles', filteredList)
        }, 500)
      } else {
        clearTimeout(this.debounce)
        this.debounce = setTimeout(() => {
          this.$store.dispatch('searchArticles', [])
        }, 500)
      }
    },
  },
  beforeDestroy() {
    this.$store.dispatch('searchArticles', [])
  }
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>