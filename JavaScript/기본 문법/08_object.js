// const myInfo = {
//   name: 'jack',
//   phoneNumber: '123456',
//   'samsung product': {
//     buds: 'Buds pro',
//     galaxy: 'S99',
//   },
// }

// console.log(myInfo.name)        //jack
// console.log(myInfo['name'])     //jack

// console.log(myInfo['samsung product'])      //{ buds: 'Buds pro', galaxy: 'S99' }
// console.log(myInfo['samsung product'].galaxy)  // 599

// const obj = {
//   name: 'jack',
//   greeting(){
//     console.log('hi!')
//   }
// }

// console.log(obj.name)
// console.log(obj.greeting())

// const key = 'country'
// const value = ['한국', '미국', '일본', '중국']

// const myObj = {
//   [key]: value,
// }

// console.log(myObj)
// console.log(myObj.country)

// const userInformation = {
//   name: 'ssafy kim',
//   userId: 'ssafyStudent1234',
//   phoneNumber: '010-1234-1234',
//   email: 'ssafy@ssafy.com',
// }

// const name = userInformation.name
// const userId = userInformation.userId
// const phoneNumber = userInformation.phoneNumber
// const email = userInformation.email

// const {name} = userInformation
// const {userId} = userInformation
// const {phoneNumber} = userInformation
// const {email} = userInformation

const jsonData = {
  coffee: 'Ame',
  iceCream: 'Mint Choco',
}

// Object -> json
const objToJson = JSON.stringify(jsonData)

console.log(objToJson)    // {"coffee":"Ame","iceCream":"Mint Choco"}
console.log(typeof objToJson)   // string

// json -> Object
const jsonToObj = JSON.parse(objToJson)

console.log(jsonToObj)    // {"coffee":"Ame","iceCream":"Mint Choco"}
console.log(typeof jsonToObj)   // object
console.log(jsonToObj.coffee)   // Ame

