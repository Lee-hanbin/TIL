<template>
  <div id="app">
    <HelloWorld/>
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld'

export default {
  name: 'App',
  data() {
    return {
      message: 'Message'
    }
  },
  components: {
    HelloWorld,
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
