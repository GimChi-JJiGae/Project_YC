import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'

import LogInView from '@/views/accounts/LogInView'
import SignUpView from '@/views/accounts/SignUpView'
import UsersView from '@/views/accounts/UsersView'
import ProfileView from '@/views/accounts/ProfileView'
import MyProfileView from '@/views/accounts/MyProfileView'
import UpdateUserView from '@/views/accounts/UpdateUserView'
import UpdatePassword from '@/views/accounts/UpdatePassword'

import ArticleHomeView from '@/views/articles/ArticleHomeView'
import ArticleDetailView from '@/views/articles/ArticleDetailView'
import ArticleCreateView from '@/views/articles/ArticleCreateView'
import ArticleUpdate from '@/views/articles/ArticleUpdate'


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
    path: '/:username/update',
    name: 'UpdateUserView',
    component: UpdateUserView,
  },
  {
    path: '/:username/change_password',
    name: 'UpdatePassword',
    component: UpdatePassword,
  },
  {
    path: '/:username/profile',
    name: 'ProfileView',
    component: ProfileView,
  },
  {
    path: '/myprofile',
    name: 'MyProfileView',
    component: MyProfileView,
  },
  {
    path: '/articles',
    name: 'ArticleHomeView',
    component: ArticleHomeView,
  },
  {
    path: '/article/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView,
  },
  {
    path: '/article/create',
    name: 'ArticleCreateView',
    component: ArticleCreateView,
  },
  {
    path: '/article/:id/update',
    name: 'ArticleUpdate',
    component: ArticleUpdate,
  },



]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
