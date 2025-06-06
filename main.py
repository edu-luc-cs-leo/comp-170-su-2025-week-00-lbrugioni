#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
first_name, is a valid name in python, because it is snake case, which is when we use '_' instead of spaces between words.
2nd_name, is an invalid name because it starts with a number
age, is a valid name becuase it starts with a letter and is descriptive
total_amount, is a valid name because it starts with a letter and uses an underscore
while, is an invalid name because it is a reserved word in python
Student, is a valid name because it starts with an uppercase letter and is descriptive
my-varibale, is an invalid name because dashes are not allowed, only underscores
for, is invalid because it is a reserved word
_temp, is a valid name because an underscore can be used to start the name
value#, is an invalid name because their can't because the # special character 
"""
# Problem 2
"""
calculate_total,is a valid name becuase it starts with a letter and uses an underscore 
3rd_function, is invalid function name because it starts with a number which is not allowed 
print_values, is a valid function name because it starts with a letter and has no spaces 
find-item, is an invalid fucntion name because it uses a hypen which is not allowed 
def, is an invalid function name because it is a reserved word 
updateProfile, is valid name but not recommeneded because snake_case is recommended by using underscores as spaces 
my_function, is a valid name because it starts with a letter and uses an underscore to seperate the words 
try, is an invalid fucntion name because it is a reserved word 
init_data, is a valid function name because it starts with a letter 
value@function, is an invalid function name because the symbol, @ is not allowed  
"""
# Problem 3
"""
True and False,is a valid expression and it evaluates to false because both sides must be true to result in true 
5 > 3 or "apple" < "banana", is a valid expression and it evaluates that 5 is greater than 3 which is true and apple comes before bananna becuase a comes before b 
not 10 <= 20, is a valid expression because 10 is less than 20 and the not before 10 is making it not true 
True or 5 = 4, is an invalid expression because the use of = can not be used to compare values 
"apple" ! = "orange" and 5, is an invalid expression because there can not be a space between the ! and the = 
3 < 5 not True, is an invalid expression because 5 is greater than 3 but it is saying that it is false 
False == (3 > 4), is a valid expression because 3 is not greater than 4 
10 <= "10", is an invalid expression because it is comparing a value with a string 
True or not False, is a valid expression because is using the truth tables and the outcome would be false 
5 and or 4, is an invalid expression because the words and, or can not be used together with integers 
"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
