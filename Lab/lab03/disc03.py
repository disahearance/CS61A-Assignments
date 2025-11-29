# discussion3相关代码，主题为“递归”
def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        swipe(n % 10)
        swipe(n // 10)
        swipe(n % 10)

def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n < 1:
        return 1
    else:
        return n * skip_factorial(n - 2) #返回自己 和 自己后面的数

from math import sqrt
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    assert n > 1,"n大于1才能开始判断哦"
    i = 2
    if n == 2:
        return True
    def f(i):
        if n % i == 0:
            return False
        elif i > sqrt(n):
            return True
        else:
            return True and f(i+1)
    return f(i)

def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
   
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return 1 + hailstone(n//2)

def odd(n):
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    else:
        return 1 + hailstone(3*n+1)



def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.
    数到2,5人玩
    >>> sevens(2, 5) 
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who # 回归
        "*** YOUR CODE HERE ***"
        # 遇到含7数字或7的倍数，转向
        if has_seven(i) == True or i % 7 == 0:
            return f(i+1, (who-direction) % k or k, -direction)

        # 没遇到含7数字，不转向
        else:
            return f(i+1, (who+direction) % k or k, direction)
            
    return f(1, 1, 1)

def has_seven(n):
    """判断数字n中是否有7。
    >>> has_seven(7)
    True
    >>> has_seven(10)
    False
    """
    if n == 0:
        return False #归
    elif n % 10 == 7:
        return True #归
    else:
        return has_seven(n // 10) #递
    
