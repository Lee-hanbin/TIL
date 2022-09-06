from django.shortcuts import render, redirect
# 데코레이터 추가
from django.views.decorators.http import require_safe
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST
from .models import Article
# 명시적 상대경로
from .forms import ArticleForm

# Create your views here.
@require_safe       # GET인 요청에 대해서만 view 함수 사용. 아니면 405응답코드 반환
def index(request): # 404는 클라이언트의 잘못 405는 서버의 잘못
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

#GET
# def new(request):
#     form = ArticleForm()                        # 폼생성
#     context = {
#         'form':form,
#     }
#     return render(request, 'articles/new.html',context)

#POST
@require_http_methods(['GET', 'POST'])
def create(request):
    #new를 넣기
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        if form.is_valid():                     # 이걸로 유효성검사 끝
            article = form.save()               # 새 글을 썼으니 form.save()은 반환값
            return redirect('articles:detail', article.pk)
    else:
        #new
        form = ArticleForm()                        # 폼생성
    context = {
        'form':form,
    }
    # 이 렌더링도 new에서 create로 바꿔줘
    return render(request, 'articles/create.html',context)


    # form = ArticleForm(request.POST)
    # if form.is_valid():                     # 이걸로 유효성검사 끝
    #     article = form.save()               # 새 글을 썼으니 form.save()은 반환값
    #     return redirect('articles:detail', article.pk)
    # # print(f'에러: {form.errors}')
    # context = {
    #     'form': form,
    # }
    # # return redirect('articles:new')
    # return render(request, 'articles/new.html', context)
    
    
    # 사용자의 데이터를 받아서
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    # article = Article(title=title, content=content)
    # article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/index.html')
    # return redirect('/articles/')
    # return redirect('articles:index')
    # return redirect('articles:detail', article.pk)

@require_safe 
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    # if request.method == 'POST':          # 무조건 POST만 들어오므로
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article) # 여기서 instance 안 쓰면 
#     context = {                          # EDIT 페이지에 기존 데이터 값 안 나옴
#         'article': article,              # 수정은 됨
#         'form':form,
#     }
#     return render(request, 'articles/edit.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)            # 공통이니까 위로 뺌
    if request.method == 'POST':
        # article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        # article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article) # 여기서 instance 안 쓰면 
    context = {                          # EDIT 페이지에 기존 데이터 값 안 나옴
        'article': article,              # 수정은 됨
        'form':form,
    }
    return render(request, 'articles/update.html', context)



    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)