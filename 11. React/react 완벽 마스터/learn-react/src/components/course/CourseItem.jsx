
function HeartIconBtn({ onClick, isFavorite = false}) {


    return (
      <button className="btn" onClick={(e) => onClick(e)}>
        <img className="btn__img" src={isFavorite ? "/img/heart-fill-icon.svg" : "/img/heart-icon.svg"} alt="" />
        {/* {isFavorite ? (
          <img className="icon-heart" src="/img/heart-fill-icon.svg" alt="" />
        ) : (
          <img className="icon-heart" src="/img/heart-icon.svg" alt="" />
        )} */}
      </button>
    )

}

function LinkIconBtn({ link }) {
  return (
      <a className="btn" href={link} target="_blank" rel="noreferrer">
        <img className="btn__img" src="/img/link-icon.svg" alt="" />
      </a>    
  )
}

export default function CourseItem({ title, description, thumbnail, isFavorite, link }) {

  function handleFavorite(e) {
    e.stopPropagation(); //버블링으로 인한 부모 핸들러 이벤트 전파 막기
    alert(isFavorite ? '좋아요' : '모르겠어요');
  }

  function handleItemClick(e) {
    open(link, '_blank') //새창에 해당 링크 
  }

  //onClick 대신 onClickCapture를 사용하면 부모 이벤트 먼저 사용됨
  return (
      <article className="course" onClick={handleItemClick}> 
        <img className="course__img" src={thumbnail} alt="강의 이미지" />
        <div className="course__body">
          <div className="course__title">{title}</div>
          <div className="course__description">{description}</div>
        </div>
        <div className="course_icons">
          <HeartIconBtn isFavorite={isFavorite} onClick={handleFavorite}/>
          {link && <LinkIconBtn link={link}/>}
        </div>
      </article>
  );
}

