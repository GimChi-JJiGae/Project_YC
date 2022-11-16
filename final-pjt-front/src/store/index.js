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
    movies: [],
  },
  getters: {
    isLogin(state) {
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
      localStorage.access_token = null
      // router.push({ name: 'HomeView' })
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
      const email = payload.email
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/registration/`,
        data: {
          email, password1, password2
        }
      })
        .then(res => {
          // console.log(res.data)
          const token = res.data.access_token
          context.commit('SAVE_TOKEN', token)
        })
        .catch((err) => {
          const errMsg = JSON.parse(err.response.request.response)
          console.log(errMsg)
          if (errMsg.email) {
            alert("email : " + errMsg.email)
          } else if (errMsg.password1) {
            alert("password : " + errMsg.password1)
          } else if (errMsg.password2) {
            alert("password confirmation : " + errMsg.password2)
          } else if (errMsg.non_field_errors) {
            alert(errMsg.non_field_errors)
          }
        })
    },
    LogIn(context, payload) {
      const email = payload.email
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          email, password
        }
      })
        .then(res => {
          const token = res.data.access_token
          context.commit('SAVE_TOKEN', token)
        })
        .catch(err => console.log(err))
    },
    LogOut(context) {
      context.commit('LOGOUT')
    }
  },
  modules: {
  }
})
