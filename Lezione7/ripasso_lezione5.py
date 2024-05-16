#1

def function():
    result: list = []
    for x in range(1999, 3201):
        if x % 7 == 0 and x % 5 != 0:
            result.append(x)
    return result

#print(function())


2#

def factorial(number: int):  
    result: int = 1
    for i in range(2, number + 1):
        result *= i
    return result

number: int = 8
#print(factorial(number))


3#

def factorial(lst: list) -> list:  
    result_list: list = []
    for i in lst:
        result: int = 1
        for x in range(2, i + 1):
            result *= x
        result_list.append(result)
    return result_list

lst = [2, 5, 8, 10]
#print(factorial(lst))


4#


def function4(number: int) -> dict:
    n_dict: dict = {}

    for x in range(1, number + 1):
        n_dict[x] = x*x
    return n_dict

number = 8
print(function4(number))

 