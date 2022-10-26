// 1.
const colors = ['red', 'blue', 'green']

const printClr = function (color) {
  console.log(color)
}

colors.forEach(printClr)


// 2. 
colors.forEach(function (color){
  console.log(color)
})

// 3-1.
colors.forEach((color) => {
  console.log(color)
})

// 3-2
color.forEach((color) => console.log(color))