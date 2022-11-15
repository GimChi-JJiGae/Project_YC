import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    access_token: null,
    refresh_token: null,
  },
  getters: {
    isLogin(state) {
      return state.access_token ? true : false
    }
  },
  mutations: {
    // auth
    SAVE_TOKEN(state, tokens) {
      state.access_token = tokens[0]
      state.refresh_token = tokens[1]
      router.push({ name: 'HomeView' })
    }
  },
  actions: {
    // 처음 영화 데이터를 받아올 함수
    // getMovies(context) {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/movies/`,
    //     headers: {
    //       Authorization: `Bearer ${ context.state.access_token }`
    //     }
    //   })
    //     .then(res => {
    //       context.commit('GET_MOVIES', res.data)
    //     })
    //     .catch(err => console.log(err))
    // },

    signUp(context, payload) {
      const username = payload.username
      const email = payload.email
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/registration/`,
        data: {
          username, email, password1, password2
        }
      })
        .then(res => {
          console.log(res.data)
          const tokens = [res.data.access_token, res.data.refresh_token]
          context.commit('SAVE_TOKEN', tokens)
        })
        .catch(err => console.log(err))
    },
    logIn(context, payload) {
      const username = payload.username
      const email = payload.email
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, email, password
        }
      })
        .then(res => {
          const tokens = [res.data.access_token, res.data.refresh_token]
          context.commit('SAVE_TOKEN', tokens)
        })
        .catch(err => console.log(err))
    },
  },
  modules: {
  }
})
