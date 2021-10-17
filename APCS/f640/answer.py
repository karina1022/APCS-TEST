def f(x):
    a = 2*int(x) - 3
    return a

def g(x,y):
    b = 2*int(x) + int(y) - 7 
    return b

def h(x,y,z):
    c = 3*int(x) - 2*int(y) + int(z)
    return c 

list_input = input().split(" ")

list_input_len = len(list_input)

while list_input_len > 0:
    list_input_len = list_input_len - 1
    if list_input[list_input_len] == "f":
        result = f(list_input[list_input_len + 1])
        list_input[list_input_len] = result
        list_input.pop(list_input_len + 1)
    elif list_input[list_input_len] == "g":
        result = g(list_input[list_input_len+1],list_input[list_input_len+2])
        list_input[list_input_len] = result
        list_input.pop(list_input_len+1)
        list_input.pop(list_input_len+1)
    elif list_input[list_input_len] == "h":
        result = h(list_input[list_input_len+1],list_input[list_input_len+2],list_input[list_input_len+3])
        list_input[list_input_len] = result
        list_input.pop(list_input_len+1)
        list_input.pop(list_input_len+1)
        list_input.pop(list_input_len+1)

print(list_input[0])
