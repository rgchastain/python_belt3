# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .models import User

def index(request):
	
	return render(request, 'logreg/index.html')

def success(request):
	if 'user_id' in request.session:
		user = User.objects.get(id = request.session['user_id'])
		
		context = {
			'user': user,
		}

		return render(request, 'logreg/success.html', context)
	return redirect(reverse('landing'))
def register(request):
	if request.method == "POST":
		errors = User.objects.validate_registration(request.POST)

	if not errors:
		user = User.objects.create_user(request.POST)

		request.session['user_id'] = user.id
		return redirect(reverse('home'))
	
	for error in errors:
		messages.error(request, error)

	return redirect(reverse('landing'))

def login(request):
	if request.method == "POST":
		result = User.objects.validate_login(request.POST)
		if type(result) == list:
			for error in result:
				messages.error(request, error)
			return redirect('landing')
		request.session['user_id'] = result.id
		
		return redirect('home')


	return redirect(reverse('home'))
def logout(request):
	if 'user_id' in request.session:
		request.session.pop('user_id')

	return redirect(reverse('landing'))



