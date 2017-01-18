def fizz_buzz(number):
	#Since they all might have numbers that intersect.
	# It makes sense to start with the intersection
  if number%3 == 0 and number%5 == 0:
		return("FizzBuzz")

	elif number%3 == 0:
		return("Fizz")

	elif number%5 == 0:
		return("Buzz")
	else: 
		return(number)	

fizz_buzz(101)
