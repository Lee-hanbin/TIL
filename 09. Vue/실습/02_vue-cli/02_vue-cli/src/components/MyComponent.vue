<template>
  <!-- div의 border class 생성 -->
  <div class="border">
    <h1>이건 이한빈 MyComponent 다! </h1>
    <!-- 1. 보내라 -->
    <MyComponentItem 
      static-props="MyComponent에서 보낸 데이터"
      :dynamic-props="dynamicProps"
      @child-to-parent = "parentGetEvent"
      @child-input= "getDynamicData"
    />
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'

export default {
  name: 'MyComponent',
  components:{
    // 2. 등록하기
    MyComponentItem,
  },
  // 함수의 return 객체여야함 
  // 이름공간 (스코프) 때문에
  // vue-cli에서 사용
  data: function () {
    return {
      dynamicProps: '이건 동적인 데이터'
    }
  },
  methods: {
    parentGetEvent: function (childData) {
      console.log('자식 컴포넌트에서 발생한 emit 이벤트를 받았다!')
      console.log(childData)
    },
    getDynamicData: function (childInputData) {
      console.log(`사용자가 입력한 값은 ${childInputData}입니다.`)
    }
  }
}
</script>

<style>
  /* border */
  .border {
    border: solid;
  }
</style>