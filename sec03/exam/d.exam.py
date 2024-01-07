#def my():
#    return 100
def test01():
    res = lambda:100
    print(res,res())


#def my():
#    return 100+x
def test02():
    res = lambda x: 100+x
    print(res,res(10))

# def my(x,y,z):
#    return x+y+z
def test03():
     res = lambda x,y,z: x+y+z
     print(res,res(1,2,3))

#def my(x):
#    return x

def test04():
    my_list= [1,2,3,4,5]
    res = lambda x:x
    print(res(my_list))

def test051():
    my_list = [1, 2, 3, 4, 5]
    even_res =[ x for x in my_list if x% 2 ==0]
    return even_res

def test05():
    my_list = [1, 2, 3, 4, 5]
    res = lambda my_list: [ x for x in my_list if x% 2 ==0]
    print(res(my_list))

def examfor():
    numbers=[1,2,3,4,5]
    squared_numbers =[ x**2  for  x in numbers]
    return print(squared_numbers)

def examzip():
    name  =['a', 'e', 'i', 'o', 'u']
    age =  [1,2,3,4]
    tel = [11,22,33,44,55,66,77,88,99]
    zip_res  = zip(name,age,tel)
    print(zip_res)
    for  name, age, tel in zip_res:
        print(f'{name}  :{age}  : {tel}')

def examfor02():
    strings = ["apple", "banana", "cherry"]
    uppercase_strings = [s.upper() for s in strings]
    print(uppercase_strings)

def examfor03():
    numbers = [1, 2, 3, 4, 5]
    filtered_numbers = [x for x in numbers if x % 2 != 0]
    print(filtered_numbers)
def examfor_03():
    numbers = [1, 2, 3, 4, 5]
    filtered_numbers = [x for x in numbers if x % 2 == 0]
    print(filtered_numbers)

def examfor04():
    strings = ["apple", "banana", "cherry"]
    substring = "an"
    filtered_strings = [s for s in strings if substring in s]
    print(filtered_strings)

def examfor_04():
    strings = ["apple", "banana", "cherry"]
    substring = "an"
    filtered_strings = [s for s in strings if substring in s]
    results = filtered_strings
    print(results)

def examfor05():
    strings = ["apple", "banana", "cherry"]
    last_chars = [s[-1] for s in strings]
    print(last_chars)

def examfor06():
    str ="process finished with exit code"
    res_words = [w.capitalize() for w in str.split()]
    print(res_words)

if __name__ == "__main__":
    examfor06()