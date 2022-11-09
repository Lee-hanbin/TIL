<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호: {{ article?.id }}</p>
    <p>글 제목: {{ article?.title }}</p>
    <p>글 내용: {{ article?.content }}</p>
    <!-- <p>글 작성시간: {{ article?.createdAt }}</p> -->
    <p>작성시간: {{ articleCreatedAt }}</p>
    <button @click="deleteArticle">삭제</button><br>
    <router-link :to="{ name: 'index' }">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  name: 'DetailView',
  data() {
    return {
      article: null     // 찾은 값을 여기에 저장해야함
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
    articleCreatedAt() {
      const article = this.article
      const createdAt = new Date(article?.createdAt).toLocaleString()
      return createdAt
    },
  },
  methods: {
    getArticleById(id) {
      //이 id 값으로 배열에서 값 찾기 (이 값은 url로 들어오므로 문자임!)
      // const id = this.$route.params.id          // url로 들어온 id를 가지고
      for (const article of this.articles) {    // 배열을 순회하여
        if (article.id === Number(id)) {        // article의 id와 url로 들어온 int(id)가 같으면
          this.article = article                // 해당 article을 data의 article 변수에
          break
        }
      }
      if (this.article === null) {
        this.$$router.push({ name: 'NotFound404'})
      }
    },
    //actions에서 할게 없으니까 바로 mutations로 보내자
    deleteArticle() {
      this.$store.commit('DELETE_ARTICLE', this.article.id)
      this.$router.push({ name: 'index' })
    }
  },
  created() {
    this.getArticleById(this.$route.params.id)
  }
}
</script>

<style>

</style>