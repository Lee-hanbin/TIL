<template>
  <div v-if="video">
    <iframe :src="videoURL" frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video:{
      type:Object
    }
  },
  computed:{
    videoURL() {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>

</style>