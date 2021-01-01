import markdown
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Article,Category

def global_variable(request):
    categories = Category.objects.all()
    archives = Article.objects.archive()
    return locals()

# all articles
def index(request):
    articles = Article.objects.all().order_by('-date',)
    num = len(articles)
    
    page = request.GET.get('page')
    paginator = Paginator(articles, 10)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request,
                'diary/index.html',
                locals())

def category(request,cid):
    articles = Article.objects.filter(category_id=cid).order_by('-date',)
    num = len(articles)
    category = Category.objects.get(id=cid)

    page = request.GET.get('page')
    paginator = Paginator(articles, 5)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request,
            'diary/category.html',
            locals())

def show(request,sid):
    article = get_object_or_404(Article,pk=sid)
    # markdown.extensions.extra：用于标题、表格、引用这些基本转换
    # markdown.extensions.codehilite：用于语法高亮
    # markdown.extensions.toc：用于生成目录
    article.body = markdown.markdown(article.body,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                ])
    previous_articles = Article.objects.filter(date__lt=article.date,category=article.category)
    if previous_articles:
        previous_article = previous_articles[0]
    next_articles = Article.objects.filter(date__gt=article.date,category=article.category)
    if next_articles:
        next_article = next_articles.last()
    return render(request,
                'diary/show.html',
                locals())

def tag(request,tag):
    tag = Tag.objects.get(name=tag)
    articles = Article.objects.filter(tags__name=tag)
    num = len(articles)

    page = request.GET.get('page')
    paginator = Paginator(articles, 5)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request,
            'diary/tag.html',
            locals())

def archive(request,year,month):
    archive = "%s年%s月" % (year,month)
    articles = Article.objects.filter(date__year=year,date__month=month)
    num = len(articles)

    page = request.GET.get('page')
    paginator = Paginator(articles, 5)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request,
            'diary/archive.html',
            locals())
    

def search(request):
    query = request.GET.get('search')
    articles = Article.objects.filter(Q(body__contains=query) | Q(title__contains=query)) 
    num = len(articles)
    page = request.GET.get('page')
    paginator = Paginator(articles, 5)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request,
            'diary/search.html',
            locals())

