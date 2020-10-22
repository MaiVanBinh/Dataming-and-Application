```python
print(7**4)
```

    2401
    


```python
s = 'Hi there Sam!'
print(s.split(" "))
```

    ['Hi', 'there', 'Sam!']
    


```python
planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers".format(planet, diameter))
```

    The diameter of Earth is 12742 kilometers
    


```python
lst = [1,2,[3,4], [5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2])
```

    ['hello']
    


```python
d = {
    'k1': [1,2,3,{
        'tricky': ['oh', 'man', 'inception',{'target': 
                                             [1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])
```

    hello
    


```python
# Tuple is immutable
```


```python
def domainGet(str):
    arr = str.split('@');
    if len(arr) == 2:
        return arr[1]
    raise Exception('Email is not valid')
print(domainGet('user@domain.com'))
print(domainGet('userdomain.com'))
```

    domain.com
    


    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    <ipython-input-11-936168e8dd18> in <module>
          5     raise Exception('Email is not valid')
          6 print(domainGet('user@domain.com'))
    ----> 7 print(domainGet('userdomain.com'))
    

    <ipython-input-11-936168e8dd18> in domainGet(str)
          3     if len(arr) == 2:
          4         return arr[1]
    ----> 5     raise Exception('Email is not valid')
          6 print(domainGet('user@domain.com'))
          7 print(domainGet('userdomain.com'))
    

    Exception: Email is not valid



```python
def findDog(str):
    import re
    return True if re.search("[^a-zA-Z0-9]dog[^a-zA-Z0-9]", str) else False
print(findDog('This is a dog.'))
print(findDog('Is there a dog here.'))
print(findDog('This is a dog.s'))
print(findDog('This is a dogs .'))
print(findDog('This is a Dog.'))
print(findDog('This is a sdog.'))

```

    True
    True
    True
    False
    False
    False
    


```python
def countDog(str):
    import re
    arr = re.findall("^dog\s|\sdog\s|\sdog$", str)
    return len(arr)
print(countDog('dog This dog is a dog. dogs'))
print(countDog('this dog runs faster than the other dog dude!'))
```

    2
    2
    


```python
seq = ['soup', 'dog', 'salad', 'cat', 'great']
list(filter(lambda item: item[0] == 's', seq))
```




    ['soup', 'salad']




```python
def caught_speeding(speed, is_birthday):
    if speed <= 60 or (speed <= 65 and is_birthday):
        print('No Ticket' )
    elif speed <= 80 or (speed <= 85 and is_birthday):
        print('Small Ticket')
    else:
        print('Big Ticket')
caught_speeding(81, True)
caught_speeding(81, False)
caught_speeding(65, False)
caught_speeding(65, True)
caught_speeding(75, False)
caught_speeding(75, True)
```

    Small Ticket
    Big Ticket
    Small Ticket
    No Ticket
    Small Ticket
    Small Ticket
    
