const numbers =[1, 2, 3, 4, 5]

//1.
const doubleEle = function (number) {
  return number * 2
}

const newArry = numbers.map(doubleEle)

console.log(newArry)

//2.
const newArry = numbers.map(function (number) {
  return number * 2
})

//3-1. 
const newArry = numbers.map((numbers) => {
  return number * 2
})

//3-2.
const newArry = numbers.map((numbers) => number * 2)