import './App.css';
import { useState } from 'react'; 


function Header(props){
  console.log('props', props, props.title)
  return <header>
    <h1><a href="/" onClick={(event)=>{
      event.preventDefault();       //reload 방지 (새로고침)
      props.onChangeMode();         //onChangeMode 실행
    }}>{props.title}</a></h1>
  </header>
}

function Nav(props){
  const lst = []
  for (let i=0; i<props.topics.length; i++){
    let t = props.topics[i];
    lst.push(<li key={t.id}>
      <a id={t.id} href={'/read/'+t.id} onClick={(event)=>{
        event.preventDefault();
        props.onChangeMode(Number(event.target.id));
      }}>{t.title}</a>
      </li>)
  }
  return <nav>
    <ol>
      {lst}
    </ol>
  </nav>
}

function Article(props){
  return <article>
    <h2>{props.title}</h2>
    {props.body}
  </article>
}

function Create(props){
  return <article>
    <h2>Create</h2>
    <form onSubmit={(event)=>{
      event.preventDefault();
      const title = event.target.title.value;
      const body = event.target.body.value;
      props.onCreate(title, body)
    }}>
      <p><input type="text" name="title" placeholder='title'/></p>
      <p><textarea name="body" placeholder='body'></textarea></p>
      <p><input type="submit" value="create"/></p>
    </form>
  </article>
}

function Update(props){
  const [title, setTitle] = useState(props.title);    //props의 값은 외부자가 접근 불가능하다.
  const [body, setBody] = useState(props.body);       //따라서 State로 접근하여 내부자로서 데이터에 접근한다.
  return <article>
    <h2>Update</h2>
    <form onSubmit={(event)=> {
      event.preventDefault();
      const title = event.target.title.value;
      const body = event.target.body.value;
      props.onUpdate(title, body);
    }}>
      <p><input type="text" name="title" placeholder='title' value={title} onChange={(event)=>{
        // console.log(event.target.value);
        setTitle(event.target.value);       // 바로 바꿔줌
      }}/></p>
      <p><textarea name="body" placeholder='body' value={body} onChange={(event)=>{
        setBody(event.target.value);
      }}></textarea></p>
      <p><input type="submit" value="Update"></input></p>
    </form>
  </article>
}
function App() {
  // const _mode = useState('WELCOME');
  // const mode = _mode[0];
  // const setMode = _mode[1];
  const [mode, setMode] = useState('WELCOME');  // 위의 세 문장의 축약형
  const [id, setId] = useState(null);
  const [nextId, setNextId] = useState(4);      // 3까지 있으니까, 4부터 시작하게 함
  const [topics, setTopics] = useState([
    {id:1, title:'html', body:'html is ...'},
    {id:2, title:'css', body:'css is ...'},
    {id:3, title:'js', body:'js is ...'}
  ])
  let content = null;
  let contextControl = null;
  if(mode === 'WELCOME'){
    content = <Article title="Welcome" body="Hello, WEB"></Article>
  } else if(mode === 'READ'){
    let title, body = null;
    for(let i=0; i<topics.length; i++){
      // console.log(topics[i].id, id)     // topics[i].id는 숫자고 id는 문자가 찍힘! => Number 이용
      if(topics[i].id === id){
        title = topics[i].title;
        body = topics[i].body;
      }
    }
    content = <Article title={title} body={body}></Article>
    contextControl = <>
      <li><a href={'/update/'+id} onClick={(event)=>{
        event.preventDefault();
        setMode('UPDATE');
      }}>Update</a></li>
      <li><input type="button" value="Delete" onClick={()=>{
        const newTopics = []
        for(let i=0; i<topics.length; i++){
          if(topics[i].id !== id){
            newTopics.push(topics[i]);
          }
        }
        setTopics(newTopics);
        setMode('WELCOME');
      }}/></li>
    </>    // READ로 접근해야만 Update 나오게
  } else if(mode === 'CREATE'){
    content = <Create onCreate={(_title, _body)=>{
      const newTopic = {id:nextId, title:_title, body:_body}
      const newTopics = [...topics]       // 1. 오리지널 데이터를 복제를 하고
      newTopics.push(newTopic);           // 2. 복제한 데이터를 변경하고
      setTopics(newTopics);               // 3. 변경한 데이터를 set한다.
      setMode('READ');
      setId(nextId);
      setNextId(nextId+1);
    }}></Create>
  } else if(mode === 'UPDATE'){
    let title, body = null;
    for(let i=0; i<topics.length; i++){
      if(topics[i].id === id){
        title = topics[i].title;
        body = topics[i].body;
      }
    }
    content = <Update title={title} body={body} onUpdate={(title, body)=> {
      // console.log(title, body);
      const newTopics = [...topics]
      const updatedTopic = {id:id, title:title, body:body}
      for(let i=0; i<newTopics.length; i++){
        if(newTopics[i].id === id){
          newTopics[i] = updatedTopic;
          break;
        }
      }
      setTopics(newTopics);
      setMode('READ');
    }}></Update>
  }
  return (
    <div>
      <Header title="WEB" onChangeMode={()=>{
        setMode('WELCOME');                 // 수정하고 싶으면 setMode를 이용
      }}></Header>
      <Nav topics={topics} onChangeMode={(_id)=>{
        setMode('READ');
        setId(_id);
      }}></Nav>
      {content}
      <ul>
        <li><a href="/create" onClick={(event)=>{
          event.preventDefault();
          setMode('CREATE');
        }}>Create</a></li>
        {contextControl}
      </ul>
    </div>
  );
}

export default App;
