import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView'
import LoginVuew from '@/views/LoginView'
import NotFound404View from '@/views/NotFound404View'
import DogView from '@/views/DogView'

Vue.use(VueRouter)

const isLoggedIn = true 

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginVuew,
    //추가
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인 되어있음') //이미 로그인 된 사용자는
        next({ name: 'home' })            //home으로 바로 이동시키기
      } else {
        next()                            //아닌 사용자는 login으로
      }
    }
  },
  {
    path: '/404',
    name: 'NotFound404View',
    component: NotFound404View,
  },
  {
    path: '/dog/:breed',  //품종
    name: 'dog',
    component: DogView,
  },
  {
    path: '*',
    redirect: '/404',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach((to, from, next) => {
//   //로그인 여부
//   const isLoggedIN = false

//   //로그인이 필요한 페이지
//   const authPages= ['hello','about']

//   // authPages라는 배열에 to에 들어있는 url의 name이 포함되어 있는 지 확인
//   const isAuthRequired = authPages.includes(to.name) 

//   // 해당 페이지가 로그인이 필요한 페이지이고 로그인이 되어 있는 경우
//   if (isAuthRequired && !isLoggedIN) {
//     console.log('Login으로 이동!')
//     next({ name: 'login'})
//   } else {  //비로그인 사용자는 hello와 about으로 못 들어감
//     console.log('to로 이동!')
//     next()
//   }
// })

export default router
