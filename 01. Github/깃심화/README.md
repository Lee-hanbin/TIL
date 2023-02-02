# Git 심화

- 목차

1. .gitignore에 없는 것들이 working directory로 들어감
2. add : working directory ⇒ staging area
3. commit : staging area ⇒ commits
4. push : commit ⇒ github

## Un doing

### `restore`

1. 이미 commit을 한 상태
2. 파일을 수정
3. 파일을 다시 commit을 했을 때 상태로 돌리고 싶음
    
    ⇒ `git restore .`
    

### `restore --staged`

1. 두 개의 파일을 수정
2. 두 개의 파일을 한 번에 add
3. 그런데 나는 각각의 파일을 따로 commit 해주고 싶어
4. 그럼 먼저 commit 할 파일은 납두고
5. 나중에 commit할 파일은 restore해줌
    
    ⇒ `git restore --staged b.py`
    
    (a파일 b파일이 있는데 b파일은 나중에 commit)
    

### `rm --cached`

1. 파일을 add 함
2. git이 해당  a 파일을 관여하지 않았ㅇ라         으면 좋겠음 (인식은 하지만)
    
    ⇒ `git rm --cached a.py`
    
3. 만약, 인식조차 하지 않았으면 좋겠으면 `.gitignore`로 추가
4. 하지만 이미 관리가 시작된 파일은 중간에 ignore 하더라도 계속 인식함

### `commit --amend`

```jsx
i 누르면 => 끼워넣기(insert) 생김 => 수정가능상태
수정완료 => esc => :wq => 저장하고 나가짐
(만약, 수정하고 :q! 하면 저장 안하고 나가는 거)
(만약, 수정 안하고 나가려면 :q 만 눌러도 됨)
```

- (커밋 뿐만 아니라 파일 내용 수정도 가능하다)

![Image Pasted at 2022-10-28 10-28.png](Git%20%E1%84%89%E1%85%B5%E1%86%B7%E1%84%92%E1%85%AA%20403dd41530c14011bfac5cfc0dc8933b/Image_Pasted_at_2022-10-28_10-28.png)

### `git reset --hard`

1. git log --oneline
2. `git reset --hard {커밋 id}`

 ⇒ 해당 커밋을 남겼을 때로 돌아감

```jsx
hard는 working directory와 staging area 뿐만 아니라 commit 또한 과거 상태로 돌아감
=> working directory의 파일들이 모두사라짐
=> git reflog + reset으로 돌아갈 수 있음
soft는 working directory과 staging area는 최신이고, commit만 과거로 돌아감
mixed는 파일은 working directory만 최신
```

=> 과거로 돌아와서 새로운 commit을 남기면 이전에 있었던 길들은 모두 사라짐
=> `협업 과정 중에는 하지말자!!!`

### `git reflog`

1. 여태까지 수정 내용(커밋 id) 다 보여줌

### `git revert`

1. 작업을 하고 commit을 남김
2. 잘못된 길을 갔음을 이해하고 돌아가고 싶음 단, 기록은 남기고 싶어
3. `git revert {지우려는 커밋 id}`

+중간에 있는 작업만 취소 할 수 도 있음!!

+ revert를 revert하면 취소했던 것을 다시 취소!

+`git revert {시작 커밋 id}..{끝 커밋 id}`

   ⇒ 구간을 revert할 수 있음

---

# git branch

```jsx
마스터에는 조심스럽게 push merge

협업시 내 develop이라는 branch에 쌓아야함

git fork를 이용하면 branch들을 관리하기 더 용이!
```

`git branch {브랜치 이름}` : 새로운 브랜치 생성

`git branch` : 브랜치 목록확인

`git switch new` : 해당 브랜치로 바꾸기

`git log --oneline --all --graph` : 브랜치의 전체적인 형태를 시각적으로 보여줌 

`git branch -d {브랜치 이름}` : 브랜치 지우기

`git merge {브랜치 이름}` : 현재 있는 브랜치에다 {브랜치 이름} 브랜치를 병합

1. 브랜치 만들고
2. 브랜치 바꾸고
3. 커밋 남기고
4. 합병 하고

```jsx
// 깃이 merge하는 과정에서 conflict가 생기면
// add . => commit 남기면 합병 완료
```

---

# Git Workflow

- 하나의 레포를 공유
- merge하기 전에 pull request 과정 (시니어에게 주니어가 검사받음)
- master branch에 직접 개발하는 것이 아니라, 기능별 branch를 따로 만들어 개발
- git branch로 branch 생성
- git switch로 branch 변경
- add ⇒ commit ⇒ push ⇒ pullrequest

---

git init (M)

Vue create (M)

git switch - a

작업

push origin T

web merge

⇒ 

master pull

branch switch -b

npm i

작업

push origin 

web merge