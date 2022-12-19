<template>
  <div>
    <p v-if="!imgSrc">{{ message }}</p>
    <img :src="imgSrc" alt="">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DogView',
  data() {
    return {
      imgSrc: null,
      message: '로딩중...',
    }
  },
  methods: {
    getDogImage() {
      const breed = this.$route.params.breed
      const dogImageUrl = `https://dog.ceo/api/breed/${breed}/images/random`
      
      axios({
        method: 'get',
        url: dogImageUrl,
      })
        // axios 요청이 성공 했을 때,
        .then((response) => {
          //이 console을 통해 img 주소를 찾는다.
          console.log(response)
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error) => {
          // this.message = `${this.$route.params.breed}은 없는 품종입니다.`
          this.$router.push('/404')
          console.log(error)
        })
    }
  },
  // getDohImage 호출
  created() {
    this.getDogImage()
  }
}
</script>

<style>

</style>