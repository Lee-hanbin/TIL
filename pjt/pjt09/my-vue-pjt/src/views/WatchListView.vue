<template>
  <div class="text-white">
    <h1>보고시푼 영화 적어바</h1>
    <WatchListForm/>
    <WatchListItem
      v-for="(todo, index) in todos"
      :key="index"
      :todo="todo"
    />
  </div>
</template>

<script>
import WatchListItem from '@/components/WatchListItem'
import WatchListForm from '@/components/WatchListForm'

export default {
  name: "WatchListView",
  components: {
    WatchListItem,
    WatchListForm,
  },
  computed: {
    todos() {
      return this.$store.state.todos
    }
  },
}
</script>

<style>

</style>