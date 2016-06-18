# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples both store collections of items, which can all be of different types. They share the same syntax for iteration, slicing, concatenation, and checking for containment using the `in` operator. However, the main difference between them is that lists are mutable, while tuples are not. This means that we can use tuples, but not lists, as keys in dictionaries. Another difference between them is that lists have access to built-in methods such as append, extend, and sort, while tuples do not.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets both store collections of items. However, unlike lists, sets do not allow for duplicate items. This can often be used to our advantage whenever we want to pick out the unique elements of a list. We simply have to convert the list into a set using the function `set`. Furthermore, unlike lists, sets do not have an inherent ordering. The upside to this is that searching for an element in a set has time complexity O(1) since it's implemented by a hash table which allows for fast lookup. However, the time complexity to search for an element in a list is O(n) since Python performs a linear search on the list.

Lists are great for when you want some kind of ordering on a sequence of items (as is the case when you want to sort a collection). For example, we can write something like:
```python
sorted(d.items(), key=lambda x: x[1]) 
```
Our goal here is to sort the dictionary `d` so we extract its contents in the form of a list of tuples. Then we can for instance sort the list by the values of the dictionary (second element of each tuple). While, the sorted function does work on dictionaries, it only returns a sorted list of the keys and forgets about the values.

Sets on the other hand are nice when all we care about is checking whether or not a collection contains a certain element (ignoring duplicates). We can dump the contents of the collection into a set (taking O(n) time) and then easily check for inclusion using `in` afterwards. While dictionaries provide similar functionality in terms of fast look up, sets can be more convenient because we don't have to set values for each of our keys. Another example of using sets is the following:
```python
friends_dict = {'Mark':['Bob', 'James', 'Cameron'], 'Jim':['Mark', 'Cameron', 'Kirk'], 'Bob':['Mark', 'Jim', 'Steve']}
unique_friends = {names for friends in friends_dict.values() for names in friends}
```
Here we wish to flatten the dictionary which maps people to their list of friends. We then want to obtain only the unique names from the dictionary. We can do this by performing a set comprehension instead of a list comprehension, with minimal change in syntax.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Python's `lambda` can be used to create anonymous functions. If we're only going to use it once, rather than going through the trouble of naming and defining a new function, we can just use `lambda` to create a function inline. One of the most common uses of `lambda` is to create "key" functions for the method `sort`. For example, we can write:
```python
a = [(2, 3), (6, 7), (3, 34), (24, 64), (1, 43)]
a.sort(key=lambda x: x[1])
```
By default the `sort` method sorts lists of tuples in increasing order on the first element, but we can use `lambda` to create a function that specifies the second element of each tuple as the key to sort on instead.

We could have achieved the same result with regular good 'ol functions like so:
```python
def get2(x):
    return x[1]

a.sort(key=get2)
```
However, as noted earlier, it's a bit of a waste to define a function that we're never going to use anywhere else in the code. Using `lambda` just makes things cleaner and more concise.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions offer a neat and concise way of creating lists of elements in a single statement. For example, writing:
```python
l = [x**2 for x in range(1,10) if x % 3 == 0]
```
is the same as writing:
```python
l = list()
for x in range(1,10):
    if x % 3 == 0:
        l.append(x**2)
```
We can also achieve the same result using `map` and `filter` as follows:
```python
filter(lambda x: x % 3 == 0, map(lambda x: x**2, range(1,10)))
```
However, this way of writing it is arguably less readable than the previous two examples.

The performance of `map` and `filter` v.s. using a list comprehension is pretty comparable. There is a slight speed advantage for `map` if we are calling an already defined function on each element and a slight speed advantage for list comprehensions if we are evaluating an expression on each element. This may be because `map` has the additional overhead of calling a `lambda` that returns the given expression, whereas list comprehensions simply evaluate the expression for each element. In any case, since their performances are pretty similar, I prefer writing list comprehensions because in most cases they are easier to read.

Set and dictionary comprehensions work pretty much in the same way as list comprehensions do. As an example, we can use a dictionary comprehension to count up frequencies as follows:
```python
colors = ['purple', 'red', 'red', 'yellow', 'green', 'yellow', 'brown', 'purple', 'yellow', 'red']
freq = {color: colors.count(color) for color in set(colors)}
```
Here we want to iterate over the unique values in `colors` so we convert it into a set in the above.

As an example of a set comprehension, we can find all unique primes up to 100:
```python
primes = {x for x in range(2, 101) if all(x % y for y in range(2, x))}
```

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
Edit the 3 functions i [q8_parsing.py](python/q8_parsing.py)





