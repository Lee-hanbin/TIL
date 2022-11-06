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
// 출력
console.log(
isPalindrome('a santa at nasa'), // true
isPalindrome('google') // false
)