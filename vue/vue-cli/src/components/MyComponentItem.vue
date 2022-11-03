<template>
  <div>
    <h3>나는 MyComponent의 하위 컴포넌트!</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
  </div>
</template>

<script>
export default {
  name: 'MyComponentItem',
  // 2. 선언
  props: {
    staticProps: String,
    dynamicProps: String,
  }
}
</script>

<style>

</style>