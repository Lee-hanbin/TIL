import { useState } from "react";

export default function Counter({onTotal}) {
  // let counter = 1;
  const [counter, setCounter] = useState(0);

  console.log('Counter');

  const handleCounter = () => {
    // setCounter(counter+1); // 0+1
    // setCounter(counter+1); // 0+1
    // setCounter(counter+1); // 0+1
    //콜백함수를 사용하면 하나의 변수에 여러번 state 변경 가능
    setCounter((prevCounter) => prevCounter+1); // 0+1
    setCounter((prevCounter) => prevCounter+1); // 1+1
    setCounter((prevCounter) => prevCounter+1); // 2+1 => 3으로 리턴
    if(onTotal){
      onTotal();
    }
    // counter++;
    // console.log('counter: ' + counter)
  }
  return (
    <button onClick={handleCounter}>Counter: {counter}</button>
  )
}

