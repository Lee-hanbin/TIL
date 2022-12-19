<template>
  <div id="app">
    <TheLunch @get-menu="getMenu"/>
    <hr>
    <TheLotto v-if="lunchMenu" :lunch-menu="lunchMenu" />
  </div>
</template>

<script>
import TheLunch from '@/components/TheLunch'
import TheLotto from '@/components/TheLotto'

export default {
  name: 'App',
  data() {
    return {
      lunchMenu: null,
    }
  },
  components: {
    TheLunch,
    TheLotto
  },
  methods: {
    getMenu: function (menu) {
      this.lunchMenu = menu
    }
  }
}
</script>


