// console.log('hello, javascript');

// function add(num1, num2) {
//   return num1 + num2
// }

// console.log(add(2,7))

// const sub = function (num1, num2) {
//   return num1 - num2
// }

// console.log(sub(2, 7))

// const greeting = function (name = 'Anoymous'){
//   return `hi ${name}`
// }

// console.log(greeting())

// const noArgs = function(){
//   return 0
// }

// console.log(noArgs(1, 2, 3))    // 0
// console.log(noArgs(1, 2, 3, 4))  // 0

// const twoArgs = function(ar1, ar2){
//   return [ar1, ar2]
// }
// console.log(twoArgs(1, 2, 3))  // [1, 2]
// console.log(twoArgs(1))  // [1, undefined]

// let parts = ['so', 'ke']
// let lyrics = [ 'as', ...parts, 'fd', 'gh']
// console.log(lyrics)     //[ 'as', 'so', 'ke', 'fd', 'gh' ]

// const f = function (a, b, ...theArgs){
//   return [a, b, theArgs]
// }

// console.log(f(1, 2, 3, 4, 5)) // [ 1, 2, [ 3, 4, 5 ] ]
// console.log(f(1, 2))          // [ 1, 2, [] ]

// console.log(add(2,7))  // 9

// function add(num1, num2) {
// 	return num1 + num2
// }

// console.log(sub(2,7))  
// // ReferenceError: Cannot access 'sub' before initialization
// const sub = function (num1, num2) {
// 	return num1 + num2
// }

// const greeting = function (name){
//   return `hi ${name}`
// }

// // 1단계
// const greeting = (name) => {
//   return `hi ${name}`
// }

// // 2단계
// const greeting = name => {
//   return `hi ${name}`
// }

// // 3단계
// const greeting = name => `hi ${name}`
// 3단계도 () 있는 것을 강조
// const greeting = (name)=> `hi ${name}`

// //1. 인자가 없다면? () or _로 표시 가능
// let noArgs = () => 'No args'
// noArgs = _ => 'No args'

// //2-1 object 를 return 하면
// let returnObject = () => { return { key: 'value'} } //return을 명시적으로 적어줌

// //2-2 return 을 적지 않으려면 괄호를 붙여야 함
// returnObject = () => ({ key: 'value'})

// (function(num) { return num ** 3})(2)  //6

// (num => num **3)(2) //8


// const numbers = [1, 2, 3, 4, 5]
// // console.log(numbers[0])         //1
// // console.log(numbers[-1])        //undefined
// // console.log(numbers.length)     //5
// // console.log(numbers[numbers.length-1]) //5
// let result

// result = numbers.join()
// console.log(result)     //1,2,3,4,5

// result = numbers.join('')
// console.log(result)     //12345

// result = numbers.join(' ')
// console.log(result)     //1 2 3 4 5

// result = numbers.join('-')
// console.log(result)     //1-2-3-4-5


