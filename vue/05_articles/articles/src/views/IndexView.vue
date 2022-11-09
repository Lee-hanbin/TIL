<template>
  <div>
    <h1>Articles</h1>
    <ArticleItem
      v-for="article in articles"
      :key=article.id
      :article=article
    />
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem'

export default {
  name: 'IndexView',
  components: {
    ArticleItem,
  },
  computed: {
    articles () {
      return this.$store.state.articles
    }
  },
}
</script>

<style>

</style>