const avengers = [
  { name: 'Tony Stark', age: 45},
  { name: 'Steve Rogers', age: 32},
  { name: 'Thor', age: 40},
]

const avenger = avengers.find((avenger) => avenger.name === 'Tony Stark')

console.log(avenger)