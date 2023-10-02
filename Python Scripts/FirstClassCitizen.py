""" 
    First Class Funtions: A programming language is said to have first-class functions it it treats functions as First-Class Citizens.

    First Class Citizens: A First-Class Citizen (sometimes called first-class objects) in a programming language is an entity which supports all the operations generaly
                            available to other entity. These operations typically include being passed as an argument, returned from a function and assigned to a
                            variable.
"""
# 1. Assigning function to a variable

def square(x):
    return x * x

f = square

print(square)
print(f)
print(f(5))

# 2. Pass function as arguments
""" If a function accepts other function as argument or return function as their result - those are called higher order fuctions.
    Example map(). """

def userdef_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = userdef_map(square, [1,2,3,4,5])
print(squares)

# 3. Returning function as Result.

def html_tag(tag):
    def wrap_tags(text):
        print('<{0}>{1}</{0}>'.format(tag, text))
    return wrap_tags

heading_h1 = html_tag('h1')
heading_h1('This is my Heading')
# (concept of closure)
para_p = html_tag('p')
para_p('Simple text paragraph')

