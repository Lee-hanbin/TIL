<template>
  <div class="col">
    <div class="card border-light border-opacity-50 mb-3 bg-dark text-white img_size">
      <img :src='movieImg(movieProps.poster_path)' class="card-img-top" alt="">
      <div class="card-body">
        <h5 class="card-title txt_title">
        {{ movieProps.title }}
        </h5>
        <p class="card-text txt_post">
        {{ movieProps.overview }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movieProps : Object,
  },
  methods: {
    movieImg(img) {
      return `https://image.tmdb.org/t/p/w300/${img}`
    }
  }
}

</script>

<style>
  .txt_post{
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3; /* 라인수 */
    -webkit-box-orient: vertical;
    word-wrap:break-word; 
    line-height: 1.2em;
    height: 3.6em; /* line-height 가 1.2em 이고 3라인을 자르기 때문에 height는 1.2em * 3 = 3.6em */
  }
  .txt_title{
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 1; /* 라인수 */
    -webkit-box-orient: vertical;
    word-wrap:break-word; 
    line-height: 1.2em;
    height: 1.2em; /* line-height 가 1.2em 이고 3라인을 자르기 때문에 height는 1.2em * 3 = 3.6em */
  }
  .img_size{
    width: 253.32px; 
    height: 510.18px;
  }
</style>