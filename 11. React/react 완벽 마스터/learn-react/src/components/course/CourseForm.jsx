import { useState } from "react";
import Card from "../Card";

export default function CourseForm() {

  const [form, setForm] = useState({
    title: '리엑트 강의',
    description: '리엑트 기초부터 실전까지!'
  })
  
  function handleCourseForm(e) {
    e.preventDefault();
  }
  
  // const handleTitleChange = (e) => {
  //   setForm({
  //     // description: form.description,
  //     ...form,
  //     title: e.target.value
  //   })
  // }

  // const handleDescriptionChange = (e) => {
  //   setForm({
  //     ...form,
  //     description: e.target.value
  //   })
  // }

  // []를 사용하여 객체 정의 안에 사용하여 동적 이름을 가진 프로퍼티 명시 가능.
  const handleChange = (e) => {
    console.log('e.target.name:', e.target.name)
     setForm({
       ...form,
       [e.target.name]: e.target.value
     })
  }

  return (

    <Card title="강의 등록">
      <form style={{ display: 'flex', flexDirection: 'column', gap: '1rem'}} onSubmit={handleCourseForm}>
        <input name="title" type="text" placeholder="강의 제목" value={form.title} onChange={handleChange} />
        <input name="description" type="text" placeholder="강의 한줄 설명" value={form.description} onChange={handleChange} />
        <input type="submit" value="등록"/>
        {(form.title || form.description) && (
          <div style={{marginTop: '16px', padding: '16px', backgroundColor: '#eee', borderRadius: '6px'}}>
            {form.title && (<p> 제목 - {form.title} </p>)}
            {form.description && (<p> 설명 - {form.description} </p>)}
          </div>
        )}

      </form>
    </Card>
  )
}