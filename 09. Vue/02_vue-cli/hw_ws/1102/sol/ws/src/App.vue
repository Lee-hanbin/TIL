<template>
  <div id="app">
    <TheLunch/>
  </div>
</template>

<script>
import TheLunch from '@/components/TheLunch'

export default {
  name: 'App',
  components: {
    TheLunch,
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
