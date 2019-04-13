# Finding nth number in Fibonacci series(Heroku deployment)

application that will display the Nth number in Fibonacci sequence. For instance, if N is 6 and the sequence starts with [1,1..] then it should display ‘8’ as the 6th element in the sequence. Application should be hosted on the internet with an user interface asking for the input ‘N’. It should also print the time it took to get the results back to the user.

## Installation
Use the package manager pip to install Django.

pip install Django==2.2

## Usage
In the function directly implement the formula for nth term in the fibonacci series.

Fn = {[(√5 + 1)/2] ^ n} / √5

x = (((math.sqrt(5)+1)/2) ** n)/math.sqrt(5)

Time Complexity: O(1)

## Support
http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html

# Running the tests
Enter the number for which you want to know the fibonacci number

Example 1 : 

	Input : 6
	Output : 8
	Time taken : 0.0000207424

Example 2 :

	Input : 50
	Output : 12586269025
	Time taken : 0.0000355244

# Built With
Django 2.2 