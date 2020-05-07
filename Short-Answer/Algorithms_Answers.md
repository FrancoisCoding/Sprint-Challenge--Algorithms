#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because as input becomes bigger, it will more time to add numbers for 'a' before while loop stops

b) O(n^2) This is looping through the same list twice with the for/while loops, this makes the code block an O(n^2) solution. The runtime for this will grow exponentially as the number of inputs increase and isn't ideal if the numbers of inputs will be large. 

c) O(n) This is a recursive solution that is looped based on the number of bunnies received. The number of bunnies we have (n) will determine how many times we have to call this function. 


## Exercise II

## Create Variables ##
 num_eggs(for dropped eggs attempted throwing ) and broke_eggs

## Start of function ##
 Input eggs and building size with n - stories

## Loop ##
Iterate over each floor and toss eggs

## If/Else ##
IF Egg Breaks - mark the floor with broken egg, and break out of the loop. This floor always yields broken eggs

ELSE - Continue dropping eggs

## Runtime Complexity ##
O(1) because it will be the same floor that egg breaks no matter N story building
