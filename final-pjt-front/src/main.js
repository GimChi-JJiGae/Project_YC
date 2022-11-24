import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Carousel3d from 'vue-carousel-3d'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { NavbarPlugin } from 'bootstrap-vue'
import VueFeather from 'vue-feather';

Vue.use(NavbarPlugin)

library.add(fas, far, fab)
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(Carousel3d)
Vue.use(BootstrapVue)
Vue.use(VueFeather);
Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
