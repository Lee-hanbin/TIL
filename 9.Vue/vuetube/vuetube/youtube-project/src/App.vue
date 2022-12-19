<template>
  <div id="app">
    <h1>My First Youtube project</h1>
    <TheSearchBar
      @vue-input="getSearchBar"
    />
    <VideoDetail
      :video="selection"
    />
    <VideoList
      :video-props="videoList"
      @select-video="selectVideo"
    />
  </div>
</template>

<script>
import axios from 'axios'
import TheSearchBar from '@/components/TheSearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

export default {
  name: 'App',
  data () {
    return {
      inputData: null,        // 검생창에서 받아온 문자를 받아올 변수
      videoList: [],         // api에서 받아올 youtube 정보
      selection: null,
    }
  },
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  methods: {
    selectVideo(video){
      this.selection = video
    },
    getSearchBar: function (vuetubeInputData) {     //vuetubeInputData에 검색창에 친 값이 들어있음
      const Youtube_key = 'AIzaSyCb0d9lMjA2mzoklTaaZ0E07FhqLrwYnEc'
      const Youtube_url = 'https://www.googleapis.com/youtube/v3/search'
      this.inputData = vuetubeInputData
      // console.log(this.inputData)
      const params = {
        key: Youtube_key,
        part: 'snippet',
        type: 'video',
        q: this.inputData,      // 인풋 데이터에 해당하는 유튜브 영상
      }
      axios({
        method: 'get',
        url: Youtube_url,
        params
      })
        .then((response) => {
          // console.log(response)    // 응답을 찍어봐서 경로찾기
          this.videoList = response.data.items
          // console.log(this.videoList)  // 잘 찍히네  ^^
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
