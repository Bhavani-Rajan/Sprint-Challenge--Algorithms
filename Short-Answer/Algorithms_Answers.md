#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  condition is checking for n^3 and inside the loop its adding n^2, So this loop excutes n times.
    The time complexity will be O(n)


b)  for loop executes n times
    while loop executes (n/2 ) times
    The time complexity will be O(n* (n /2))
    


c)  This recursion function will be executed n + 2 times for every n bunnies.
    The time complexity will be O(n * n).
    Also, since Cache is not used, the program will give error in 2960 time.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. 
Suppose also that an egg gets broken if it is thrown off floor f or higher, 
and doesn't get broken if dropped off a floor less than floor f. 
Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

Since, its number of floors, its a sorted list. Binary search will minimise the time complexity to search the f, from which the number of dropped + broken eggs is minimized.
Time complexity will be O(log n)
Binary search - its an algorithm, where the list is sorted and desired number is searched mid of the list. discarding half of the list based on the condition. that way everytime the length of the search is reduced.

here we have to find the f where egg dropped doesn't break.
lets consider floors stored in a list
select the floor thats mid of the list and check if egg dropped will break or not,

if the answer is yes 
 discard the right half and consider the left half of the list
 
again find the mid of the sub list and search goes on until we find the f :)

