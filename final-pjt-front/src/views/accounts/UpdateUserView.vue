<template>
  <div class="row justify-content-center">
    <div class="border p-3 rounded-3 row justify-content-center" style="width:500px; height:550px">
      <div style="width:300px; height: 70px;" class="my-3">
        <form @submit.prevent="update">
          <div class="text-start " style="height: 150px;">
            <div class="row">
              <label for="username" class="st-font form-label"><strong>프로필 사진</strong></label>
            </div>
            <div class="row">
              <div class="filebox" style="height: 100px;">
                <label for="ex_file" style='height:100px; width:100px; border-radius:50%; overflow:hidden; padding: 0px;'>
                  <img v-if="image" :src="image" alt="" style="width: 100%; height:100%; object-fit: cover;">
                  <img v-else :src="basic" alt="" style="width: 100%; height:100%; object-fit: cover;">
                </label> 
                <input type="file" @change="onInputImage()" id="ex_file" ref="serveyImage">
              </div>
            </div>
          </div>
          <div class="text-start mb-3" style="height: 70px;">
            <label for="username" class="st-font form-label"><strong>아이디</strong></label>
            <input v-model.trim="user.username" id="id" type="text" placeholder="아이디" required="required" data-validation-required-message="Please enter your username." class="form-control"/><br>
          </div>

          <div class="text-start mb-3" style="height: 70px;">
            <label for="email" class="st-font form-label"><strong>Email</strong></label>
            <input v-model.trim="user.email" id="email" type="text" placeholder="email" required="required" data-validation-required-message="Please enter your email address." class="form-control"/>
          </div>

          <div class="text-start mb-3" style="height: 70px;">
            <label for="password1" class="st-font form-label"><strong>비밀번호</strong></label>
            <input v-model.trim="password" id="password" type="password" placeholder="Password" required="required" data-validation-required-message="Please enter your password." class="form-control"/>
          </div>
          
          <div class="mt-3">
            <button class="btn content-font border" type="submit">변경</button>
            <button @click="moveToChangePassword" class="btn content-font border">비밀번호 변경하기</button>
          </div>
        </form>
        <div class="mt-2">
          <button @click="open" class="m-2 btn content-font">회원 탈퇴</button>
        </div>
        <b-modal
          hide-footer
          v-model="show"
          id="deleteUser-modal"
          size="md"
          title="회원탈퇴"
          hide-header-close
        >
          <div class="text-start mb-3" style="height: 100px;">
            <label for="password1" class="st-font form-label"><strong>비밀번호를 입력하세요</strong></label>
            <input v-model.trim="password" id="password" type="password" placeholder="Password" required="required" data-validation-required-message="Please enter your password." class="form-control"/>
            <button @click="deleteUser" class="my-2 btn btn-outline-dark btn-sm">회원 탈퇴</button>
          </div>
        </b-modal>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"
// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UpdateUserView',
  data() {
    return {
      user: [],
      original_username: null,
      password: null,
      image: null,
      basic: null,
      is_upload: null,
      show: false,
      variants: ["light", "dark"],
      headerBgVariant: "dark",
      headerTextVariant: "white",
      bodyBgVariant: "dark",
      bodyTextVariant: "white",
      footerBgVariant: "danger",
      footerTextVariant: "dark",
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
    getImage(url) {
      this.image = SERVER_URL + url
    },
    getMyName: function () {
      const config = this.getToken()

      const hash = localStorage.getItem('access_token')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
      .then( (res) => {
        this.user = res.data
        this.original_username = res.data.username
        this.image = SERVER_URL + res.data.image
        if (this.user.image) {
          this.getImage(this.user.image)
        } else {
          const url = '/media/basic.png'
          this.getImage(url)
        }
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    onInputImage() {
      let files = this.$refs.serveyImage.files
      this.user.image = this.$refs.serveyImage.files
      this.is_upload = this.$refs.serveyImage.files
      let reader = new FileReader()
      reader.readAsDataURL(files[0])
      reader.onload = e => {
        this.image = e.target.result
      }
    },
    update() {
      const token = this.getToken().headers.Authorization
      const formdata = new FormData()
      formdata.append('username', this.user.username)
      formdata.append('age', this.user.age)
      formdata.append('sex', this.user.sex)
      formdata.append('email', this.user.email)
      formdata.append('password', this.password)
      formdata.append('passwordConfirmation', this.password)
      if (this.is_upload) {
        formdata.append('image', this.user.image[0])
      } 

      // axios.put(`${SERVER_URL}/accounts/${this.original_username}/update/`, data, config)
      axios({
        method: 'put',
        url: `${SERVER_URL}/accounts/${this.original_username}/update/`,
        headers: {
          'Content-Type':'multipart/form-data',
          'Authorization': `${token}`,
        },
        data: formdata
      })
      .then( () => {
        const login_credential = {
          username: this.user.username,
          password: this.password,
        }
        axios.post(`${SERVER_URL}/accounts/api-token-auth/`, login_credential)
          .then((res) => {
            localStorage.setItem('access_token', res.data.token)
            this.$store.dispatch('LogIn', res.data.token)
            this.$router.push({ name: "HomeView" }).catch(()=>{})
          })
          .catch( (err) => {
            console.log(err)
          })
        })
      .catch( (err) => {
        console.log(err)
      })
    },
    moveToChangePassword() {
      this.$router.push({ name: 'UpdatePassword', params: { username: `${this.original_username}`} })
    },
    deleteUser() {
      const config = this.getToken()
      axios.delete(`${SERVER_URL}/accounts/${this.user.username}/delete/`, {headers: config['headers'], data: {password:this.password}})
        .then(() => {
          this.$store.dispatch('LogOut')
          this.$router.push({ name: 'HomeView' })
        })
    },
    open() {
      this.show = true
    },
    close() {
      this.show = false
    }
  },
  created() {
    this.getMyName()
  }
}
</script>

<style>
.filebox label {
  display: inline-block;
  padding: .5em .75em;
  color: #999;
  font-size: inherit;
  line-height: normal;
  vertical-align: middle;
  background-color: #fdfdfd;
  cursor: pointer;
  border: 1px solid #ebebeb;
  border-bottom-color: #e2e2e2;
  border-radius: .25em;
}

.filebox input[type="file"] {  /* 파일 필드 숨기기 */
  position: absolute;
    width: 0;
    height: 0;
    padding: 0;
    overflow: hidden;
    border: 0;
}
</style>