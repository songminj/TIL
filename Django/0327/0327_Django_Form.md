# Django Form

## Django Form
HTML Form 
- 사용자로부터 데이터를 받기 위해 활용한 방법
- 비정상적인, 악의적인 요청을필터링 할 수 없음
> 유효한 데이터인지에 대한 확인이 필요 

유효성 검사 구현 
- 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 한다. 
- 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용

### Form Class
- 사용자 입력 데이터를 수집하고 처리 및 유효성 검사를 수행하기 위한 도구 
- 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공
- models.py랑 비슷하게 생김. 
- form 을 class 형태로 받겠다. 라는 의미
- form field 에는 TextField()가 없다. 
- Model Field에는 CharField()안에 max_length가 필수인자였는데 Form Field에는 max_length가 필수가 아니다!!

```python
# articles/forms.py
from django import forms 

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()

```

### form rendering options 

```plain
form.as_p 
form.as_ul
form.as_div
form.as_ul
```
form 태그를 달아준다. 

### [Widgets](https://docs.djangoproject.com/en/5.0/ref/forms/widgets/)
- HTML 'input'element의 '표현'을 담당한다.
- widget은 단순히 input요소의 속성 및 출력되는 부분을 변경하는 것이다. 


## Django Model Form

목적을 나눠서 form을 사용해야 한다! 
Form : 사용자 입력 데이터를 DB에 저장하지 않을 때(ex : 로그인)
ModelForm : 사용자 입력 데이터를 DB에 저장해야 할 때 (ex : 게시글 작성, 회원가입)

```python 
# articles/forms.py
from django import forms 
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    class Meta:
        # 어떤 모델과 연동할 것인지?
        model = Article 
        # 그 모델에서 어떤 필드를 쓸지?
        fields = '__all__' 
        

```
### Meta class
- Model Form의 정보를 작성하는 곳


### is_valid()

- 여러 유효성 검사를 실행하고, 데이터가유효한지 여부를 Boolean으로 반환한다.

공백 데이터가 유효하지 않은 이유와 에러메세지가 출력되는 과정
1. 별도로 명시하지 않았지만 모델 필드에는 기본적으로 빈 값은 허용하지 않는 제약조건이 설정되어있음 (HTML)
2. 빈 값은 is_valid()에 의해 False 로 평가되고 form객체에는 그에 맞는 에러 메세지가 포함되어 다음 코드로 진행됨. 

### UPDATE와 CREATE의 차이
CREATE
```python
def create(request):
    form = ArticleForm(request.POST)
    # 유효성 검사 .is_valid()
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    # 에러 메세지를 반환한다
    context = {
        'form': form,
    }
    # return redirect('articles:new')
    return render(request, 'articles/new.html', context)
```


UPDATE
```python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)

    context = {
        'form' : form,
    }
    return render(request, 'articles/edit.html', context)

```
form에 instance = article을 넣는 것이 차이이다. 


## Handling HTTP requests

### NEW와 CREATE의 차이 

두 함수를 결합한 코드
```python
# articles/views.py 

def create(request):
    # 유효성 검사 .is_valid()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:   # Post가 아닌 다른 모든 경우 
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/new.html', context)
"""
else... 
Post와 그 외의 경우를 걸러내기위해서 method==POST를 먼저 보는 것이다 .

"""

```


