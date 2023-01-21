/* eslint-disable */    // Lint 끄는 기능

import logo from './logo.svg';
import './App.css';
import { useState } from 'react'

function App() {

  let post = '강남 우동 맛집';      // 자료를 잠깐 저장할 땐 변수
  let [글제목, 글제목변경] = useState(['남자 코트 추천', '강남 우동맛집', '파이썬독학']);
  // let [logo, setLogo] = useState('ReactBlog');
  // let [a, b] = useState('남자 코트 추천');    // a: state에 담은 자료
  //                                            // b: state 변경도와주는 함수
  let [따봉, 따봉변경] = useState([0,0,0]); 
  // let [따봉, 따봉변경] = useState(0); 
  // function 함수(){
  //   console.log(1);
  // }
  let [modal, setModal] = useState(false);
  
  let [idx_num, idx_func] = useState(0);

  let [입력값, 입력값변경] = useState('');

  return (
    <div className="App">
      <div className='black-nav'>
        <h4 style={ {color : 'red', fontSize: '16px'} }>
          'ReactBlog'
        </h4>
      </div>

      <button onClick={ () => {
        let copy = [...글제목];
        copy.sort();
        글제목변경(copy)
      }}>가나다순정렬</button>

      {/* <button onClick={ () => {
        // 글제목[0] = '여자 코트 추천'        
        let copy = [...글제목];
        copy[0] = '여자 코트 추천'
        // 글제목변경(글제목)
        글제목변경(copy)
      }}>글수정</button> */}


      {/* <div className="list">
        <h4>{ 글제목[0] } <span onClick={ () => {
          따봉변경(따봉+1)
        } }>👍</span> { 따봉 } </h4>
        <p>2월 17일 발행</p>
      </div>


      <div className="list">
        <h4>{ 글제목[1] }</h4>
        <p>2월 17일 발행</p>
      </div>
      <div className="list">
        <h4 onClick={() => {
           modal == true ? setModal(false) : setModal(true) 
           }}>{ 글제목[2] }</h4>
        <p>2월 17일 발행</p>
      </div> */}
      
      {
        글제목.map( (article, idx) => {
          return (
          <div className="list" key={idx}>
            <h4 onClick={() => {
              setModal(true);
              idx_func(idx);
            }}>{ article } <span onClick={ (e) => {
              e.stopPropagation();
              let tmp_따봉 = [...따봉];
              tmp_따봉[idx] += 1;
              따봉변경(tmp_따봉)
            } }>👍</span> { 따봉[idx] } </h4>
            <p>2월 17일 발행</p>

            {/* 이렇게 하면 동일한 글도 모두 지워짐 ㅠ */}
            {/* <button onClick={() => {
              let copy = []
              for ( const 글 of 글제목){
                if (article === 글){
                  continue
                } else {
                  copy.push(글)
                }
              }
              글제목변경(copy)
            }}>delete</button> */}

            <button onClick={() => {
              let copy = [...글제목];
              copy.splice(idx, 1);
              글제목변경(copy)
            }}>delete</button>

          </div>
          )
        })
      }
      
      {/* <div className='modal'>
        <h4>제목</h4>
        <p>날짜</p>
        <p>상세내용</p>
      </div> */}
      {/* 위의 modal을 component 문법으로 만들기!*/}
      
      {/* {}는 html 코드를 작성하는 영역이므로 if문을 사용 x => 삼항연상자 사용
          삼항연산자 => ' 조건식 ? 참일때 실행할 코드 : 거짓일 때 실행할 코드 '
      */}
      {
        modal == true ? <Modal color={'blue'} 글제목={글제목} 글제목변경={글제목변경} idx_num={idx_num}/> : null
      }
      {/* <Modal/> */}
      
      {/* input 이해하기 */}
      {/* <input type="text"/>
      <input type="range"/>
      <input type="checkbox"/>
      <select/>
      <textarea/> */}
      {/* <input onChange={() => {} }/>
      <input onInput={ () => {} }/>
      <input onMouseOver={() => {} }/>
      <input onScroll={() => {}}/> */}

      <input onChange={(e) => { 
        입력값변경(e.target.value );
      }}/>
      <button onClick={() =>{
        let tmp_글제목 = [...글제목];
        tmp_글제목.unshift(입력값);   // 제일 앞에 추가
        // tmp_글제목.push(입력값);   // 제일 뒤에 추가
        글제목변경(tmp_글제목);
      }}>글 발행</button>
    </div>
  );
}

// Modal을 component 문법으로 만든거임! 하나의 태그만 써야함을 인지
// div하나에 두개의 div를 넣어도 됨
// 필요없이 div를 쓰고 싶지 않고 묶기는 해야하면 <> </> 를 이용하자
function Modal(props){
  return (
      <div className='modal' style={{ background : props.color }}>
        <h4>{props.글제목[props.idx_num]}</h4>
        <p>날짜</p>
        <p>상세내용</p>
        <button onClick={ () => {
          let tmp_글제목 = [...props.글제목]
          tmp_글제목[props.idx_num] = '여자 코트 추천'
          props.글제목변경(tmp_글제목)
        }} >글수정</button>
      </div>
  )
}


export default App;
