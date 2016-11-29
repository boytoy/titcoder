# -*- coding: utf-8 -*-

from django import forms

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class LoginForm(forms.Form):
	uid = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' ,'id':'uid', 'placeholder': '请输入您的用户名'}))
	pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' ,'id':'pwd', 'placeholder': '请输入你的密码'}))

class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'用户名', 'placeholder': '请输入您的用户名'}))
	pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' ,'id':'密码', 'placeholder': '请输入你的密码'}))
	re_pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' ,'id':'重复密码', 'placeholder': '请重复输入你的密码'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control' ,'id':'电子邮箱', 'placeholder': '请输入你的电子邮箱'}))

class SetInfoForm(forms.Form):
	username = forms.CharField()

class CommentForm(forms.Form):
	comment = forms.CharField(label='', widget=forms.Textarea(attrs={'cols': '60', 'rows': '6'}))

class SearchForm(forms.Form):
	keyword = forms.CharField(widget=forms.TextInput)
