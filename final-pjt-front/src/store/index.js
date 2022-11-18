import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)
// const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    
    access_token: null,

    articles: [],

    sex: ["male", "female"],
    ages: ["10대", "20대", "30대", "40대", "50대", "60대", "70대", "80대", "90대", ],
    reviewRate: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    
    movies: [],
    
  },
  getters: {
    isLogin(state) {
      state.access_token = localStorage.getItem('access_token')
      // console.log(state.access_token)
      return state.access_token ? true : false
    }
  },
  mutations: {
    // auth
    SAVE_TOKEN(state, token) {
      state.access_token = token
      router.push({ name: 'HomeView' }).catch(()=>{})
    },
    LOGOUT(state) {
      state.access_token = null
      localStorage.removeItem('access_token')
      localStorage.removeItem('vuex')
      // router.push({ name: 'HomeView' })
    },
    CLEAR_MOVIES(state){
      state.movies
    },
    GET_ARTICLES(state, articles) {
      state.articles = articles
    }
  },
  actions: {
    // 처음 영화 데이터를 받아올 함수
    // getMovies(context) {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/movies/`,
        // headers: {
        //   Authorization: `Bearer ${ context.state.access_token }`
        // }
    //   })
    //     .then(res => {
    //       context.commit('GET_MOVIES', res.data)
    //     })
    //     .catch(err => console.log(err))
    // },
    LogIn(context, token) {
      context.commit('SAVE_TOKEN', token)
    },
    LogOut(context) {
      context.commit('LOGOUT')
    },
    getArticles(context, articles) {
      context.commit('GET_ARTICLES', articles)
    }
  },
  modules: {
  }
})
