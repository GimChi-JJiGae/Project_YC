import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import LogInView from '@/views/accounts/LogInView'
import SignUpView from '@/views/accounts/SignUpView'
import UsersView from '@/views/accounts/UsersView'
import ProfileView from '@/views/accounts/ProfileView'
import MyProfileView from '@/views/accounts/MyProfileView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView,
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView,
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView,
  },
  {
    path: '/logout',
    name: 'LogOut',
  },
  {
    path: '/users',
    name: 'UsersView',
    component: UsersView,
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView,
  },
  {
    path: '/myprofile',
    name: 'MyProfileView',
    component: MyProfileView,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
