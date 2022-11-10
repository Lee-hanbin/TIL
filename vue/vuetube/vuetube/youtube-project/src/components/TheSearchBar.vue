<template>
  <div>
    <input
      type="text"
      v-model="vuetubeInputData"
      @keyup.enter="vuetubInput"    
    >
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'TheSearchBar',
  data: function () {
    return {
      vuetubeInputData: null,
    }
  },
  methods: {
    vuetubInput: function () {
      this.$emit('vue-input', this.vuetubeInputData)
    },
  }
}
</script>

<style>

</style>