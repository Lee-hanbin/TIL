<template>
  <div @click="goDetail(article.id)">
      <p>글 번호 : {{ article.id }}</p>
      <p>글 제목 : {{ article.title }}</p>
      <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  },
  methods: {
    goDetail(id) {
      this.$router.push({ name: 'detail', params: {id} })
      // this.$router.push({ name: 'detail', params: {id: `${this.article.id}`} }) // 이건 props에서 가져옴
      
    }
  }
}
</script>

<style>

</style>