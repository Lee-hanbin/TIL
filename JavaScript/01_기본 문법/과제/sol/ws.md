# ws

# JavaScript 기초

## 1. 주어진 문자열이 회문인지 판하는 isPalindrome함수를 완성

```jsx
function isPalindrome(str) {

}
// 출력
console.log(
isPalindrome(‘a santa at nasa'), // true
isPalindrome('google') // false
)
```

```jsx
//답

function isPalindrome(str) {
  str = str.split(' ')
  const chk = str.join('')
  console.log(chk)
  for ( let i = 0; i < (chk.length-1)/2; i++){
    if (chk[i] != chk[chk.length-1-i]) {
      return false
    }
  }
  return true
}
```