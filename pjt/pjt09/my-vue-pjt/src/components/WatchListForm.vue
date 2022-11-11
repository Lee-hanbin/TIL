<template>
  <div>
    <input 
      type="text"
      v-model.trim="todoTitle"
    >
    <button @click="createTodo">Add</button>
  </div>
</template>

<script>
export default {
  name:'WatchListForm',
  data() {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo() {
      // console.log(this.todoTitle)
      if (this.todoTitle) {
        this.$store.dispatch('createTodo', this.todoTitle)
      }
      this.todoTitle = null
    }
  }
}
</script>

<style>

</style>
