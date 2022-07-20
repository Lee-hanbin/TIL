### 초기 설정

- 깃허브 유저네임, 이메일로 아래 설정
  
  - git config --global user.name {user name}
  
  - git config --global user.email {user email}

- 깃랩 유저네임, 이메일로 repo마다 아래 설정
  
  - git config --local user.name {user name}
  
  - git config --local user.email {user email}

### 명령어

- git init
  
  - git repository로 만듦

- git add {filename}
  
  - staging area에 파일 추가
  
  - git add .
    
    - 해당 폴더 내 모든 파일 staging area에 추가

- git commit -m 'commit message'
  
  - 커밋 메시지와 함께 버전 기록을 남김

- git status
  
  - git으로 관리되는 파일들의 상태 확인

- git log
  
  - 커밋 기록 확인
  
  - git log --oneline
    
    - 한줄로 확인

cf. `.gitignore`

    커밋을 남기기 전에 추가. 

    `gitignore.io` 에 운영체제, 언어 등 추가하여 복붙하여 사용.

### 원격 저장소

- git remote add origin {git repo url}
  
  - origin이라는 별명에 원격 저장소 url 추가

- git push origin master
  
  - master branch를 origin(위에 추가한 git repo)에 추가
  
  - git push -u origin master
    
    - push의 기본값으로 origin, master를 추가

### clone, pull

- git clone {url}
  
  - git repo를 repo 이름 폴더를 만들어 복사
  
  - git clone {url} .
    
    - 해당 폴더에 git repo 복사

- git pull
  
  - git repo의 커밋을 local로 다운로드





### 흐름

- git init

- git remote add origin {github repo url}

- .gitignore 추가

- 변경사항 발생 (파일 생성, 수정 등)

- 아래 반복
  
  - git add .
  
  - git commit -m 'message'

- 
  
  - 최초 1회는 git push -u origin master

- git push origin master
  
  - 최초 1회는 git push -u origin master
