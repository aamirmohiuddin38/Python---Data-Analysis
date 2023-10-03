"""
> "A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory."    (OR)
> "Python closure is a nested function that allows us to access variables (free variables) of the outer function even after the outer function is closed."
"""

# ---------------------- Example 1:

# def outer_func():
#     message = "Hi"  #free variable

#     def inner_func():
#         print(message)

#     return inner_func

# hi = outer_func()   #outer_func() gets executed / not in memory now
# print(hi)
# print(hi.__name__)
# hi()    #still remembers the free variable of outer func 



# --------------------- Example 2 (using above function with parameters):

# def outer_func(msg):
#     message = msg  

#     def inner_func():
#         print(message)

#     return inner_func

# hi = outer_func('HI')
# hello = outer_func('HELLO') 

# hi()
# hello()

# -------------------- Example 3 (Practical Use Case):
import logging
logging.basicConfig(filename='closure_example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args)
        )
        print(func(*args))
    return log_func

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

#print(add_logger.__name__)
add_logger(20,10)
sub_logger(20,10)