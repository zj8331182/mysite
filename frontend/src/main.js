// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import ElementUI, {Aside, Container, Main, Menu, MenuItem, PageHeader} from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import router from './router'
import globalVariable from '@/api/globalVariable.js'

Vue.prototype.GLOBAL = globalVariable

Vue.use(ElementUI)
Vue.use(Container)
Vue.use(Menu)
Vue.use(MenuItem)
Vue.use(Main)
Vue.use(Aside)
Vue.use(PageHeader)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
