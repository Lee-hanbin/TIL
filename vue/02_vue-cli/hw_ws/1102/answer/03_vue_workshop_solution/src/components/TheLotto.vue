<template>
  <div>
    <h1>{{ lunchMenu }} 먹고 로또</h1>
    <button @click="getLottoNums">Get Lucky Numbers</button>
    <p>{{ lottoNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data() {
    return {
      lottoNums: null,
    }
  },
  props: {
    lunchMenu: String,
  },
  methods: {
    getLottoNums: function () {
      const numbers = _.range(1, 46)
      this.lottoNums = _.sampleSize(numbers, 6)
    }
  }
}
</script>

<style>

</style>