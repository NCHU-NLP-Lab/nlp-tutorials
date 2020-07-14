# Example Python Homework   

From https://github.com/uwhpsc-2016/example-python-homework    

*An example homework assignment in Python for demonstrating how homework is done
in the course.*

In this (example) assignment we will learn some basic Python. In particular, we
will learn about basic Python arithmetic, list handling, and how to create
Python modules as well as an introduction to writing tests using Python's
`unittest` module.

## Objective

Provide definitions to the functions `square` and `cube` defined in the Python
submodules `example_homework.squaring` and `example_homework.cubing`,
respectively.

```python
def square(x):
    # return the square of x
    
def cube(x):
    # return the cube of x
```

The provided example test suite can be executed using

```
$ python ./test_example_homework.py
```

As always, you are welcome (and encouraged) to add your own tests to the test
suite to ensure that your code is robust. Most of all, make sure that the
supplied tests pass so that the grading software can import and use your
function as expected.

## Grading

When the homework deadline is reached your implementation of `square` and `cube`
will be run against the following tests:

* (1/5) the square and cube of zero is zero (already in the provided test suite)
* (1/5) the square and cube of two is four and eight, respectively (already in
  the provided test suite)
* (1/5) `square` and `cube` should behave appropriately with complex numbers as
  input (e.g. `1.0 - 2.0j`)
* (2/5) these functions should also be able to act on Python `list`s of numbers
  without the use of the Python function `map`. that is, if the input is of type
  `list` then the output should also be of type `list` containing appropriate
  corresponding values

It is important that the function names and locations DO NOT CHANGE. Otherwise,
the test suite used for grading may not be able to import your code. If it's
importable in the test suite provided to you it should be importable in the
grading test suite.
