<template>
  <div class="d-flex flex-column align-items-center">
    <div class="row align-items-center">
      <div class="col row">
        <input class="stage-search border-opacity-10 rounded-2" type="text" v-model="search" placeholder="유저 이름" @input="handleSearchInput" style="width:100%; height:36px;"/>
      </div>
      <div class="col-2 p-0 text-start">
        <button class="btn content-font border btn-sm" style="height:36px;" @click="handleSearchInput" type="sumbit">
          <span style="font-size: 11px;">검색</span>
        </button>
      </div>
    </div>
    <hr style="width: 400px">
    <div class="">
      <ul class="list-group list-group-flush" style="width:300px;" >
        <li
         v-for="(user, idx) in Users"
        :key="idx"
        class="list-group-item"
        style="height: 90px;"
        >
          <div class="row align-items-center" style="height: 100%;">
            <div class="col-3 p-0" style='height:100%; border-radius:50%; overflow:hidden; '>
              <img v-if="user.image" :src="SERVER_URL+user.image" alt="" style="width: 100%; height:100%; object-fit: cover;">
              <img v-else :src="basic" alt="" style="width: 100%; height:100%; object-fit: cover;">
            </div>
            <div class="col row align-content-center">
              <div class="row align-content-center">
                <span @click="moveToProfile(user)" style="cursor:pointer;" class="fs-5 fw-semibold">{{ user.username }}</span>
              </div>
              <div class="row align-content-center">
                <span @click="moveToProfile(user)" class="fs-6">{{ user.email }}</span>
              </div>
            </div>
            <div class="col">
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UsersView',
  data() {
    return {
      users: [],
      filteredUsers: [],
      search: null,
      SERVER_URL : 'http://127.0.0.1:8000',
      basic: SERVER_URL + '/media/basic.png',
    }
  },
  computed: {
    Users() {
      if (this.search) {
        return this.filteredUsers
      } else {
        return this.users
      }
    }
  },
  methods: {
    getToken() {
      const token = localStorage.getItem('access_token')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    getUsers() {
      const config = this.getToken()
      axios.get(`${SERVER_URL}/accounts/users`, config)
        .then(res => {
          this.users = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    moveToProfile(user) {
      this.$router.push({ name: "ProfileView", params: { username: `${user.username}` }})
    },
    handleSearchInput() {
      if (this.search !== 0) {
        clearTimeout(this.debounce)
        this.debounce = setTimeout(() => {
          let filteredUsers = []
          filteredUsers = this.users.filter(user => user.username.includes(this.search))
          this.filteredUsers = filteredUsers
        }, 500)
      } else {
        clearTimeout(this.debounce)
        this.debounce = setTimeout(() => {
          this.filteredUsers = []
        }, 500)
      }
    },
  },
  created() {
    this.getUsers()
  }
}
</script>

<style>

</style>