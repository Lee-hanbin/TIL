<template>
  <div>
    <h1>{{ menuProps }} 먹고 로또</h1>
    <button @click="getLotto">Get Lucky Numbers</button>
    <br>
    {{ nums }}
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data () {
    return {
      nums: [],
    }
  },
  props: {
    menuProps: String
  },
  methods: {
    getLotto () {
      const numbering = _.range(1,46)
      this.nums = _.sampleSize(numbering, 6)
    }
  }
}
</script>

<style>

</style>