<template>
  <div>
    <h1>점심 메뉴</h1>
    <button @click="randomMenu">Pick One</button><br>
    {{menu}}
    <hr>
    <TheLotto v-if="menu"
      :menu-props= menu
    />
  </div>
</template>

<script>
import TheLotto from '@/components/TheLotto'
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data () {
    return {
      menu: null
    }
  },
  components: {
    TheLotto,
  },
  props: {
    
  },
  methods: {
    randomMenu () {
      const menuList = ['국밥', '짜장면', '햄버거'] 
      this.menu = _.sample(menuList)
    }
  }
}
</script>

<style>

</style>