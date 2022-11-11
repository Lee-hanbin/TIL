<template>
  <div>
    <span 
      @click="updateTodoStatus"
      :class="{ 'is-completed': todo.isCompleted }"
    >
      {{ todo.title }}
    </span>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo() {
      this.$store.dispatch('deleteTodo', this.todo)
    },
    updateTodoStatus() {
      this.$store.dispatch('updateTodoStatus', this.todo)
    },
  }
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>
