# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# here
from .models import *
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import stripe
stripe.api_key = "sk_test_gY7fgCe8R3vMLA63YqYpSYIp"

REGEX_email=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
	if Coder.objects.all().count() == 0:
		Coder.objects.create(first_name = 'Tang', alias = '年轻的妈妈抱着一个孩子', desc = " 这位女士喜欢说话，她能一直喋喋不休，并且她永远不会累，她能对着你说单口相声说100年。This lady has super power, she can talk over and over agian, and she never feel tired during talking, she can talk to you for a whole life", email = 'tang@mail.com', age = 54, url_img = " {% static 'singleproject/img/j0.jpg' %} ")
		Coder.objects.create(first_name = 'Pikaqiu', alias = '超级皮卡丘', desc = "Greetings. More important than engaging in the social convention of sharing my given name, is the fact that I have an IQ of 182. I am eager to find something that occupies my time. Also, Mom doesn’.", email = 'insideisbetterthanoutside@gmail.com', age = 10, url_img = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png")
		Coder.objects.create(first_name = 'tingting', alias = '自拍的婷婷', desc = "你好，这位是喜欢自拍的美女婷婷，她有1000张自拍。Hello! My name is tingting, I like to take self picture, this is just one of thousands of them", email = 'dmitrycodingmaster@gmail.com', age = 24, url_img = "https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/26113713_1831252583611365_6238185155745456642_n.jpg?oh=6d26674adfd2abe56148f4ad3877c380&oe=5AFAB95A")

	
	return render(request,'singleproject/index.html')

def order(request):
	try:
		request.session['id']
	except:
		return redirect('/')

	context = {
		'coders'    : Coder.objects.all()[:3] # ONLY 3 CODERS
	}
	return render(request, 'singleproject/order.html', context)

def dashboard(request, user_id):
	try:
		request.session['id']
	except:
		return redirect('/')
	the_user = User.objects.get(id=request.session['id'])
	if request.session['id'] != int(user_id) and not the_user.admin:
		return redirect('/dashboard/'+str(request.session['id']))
	context = {
	        'all_orders'   : Order.objects.filter(user=user_id),
	        'user'          : User.objects.get(id=user_id)
	}
	return render(request, 'singleproject/dashboard.html', context)

def register(request):
	if 'id' in request.session:
		return redirect('/dashboard/{}'.format(request.session['id']))
	return render(request, 'singleproject/register.html')

def process(request, action):
	if request.method == 'POST':
		if action == 'add':
			check_submission = User.objects.validateRegistration(request.POST)
			if len(check_submission) > 0:
				for message in check_submission['error']:
					messages.error(request, message)
				return redirect('/register')
			else:
				newuser = User.objects.addUser(request.POST)
				if User.objects.all().count() == 1:
					user_admin = User.objects.first()
					user_admin.admin = True
					user_admin.save()
				print newuser
				request.session['id'] = newuser.id
				return redirect('/dashboard/'+str(request.session['id']))
		elif action == 'login':
			if len(request.POST['user_input']) < 1 or len(request.POST['password']) < 8:
				messages.warning(request, 'Invalid login information')
				return redirect('/')
			user_id = User.objects.validateLogin(request.POST)
			if user_id:
				request.session['id'] = user_id
				return redirect('/dashboard/'+str(request.session['id']))
			else:
				messages.warning(request, 'Invalid login information')
				return redirect('/')
			return redirect('/')
	else:
		print 'get out of the main process'
		return redirect('/')

def checkout(request):
	try:
		request.session['id']
	except:
		return redirect('/')

	request.session['cart'] = {
	        'coder'     : request.POST['coder'],
	        'exam'      : request.POST['exam_subject'],
	        'date'      : request.POST['date']
	}
	return render(request, 'singleproject/checkout_official.html', {'coder_name' : Coder.objects.get(id=request.POST['coder'])})

def charge(request):
	token = request.POST['stripeToken']
	print token
	charge = stripe.Charge.create(amount=108,currency="usd",description="jason Test charge",source=token,)

	cart = request.session['cart']
	user_id = request.session['id']
	neworder = Order.objects.addOrder(cart, user_id)
	return redirect('/dashboard/'+str(request.session['id']))


def admin_users(request):
    try:
        request.session['id']
    except:
        return redirect('/')
    checkuser = User.objects.get(id = request.session['id'])
    if not checkuser.admin:
        return redirect('/dashboard/'+str(request.session['id']))

    context = {
        'user' : User.objects.get(id=request.session['id']),
        'all_users' : User.objects.all()
    }
    return render(request, 'singleproject/admin_home.html', context)

def admin_coders(request):
    try:
        request.session['id']
    except:
        return redirect('/')
    checkuser = User.objects.get(id = request.session['id'])
    if not checkuser.admin:
        return redirect('/dashboard/'+str(request.session['id']))

    context = {
        'user' : User.objects.get(id=request.session['id']),
        'all_coders' : Coder.objects.all()
    }
    return render(request, 'singleproject/admin_coders.html', context)

def remove_coder(request, number):
    try:
        request.session['id']
    except:
        return redirect('/')
    checkuser = User.objects.get(id = request.session['id'])
    if not checkuser.admin:
        return redirect('/dashboard/'+str(request.session['id']))

    Coder.objects.removeCoder(number)
    return redirect('/admin/coders')

def logout(request):
    if 'cart' in request.session:
        cart = request.session['cart']
        request.session.clear()
        request.session['cart'] = cart
    else:
        request.session.clear()
    return redirect('/')

def coder_profile(request,number):
    try:
        request.session['id']
    except:
        return redirect('/')
    context = {
        'coder' : Coder.objects.get(id=number)
    }
    return render(request, 'singleproject/coder_profile.html', context)
