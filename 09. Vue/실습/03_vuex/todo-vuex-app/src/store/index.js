import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todos: []
  },
  getters: {
    allTodosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state) {
      // 1. 완료된 투두만 모아놓은 새로운 배열을 생성
      const completedTodos = state.todos.filter((todo) => {
        return todo.isCompleted === true
      })
      // 2. 그 새로운 배열의 길이를 반환
      return completedTodos.length
    },
    unCompletedTodosCount(state, getters) {
      return getters.allTodosCount - getters.completedTodosCount
    }
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS(state, todoItem) {
      console.log(todoItem)
      // todos 배열에서 선택된 todo의 is_completed값만 토글한 후
      // 업데이트 된 todos 배열로 되어야 함
      state.todos = state.todos.map((todo)=> {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    },
    // LOAD_TODOS(state) {
    //   const localStorageTodos =  localStorage.getItem('todos')
    //   const parsedTodos = JSON.parse(localStorageTodos)
    //   state.todos = parsedTodos
    // }
  },
  actions: {
    createTodo(context, todoTitle) {
      // Todo 객체 만들기
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      // console.log(todoItem)
      context.commit('CREATE_TODO', todoItem)
      // context.dispatch('saveTodosToLocalStorage')
    },
    // actions가 할게 없어보임 => 생략
    deleteTodo(context, todoItem) {
      context.commit('DELETE_TODO', todoItem)
      // context.dispatch('saveTodosToLocalStorage')
    },
    updateTodoStatus(context, todoItem) {
      context.commit('UPDATE_TODO_STATUS', todoItem)
      // context.dispatch('saveTodosToLocalStorage')
    },
    // saveTodosToLocalStorage(context) {
    //   const jsonTodos = JSON.stringify(context.state.todos)
    //   window.localStorage.setItem('todos' , jsonTodos ) //key는 임의 지정하면 된다.
    // },
    // loadTodos(context) {
    //   context.commit('LOAD_TODOS')
    // }
  },
  modules: {
  }
})
