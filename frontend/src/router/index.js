import Vue from 'vue'
import VueRouter from 'vue-router'
import Employee from '@/components/Employee'
import Customer from '@/components/customer'
import Order from '@/components/Order'
import AddEmployee from '@/components/AddEmployee'

Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/employee',
      name: 'employee',
      component: Employee
    },
    {
      path: '/employee/add',
      name: 'addEmployee',
      component: AddEmployee
    },
    {
      path: '/customer',
      name: 'customer',
      component: Customer
    },
    {
      path: '/order',
      name: 'order',
      component: Order
    },
  ]
})
