### 1. 히스토리 보는 법

- git log --oneline
  
  - 이동하고 싶은 커밋의 아이디를 가져옴

- git reset --hard {커밋 아이디}
  
  ---
  
  어떻게 돌아오냐?

- git reflog를 통해 가장 최근 커밋의 아이디 확인

- git reset --hard {커밋 아이디}

### 2. 이전버전 파일 긁어오기

git clone

git reset --hard 3bad

---

templates space 는 index내의 url 이름을 바꿔주는 게 아니라 views의 함수만 바꿔준다.

이 경우 다른 html에서 index를 찾을 때 pages/index로 간다

=> 위에서 아래로 훑으면서 실행시켜주기 때문에

---

### 3. 하위 폴더만 clone 하기

- git 활성화
  
  `git init`

- git 저장소 연결
  
  `git remote add origin {repo주소}`

- sparse Checkout 기능 활성화
  
  `git config core.sparseCheckout true`

- clone하기 위한 git 저장소 연결
  
  `echo {프로젝트 경로} >> .git/info/sparse-checkout`
  
  ex) pjt repo에서 frontend 폴더만 다운받고 싶으면
  
  => `echo frontend/* >> .git/info/sparse-checkout`

- pull 명령어로 해당 폴더 다운받기
  
  `git pull origin {브랜치명}`
  
  => `git remote -v` 으로 git 저장소를 확인
