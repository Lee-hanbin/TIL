import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import RandomView from '@/views/RandomView'
import WatchListView from '@/views/WatchListView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/random',
    name: 'random',
    component: RandomView
  },
  {
    path: '/watch-list',
    name: 'watchlist',
    component: WatchListView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
