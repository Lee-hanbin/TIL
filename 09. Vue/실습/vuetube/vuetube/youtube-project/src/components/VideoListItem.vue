<template>
  <li @click="selectVideo">
    <img :src="videopropsProps.snippet.thumbnails.default.url" alt="유튜브 이미지">
    {{ videopropsProps.snippet.title }}
  </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props:{
    videopropsProps:{
      type: Object,
    }
  },
  methods:{
    selectVideo(){
      this.$emit('select-video',this.videopropsProps)
    }
  }
}
</script>

<style>

</style>