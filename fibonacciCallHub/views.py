from django.http import HttpResponse
from django.template import Template 
from django.shortcuts import render, redirect
import time
import math

def homePage(request):
	# return HttpResponse("Hello from Home Page")
	return render(request,'fibonacciCallHub/homepage.html')

def result(request):
	if request.method == 'POST':
		user_entered = request.POST.get('fnumber')
		
		if user_entered == '':
			return  render(request,'fibonacciCallHub/homepage.html', {'number':user_entered, 'message': "Please enter the number"})
		else:
			start_time = time.time()

			fibNum = fibonacci(int(user_entered))
			
			time_diff = time.time() - start_time

			# start_time1 = time.time()
			
			# fibNum1 = fibonacci1(int(user_entered))
			
			# time_diff1 = time.time() - start_time

			return  render(request,'fibonacciCallHub/homepage.html', {'number':user_entered, 'fibNum':fibNum, 'timeDiff':("%.5f" % time_diff)})

# def fibonacci1(n):
#     if n==0: 
#         return 0
#     elif n==1: 
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)


## Optimized code
# Using the formula Fn = {[(√5 + 1)/2] ^ n} / √5 
# Time Complexity = O(1)
def fibonacci(n):
	
	x = ((math.sqrt(5)+1)/2)
	
	y = (x ** n)/math.sqrt(5)

	return int(y)