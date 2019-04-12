from django.http import HttpResponse
from django.template import Template 
from django.shortcuts import render, redirect

def homePage(request):
	# return HttpResponse("Hello from Home Page")
	return render(request,'fibonacciCallHub/homepage.html')

def result(request):
	if request.method == 'POST':
		user_entered = request.POST.get('fnumber')
		print(user_entered)
		return  render(request,'fibonacciCallHub/result.html', {'number':user_entered})