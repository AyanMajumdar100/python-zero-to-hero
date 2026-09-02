


# B. Passing Functions as arguements
# Higher Order Function : The function which accepts a function as an arguement or returns func as a result
# CallBack Function : The function being passed as arguements

def tone1(name):
    return f"FUCK YOU {name}"

def tone2(name):
    return f"THANK YOU {name}"
# HOC
def greeter(name,func):
    msg = func(name)
    print(msg)

greeter("Aryan", func = tone1)      # FUCK YOU Aryan
greeter("Ayan", tone2)              # THANK YOU Ayan

# EXAMPLE 2
lc_str = list(map(str.lower,["AYAN", "SAYAN", "GOKUL", "VISHNU"]))
print(lc_str)                       # ['ayan', 'sayan', 'gokul', 'vishnu']

# BOTH ARE SAME
print("AYANNN".lower())
print(str.lower("AYANNN"))

names = ["AYAN1", "SAYAN1", "GOKUL1", "VISHNU1"]
print (list(map(str.lower,names)))



def longest(*words):
    return max(words, key=len)
print(longest("Python", "AI", "Programming", "ML"))