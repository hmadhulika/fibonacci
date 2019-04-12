from django.http import HttpResponse
from django.template import Template 
from django.shortcuts import render, redirect
import time

def homePage(request):
	# return HttpResponse("Hello from Home Page")
	return render(request,'fibonacciCallHub/homepage.html')

def result(request):
	if request.method == 'POST':
		start_time = time.time()

		user_entered = request.POST.get('fnumber')
		print(user_entered)
		if user_entered == '':
			return  render(request,'fibonacciCallHub/homepage.html', {'number':user_entered, 'message': "Please enter the number"})
		else:
			fibNum = fibonacci(int(user_entered))
			
			time_diff = time.time() - start_time

			return  render(request,'fibonacciCallHub/homepage.html', {'number':user_entered, 'fibNum':fibNum, 'timeDiff':float(round(time_diff,5))})

def fibonacci(n):
    if n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)