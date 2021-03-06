def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)

print(pure_function(2,2))

"""

It used Memoization.

Memoization is whereby the result of a previous section can be referred and used to
get the result of the next without having to go through a lot of work.

Example.
If you write
 1 + 1 + 1 + 1 + 1
and asked for an answer, you will take time to do that and get 5
Now if I add another +1 at the end
1 + 1 + 1 + 1 + 1 + 1
You will instantly say 6

That is memoization. 
You will not go back to adding the whole list of 1s.
Practical example can be in calculation of factorials.

Once you know that 3! is 6 (ie 1 * 2 * 3) then if I asked you 4! you simply 
take 3! * 4 = 24 other than doing it over again as 1 * 2 * 3 * 4

Now let us apply Memoization:
9! = 362880
find 10!
Answer: Simply 9! * 10 = 3628800
"""
