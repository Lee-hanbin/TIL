# Workshop 풀이


## Lunch 컴포넌트 작성
* lodash 를 설치한다.
  `npm install lodash`  
* 기본 동작을 먼저 작성한다.

`components/TheLunch.vue`
```html
<template>
  <div>
    <h1>점심 메뉴</h1>
    <button @click="pickLunchMenu">Pick One</button>
    <p>{{ pickMenu }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data() {
    return {
      lunchList: ['국밥', '짜장면', '햄버거'],
      pickMenu: null,
    }
  },
  methods: {
    pickLunchMenu: function () {
      this.pickMenu = _.sample(this.lunchList)
    }
  }
}
</script>

<style>

</style>
```

## App.vue 에 TheLunch 컴포넌트를 등록한다.
`App.vue`
```html
<template>
  <div id="app">
    <TheLunch />
    <hr>
  </div>
</template>

<script>
import TheLunch from '@/components/TheLunch'

export default {
  name: 'App',
  components: {
    TheLunch,
  },
}
</script>
```


## Lotto 컴포넌트 작성

`componenets/TheLotto.vue`
```html
<template>
  <div>
    <h1>로또</h1>
    <button @click="getLottoNums">Get Lucky Numbers</button>
    <p>{{ lottoNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data() {
    return {
      lottoNums: null,
    }
  },
  methods: {
    getLottoNums: function () {
      const numbers = _.range(1, 46)
      this.lottoNums = _.sampleSize(numbers, 6)
    }
  }
}
</script>

<style>

</style>
```

## App.vue 에 TheLotto 컴포넌트를 추가한다.
`App.vue`
```html
<template>
  <div id="app">
    <TheLunch />
    <hr>
    <TheLotto />
  </div>
</template>

<script>
import TheLunch from '@/components/TheLunch'
import TheLotto from '@/components/TheLotto'

export default {
  name: 'App',
  components: {
    TheLunch,
    TheLotto
  },
}
</script>
```

## TheLotto 컴포넌트에서 App.vue로 점심 메뉴를 emit으로 전달한다.
* pickLunchMenu 메서드에서 emit 부분을 추가한다.
`components/TheLunch.vue`
```html
...
 },
  methods: {
    pickLunchMenu: function () {
      this.pickMenu = _.sample(this.lunchList)
      this.$emit('get-menu', this.pickMenu)
    }
  }
}
```
* App.vue 에서 emit을 받고 data에 저장하는 메서드 getMenu를 작성한다.
* 점심 메뉴가 없으면 Lotto가 출력되지 않도록 v-if 를 추가한다.

`App.vue` 
```html
<template>
  <div id="app">
    <TheLunch @get-menu="getMenu"/>
    <hr>
    <TheLotto v-if="lunchMenu" />
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
```

## App.vue 에서 TheLotto 컴포넌트로 점심메뉴를 전달한다.

* v-bind를 통해 TheLotto 에 점심 메뉴를 전달한다.

`App.vue`
```html
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
```

## TheLotto 컴포넌트에서 전달되는 점심 메뉴 데이터를 prop으로 받아 출력한다.

`componenets/TheLotto.vue`
```html
<template>
  <div>
    <h1>{{ lunchMenu }} 먹고 로또</h1>
    <button @click="getLottoNums">Get Lucky Numbers</button>
    <p>{{ lottoNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data() {
    return {
      lottoNums: null,
    }
  },
  props: {
    lunchMenu: String,
  },
  methods: {
    getLottoNums: function () {
      const numbers = _.range(1, 46)
      this.lottoNums = _.sampleSize(numbers, 6)
    }
  }
}
</script>

<style>

</style>
```