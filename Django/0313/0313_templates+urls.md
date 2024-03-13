# Templates & URLs



## Template System
데이터로 표현을 제어하면서, 표현과 관련된 부분을 담당한다. 

### Django Template Language (DTL)
1. variable 
- render 함수의 세번째 인자로 딕셔너리 데이터를 사용
- 딕셔너리 key에 해당하는 문자열이 template에서 사용가능한 변수명이 됨
- dot('.')을 사용하여 변수 속성에 접근할 수 있음 
- `{{variable}}` or `{{variable.attribute}}`

2. Filters
- 표시한 변수를 수정할 때 (변수 + '|' + 필터)
- chained이 가능하며 일부 필터는 인자를 받는다.
- 약 60개의 built-in template filters를 제공한다. 

3. Tags
- 반복 또는 논리를 수행하여 제어 흐름을 만든다 
- 일부 태그는 시작과 종료 태그가 필요하다 
- 약 24개의 built-in template tags를 제공한다
- `{% tag %}` or `{% if %} {% endif %}`

4. Comments
- DTL에서의 주석 
- 시작태그와 종료 태그 안에 주석처리를 할 때 사용한다 
- `{# name #}`인데 보통 `{%comment%}  어쩌구저쩌구주석처리할곳   {%endcomment%}`를 쓴다.

### 템플릿 상속
- 만약 모든 템플릿에 bootstrap을 적용하려면 ?
- 페이지의 공통 요소를 포함하고
- 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton'템플릿을 작성하여 상속 구조를 구축한다. 
- blick tag : 하위 템플릿에서 재정의 할 수 있는 블록을 정의한다. 
- extends tag : 자식 템플릿이 부모 템플릿을 확장한다는 것을 알림. 반드시 자식 템플릿 최상단에 작성되어야 한다. 


## HTML form 
- 사용자로부터 할당된 데이터를 서버로 전송하는 것 
- 웹에서 입력하는 것들 

### action과 method
action 
- 입력 데이터가 전송될 URL을 지정
- 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 url로 보내짐

method
- 데이터를 어떤 방식으로 보낼 것인지 정의
- 데이터의 HTTP request methods (Get, Post)를 지정
- 로그인 할 때 get방식으로 하면 url에 아이디가 나오게 된다. 하지만 post는 로그인 할 때 아이디가 url에 노출되지 않는다. 


### Query string parameters
- 사용자의 입력 데이터를 URL주소에 파라미터를 통해 서버로 보내는 방법 
- 문자열은 앰퍼센드('&') 로 연결된 key=value 쌍으로 구성되며, 기본 URL과는 '?'로 구분된다. 


## Django URLs


