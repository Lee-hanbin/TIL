const arr = [1, 2, 3, 4, 5]

//1. 
const result = arr.every(function (elem) {
  return elem % 2 === 0
})

//2.
const result = arr.evrey((elem) => {
  return elem % 2 === 0
})

//3.
const result = arr.evrey((elem) => elem % 2 === 0)