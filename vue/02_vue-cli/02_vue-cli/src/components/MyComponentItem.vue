<template>
  <div>
    <h3>나는 MyComponent의 하위 컴포넌트!</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent">클릭!</button>
    <!---->
    <input 
      type="text"
      v-model="childInputData"
      @keyup.enter="childInput"
    >
  </div>
</template>

<script>
export default {
  name: 'MyComponentItem',
  // 2. 선언
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  data: function () {
    return {
      childInputData: null,
    }
  },
  methods: {
    childToParent: function () {
      this.$emit('child-to-parent', '나는 자식이 보낸 데이터다') // 받는쪽이 html이므로 케밥으로 작성
    },             // 이름             // 데이터
    childInput: function () {
      this.$emit('child-input', this.childInputData)
    }
  },

}
</script>

<style>

</style>