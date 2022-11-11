import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'


Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movieList: null,
    todos: [],     
  },
  getters: {
    allTodosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state) {
      const completedTodos = state.todos.filter((todo) => {
        return todo.isCompleted === true
      })
      return completedTodos.length
    },
    unCompletedTodosCount(state, getters) {
      return getters.allTodosCount - getters.completedTodosCount
    },
  },
  mutations: {
    GET_MOIVE(state, movieList){
      state.movieList = movieList
    },
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS(state, todoItem) {
      console.log(todoItem)
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        } 
        return todo
      })
   }
  },
  actions: {
    getMovie(context) {
      const tmdbKey = process.env.VUE_APP_TMDB_API_KEY
      const movieUrl = `https://api.themoviedb.org/3/movie/top_rated?api_key=${tmdbKey}&language=ko-kr&page=1`

      axios({
        method: 'get',
        url: movieUrl,
      })
        .then((res) => {
          console.log(res.data.results)
          const movieList = res.data.results
          context.commit('GET_MOIVE',movieList)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    createTodo(context, todoTitle) {
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      context.commit('CREATE_TODO', todoItem)
    },
    deleteTodo(context, todoItem) {
      context.commit('DELETE_TODO', todoItem)
    },
    updateTodoStatus(context, todoItem) {
      context.commit('UPDATE_TODO_STATUS', todoItem)
    },
  },
  modules: {
  }
})
