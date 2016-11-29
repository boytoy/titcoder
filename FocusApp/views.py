from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment, ThumbUp, Category, Author
from CourseApp.models import User
from .forms import CommentForm, LoginForm, RegisterForm, SetInfoForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.conf.urls import url

import markdown2, urlparse

def Index(request):
	latest_article_list = Article.objects.query_by_time()
	loginform = LoginForm()
	context = {'latest_article_list': latest_article_list, 'loginform':loginform}
	return render(request, 'news.html', context)

def News(request, article_id):
	article = get_object_or_404(Article, id=article_id)
	content = markdown2.markdown(article.content, extras=["code-friendly",
		"fenced-code-blocks", "header-ids", "toc", "metadata"])
	commentform = CommentForm()
	loginform = LoginForm()
	comments = article.comment_set.all

	return render(request, 'article.html', {
		'article': article,
		'loginform':loginform,
		'commentform':commentform,
		'content': content,
		'comments': comments
	})

def Register(request):
	error1 = "this name is already exist"
	valid = "this name is valid"

	if request.method == 'GET':
		form = RegisterForm()
		return render(request, 'register.html', {'form': form})
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if request.POST.get('raw_username', 'erjgiqfv240hqp5668ej23foi') != 'erjgiqfv240hqp5668ej23foi':
			try:
				user = User.objects.get(username=request.POST.get('raw_username',''))
			except ObjectDoesNotExist:
				return render(request, 'register.html', {'form': form, 'msg': valid})
			else:
				return render(request, 'register.html', {'form': form, 'msg': error1})
		else:
			if form.is_valid():
				username = form.cleaned_data['username']
				email = form.cleaned_data['email']
				password1 = form.cleaned_data['password1']
				password2 = form.cleaned_data['password2']
				if password1 != password2:
					return render(request, 'register.html', {'form': form, 'msg': 'two password is not equal'})
				else:
					user = User(username=username, email=email, password=password1)
					user.save()
					return redirect('/news/login')
			else:
				return render(request, 'register.html', {'form', form})

@login_required
def Collect_Article(request, article_id):
	logged_user = request.user
	article = Article.objects.get(id=article_id)
	articles = logged_user.article_set.all()
	if article not in articles:
		article.user.add(logged_user)
		article.keep_num += 1
		article.save()

		return redirect('/news/')
	else:
		url = urlparse.urljoin('/news/'+{article_id}, article_id)
		return redirect(url)

def Comment_Article(request, article_id):
	form  = CommentForm(request.POST)
	url = urlparse.urljoin('/news/', article_id)
	if form.is_valid():
		user = request.user
		article = Article.objects.get(id=article_id)
		new_comment = form.cleaned_data['comment']
		c = Comment(content=new_comment, article_id=article_id)
		c.user = user
		c.save()
		article.comment_num += 1
	return redirect(url)

def ThumbUp_Article(request, article_id):
	logged_user = request.user
	article = Article.objects.get(id=article_id)
	thumbup_num = logged_user.thumbup_set.all()
	articles = []
	for thumbup in thumbup_num:
		articles.append(thumbup.article)

	if article in articles:
		url = urlparse.urljoin('/news/'+{article_id}, article_id)
		return redirect(url)
	else:
		article.thumbup_num += 1
		article.save()
		thumbup_num = ThumbUp(user=logged_user, article=article)
		thumbup_num.save()
		data = {}
		return redirect('/news/')

def Log_In(request):
	if request.method == 'GET':
		form = LoginForm()
		return render(request, 'login.html', {'form': form})
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['uid']
			password = form.cleaned_data['pwd']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				url = request.POST.get('source_url','/news')
				return redirect(url)
			else:
				return render(request,'login.html', {'form':form, 'error': "password or username is not ture!"})
		else:
			return render(request, 'login.html', {'form': form})

@login_required
def Log_Out(request):
	url = request.POST.get('source_url', '/news/')
	logout(request)
	return redirect(url)
