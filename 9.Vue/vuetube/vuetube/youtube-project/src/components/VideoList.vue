<template>
  <div>
    <h1>난 리스트</h1>
    <VideoListItem
      v-for="video in videoProps" 
      :key="video.id.videoId"
      :videoprops-props="video"
      @select-video="selectVideo"
    />
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videoProps: Array,
  },
  methods: {
    selectVideo(video){
      this.$emit('select-video',video)
    }
  }
}
</script>

<style>

</style>