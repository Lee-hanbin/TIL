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
      state.article_id = state.article_id + 1
    }
  },
  actions: {
    CreateArticle(context, payload){
      const article = {
        id: context.state.article_id,
        title: payload.title,
        content: payload.content,
        createdAtL new Date().getTime(),
      }
      context.commit('CREATE_ARTICLE', article)
    }
  },
  modules: {
  }
})
