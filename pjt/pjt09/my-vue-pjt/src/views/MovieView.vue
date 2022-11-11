<template>
  <div class="container">
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <MovieCard
        v-for="movie in movieList" :key="movie.id"
        :movie-props="movie"
      />
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import MovieCard from '@/components/MovieCard'
export default {
  name: "MovieView",
  components:{
    MovieCard,
  },
  methods: {
    getMovie() {
      this.$store.dispatch('getMovie')
    }
  },
  created() {
    this.getMovie()
  },
  computed:{
    movieList(){
      return this.$store.state.movieList
    }
  }
}
</script>

<style>

</style>