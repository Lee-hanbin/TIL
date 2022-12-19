import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexView from '../views/IndexView.vue'
import CreateView from '../views/CreateView.vue'
import DetailView from '../views/DetailView.vue'
import NotFound404 from '../views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView,
  },
  {
    path: '/create',
    name: 'create',
    component: CreateView,
  },
  {
    path: '404-not-found',  // 이것을 detail보다 아래 두면 404에 걸림
    name: 'NotFound404',    // 따라서 detail보다 위에 두거나 path명을 바꿔
    component: NotFound404
  },
  {
    path: '/:id',     // 변수가 동적!
    name: 'detail',
    component: DetailView,
  },
  {
    path: '*',
    redirect: { name: 'NotFound404'}
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
