import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    token: null,
  },
  getters: {
  },
  mutations: {
    // auth
    SIGN_UP(state, token) {
      state.token = token
    }
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/registration/`,
        data: {
          username, password1, password2
        }
      })
        .then(res => {
          console.log(res.data)
          context.commit('SIGN_UP', res.data.key)
        })
        .catch(err => console.log(err))
    }
  },
  modules: {
  }
})
