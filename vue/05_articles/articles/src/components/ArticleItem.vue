<template>
  <div>
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
  }
}
</script>

<style>

</style>