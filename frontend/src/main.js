// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import ElementUI, {Aside, Container, Main, Menu, MenuItem, MenuItemGroup, Submenu} from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI)
Vue.use(Container)
Vue.use(Menu)
Vue.use(Submenu)
Vue.use(MenuItem)
Vue.use(MenuItemGroup)
Vue.use(Main)
Vue.use(Aside)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App)
})
