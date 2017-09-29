# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..logreg.models import User
from django.shortcuts import render
from django.shortcuts import render, redirect, reverse

def home(request):
	if 'user_id' in request.session:
		user = User.objects.get(id = request.session['user_id'])
		friends = user.friends.all()
		other_users = User.objects.exclude(id__in=friends).exclude(id=user.id)
			# .exclude(id__in=friends).exclude()
		context = {
			'user': user,
			'friends': friends,
			'peeps': other_users
		}
		return render(request, 'friends/home.html', context)
	return redirect(reverse('landing'))

def show(request, id):
	if 'user_id' in request.session:
		friend = User.objects.get(id=id)
		context ={
			'friend': friend,

		}
		return render(request, 'friends/show.html', context)
	return redirect(reverse('landing'))
def add(request, id):
	user = User.objects.get(id = request.session['user_id'])
	friend = User.objects.get(id=id)

	friend.friends.add(user)
	return redirect(reverse('home'))

def remove(request, id):
	user = User.objects.get(id = request.session['user_id'])
	friend = User.objects.get(id=id)

	friend.friends.remove(user)
	return redirect(reverse('home'))