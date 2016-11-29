# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Comment, ThumbUp, User, Category, Author
from .forms import CommentForm, LoginForm, RegisterForm, SetInfoForm, SearchForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.cache import cache_page
from django.core.urlresolvers import reverse
from django.conf.urls import url
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .utils import permission_check
from django.contrib import auth
from django.contrib.auth.models import User

import markdown2, urlparse

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def Index(request):
	return render(request, 'index.html')

def CourseView(request):
	latest_course_list = Course.objects.query_by_time()
	loginform = LoginForm()
	context = {'latest_course_list': latest_course_list, 'loginform': loginform}
	return render(request, 'course.html', context)

def CoursePage(request, course_id):
	course = get_object_or_404(Course, id=course_id)
	loginform = LoginForm()

	return render(request, 'course_page.html', {
		'course': course,
		'loginform':loginform,
	})

def Register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('homepage'))
	state = None
	if request.method == 'POST':
		password = request.POST.get('password', '')
		repeat_password = request.POST.get('repeat_password', '')
		if password == '' or repeat_password == '':
			state = 'empty'
		elif password != repeat_password:
			state = 'repeat_error'
		else:
			username = request.POST.get('username', '')
			if User.objects.filter(username=username):
				state = 'user_exist'
			else:
				new_user = User.objects.create_user(username=username, password=password, email=request.POST.get('email', ''))
				new_user.save()
				state = 'success'
	content = {
		'active_menu': 'homepage',
		'state': state,
		'user': None,
	}
	return render(request, 'register.html', content)

def ThumbUp_Course(request, course_id):
	logged_user = request_user
	course = Course.objects.get(id=course_id)
	thumbup_num = logged_user.thumbup_set.all()
	courses = []
	for thumbup in thumbups:
		courses.append(thumbup.course)

	if course in courses:
		url = urlparse.urljoin('/CourseApp/', course_id)
		return redirect(url)
	else:
		course.thumbup += 1
		course.save()
		thumbup_num = ThumbUp(user=logged_user, course=course)
		thumbup_num.save()
		data = {}
		return redirect('/CourseApp/')

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
				url = request.POST.get('source_url','/')
				return redirect(url)
			else:
				return render(request,'login.html', {'form':form, 'error': "password or username is not ture!"})
		else:
			return render(request, 'login.html', {'form': form})

@login_required
def Log_Out(request):
	url = request.POST.get('source_url', '/')
	logout(request)
	return redirect(url)
