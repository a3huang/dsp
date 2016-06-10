# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples both store collections of items, which can all be of different types. We can also iterate over, perform slicing on, perform concatenation on, and use the `in` operator with both lists and tuples. However, the main difference between them are that lists are mutable, while tuples are not. This means that we can use tuples, but not lists, as keys in dictionaries. Another difference between them is that lists have access to built-in methods such as append, extend, and sort, while tuples do not.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets both store collections of items. However, sets do not have any duplicates as they only store unique values. Furthermore, unlike lists, sets do not have an inherent ordering. Searching for an element in a set has time complexity O(1) since it's implemented by a hash table which allows for fast lookup. However, the time complexity to search for an element in a list is O(n) since Python must perform a linear search on the list.

Lists are great for when you want an ordering on a sequence of items.

For example:

`l = list("string")`

`l.sort()`

Here, we convert the string called "string" into a list of characters and sort them in alphabetical order.

Sets on the other hand are nice when all we care about is checking whether we have a certain element or not (ignoring duplicates). Say we have a long list of words named `l` and we want to check if the word "swallow" is contained in `l`. 

We can do for example:

`s = set(l)`

`"swallow" in s`

Once we dump the entire list into a set, we can easily check whether it contains a given element or not.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Python's `lambda` can be used to create anonymous functions. If it's for something we're probably going to use only once, rather than going out of our way to define a named function for it, we can just create a "disposable" function using `lambda`. One of the most common uses of `lambda` is to create "key" functions for `sort`.

For example:

`a = [(2, 3), (6, 7), (3, 34), (24, 64), (1, 43)]`

`a.sort(key=lambda x: x[1])`

By default `sort` sorts lists of tuples in increasing order on the first element, but we can use `lambda` to specify the second element of each tuple as the key to sort on instead.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions offer a neat and concise way of creating lists of elements in a single statement.

For example:

`l = [x**2 for x in range(1,10) if x % 3 == 0]`

is the same as writing:
`l = list()

for x in range(1,10):

    if x % 3 == 0:
    
        l.append(x**2)`

We can also achieve the same result using `map` and `filter` as follows:
`filter(lambda x: x % 3 == 0, map(lambda x: x**2, range(1,10)))`
However, this way of writing it is arguably less readable than if we used list comprehensions.

The performance of `map` and `filter` v.s. using a list comprehension is comparable. There is a slight speed advantage for `map` if we are calling an already defined function on each element and a slight speed advantage for list comprehensions if we are evaluating an expression on each element. This may be because using `map` has the additional overhead of calling a `lambda` that returns the given expression, whereas the list comprehension simply evaluates the expression for each element.

Set and dictionary comprehensions work pretty much the same way as list comprehensions. 
For example, let's say that `colors` is a list of strings of color names (with duplicates). Then, to count up the frequencies of each color, we can perform a dictionary comprehension as follows:

`freq = {color: colors.count(color) for color in set(colors)}`

Here we want to iterate over the unique values in `colors` so we convert it into a set in the above.

As an example of a set comprehension, we can find all (unique) primes up to 100:

`primes = {x for x in range(2, 101) if all(x % y for y in range(2, x))}`

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937 days

b.  
```
date_start = '12312013'
date_stop = '05282015'  
```

513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





