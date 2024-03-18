# 커밋 작성법


[Before read...](https://cbea.ms/git-commit/)

### 1. 기본 7가지 규칙 

1. 제목과 본문을 빈 행으로 구분한다.
2. 제목은 50글자 이내로 제한한다.
3. 제목의 첫 글자는 대문자로 작성한다.
4. 제목 끝에는 마침표를 넣지 않는다.
5. 제목은 명령문으로 사용하며 과거형을 사용하지 않는다.
6. 본문의 각 행은 50글자 내로 제한한다.
7. 어떻게 보다는 무엇과 왜를 설명한다.


<br>

Type | 내용
|---|---|
feat | 새로운 기능에 대한 커밋
fix | build 빌드 관련 파일 수정에 대한 커밋
build | 빌드 관련 파일 수정에 대한 커밋
chore | 그 외 자잘한 수정에 대한 커밋(기타 변경)
ci | CI 관련 설정 수정에 대한 커밋
docs | 문서 수정에 대한 커밋
style | 코드 스타일 혹은 포맷 등에 관한 커밋
refactor | 코드 리팩토링에 대한 커밋
test | 테스트 코드 수정에 대한 커밋
release | 버전 릴리즈 



### 2. 구조

```plain
<type>: <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

< body > : 헤더로 표현이 가능하다면 생략이 가능하다. 아니라면 자세한 내용을 함께 적어 본문을 구성한다. 

< footer > : 어떤 이슈에 대한 commit인지 issue number을 포함한다. 
[이슈링크와 닫는 참조 키워드 ](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue)

### 3. 예시
```
feat: Nav bar 'login' 버튼 기능 추가 

Nav bar에서 login 화면으로 넘어갈 수 있도록 버튼을 추가하였다. 

해결 : close #101
```


### 4. 왜 중요한가?
- 메세지의 형태는 사람마다 다르기 때문에 각 커밋의 위치에서 어떤 작업을 했는지 명확히 알 수 있어야 작업 내용을 추적할 수 있고 움직임을 정확하게 알 수 있다. 
- 과거 코드에 대한 코드 추적이 쉽고 이슈사항을 처리할 수 있다. 
