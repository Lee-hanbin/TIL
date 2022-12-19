import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    article_id: 3,      // 다음에 작성될 3번의 글의 id
    articles: [
      {
        id: 1,
        title: 'title',
        content: 'content',
        createdAt: new Date().getTime(),
      },
      {
        id: 2,
        title: 'title2',
        content: 'content2',
        createdAt: new Date().getTime(),
      },
    ]
  },
  getters: {
  },
  mutations: {
    CREATE_ARTICLE(state, article) {
      state.articles.push(article)
      state.article_id = state.article_id + 1 //위에 적었던 3번째 글 이후에 +1씩
    },
    DELETE_ARTICLE(state, article_id) {
      // filter를 통해 articles라는 배열에서 
      // article.id === article_id 이면 false를 만들고 해당 값을 빼고 배열 다시 만들기
      state.articles = state.articles.filter((article) =>{
        return !(article.id === article_id)
      })
    }
  },
  actions: {
    createArticle(context, payload){    // 이거 첫 글자 소문자ㅠ
      const article = {
        id: context.state.article_id,
        title: payload.title,
        content: payload.content,
        createdAt: new Date().getTime(),
      }
      context.commit('CREATE_ARTICLE', article)
    }
  },
  modules: {
  }
})
