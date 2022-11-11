<template>
  <div>
    <button @click="pickmovie">PICK!</button> <br> <br>
    <div class="d-flex justify-content-center">
      <div v-if="selectMovie" class="card border-light border-opacity-50 mb-3 bg-dark text-white ">
        <img :src='movieImg(selectMovie.poster_path)' class="card-img-top random_img_size" alt="">
        <div class="card-body">
          <h5 class="card-title txt_title">
          {{ selectMovie.title }}
          </h5>
          <!-- <hr>
          <p class="card-text txt_post">
          {{ selectMovie.overview }}
          </p> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: "RandomView",
  data() {
    return {
      selectMovie: null,
    }
  },
  methods: {
    getMovie() {
      this.$store.dispatch('getMovie')
    },
    pickmovie() {
      this.selectMovie = _.sample(this.$store.state.movieList)
    },
    movieImg(img) {
      return `https://image.tmdb.org/t/p/w300/${img}`
    }
  },
  created() {
    this.getMovie()
  },
  computed:{
    movieList(){
      return this.$store.state.movieList
    },
  }

}
</script>

<style>
  .random_img_size{
    width: 253.32px; 
    height: 440px;
  }
</style>