#y = [1, 2, 3, 4, 5]
# result=0
# for i in y:
#     if i % 2 == 0:
#         result  += i
        
    
#print(result)

def sum(y):
    result = 0
    for i in y:
        if i % 2 == 0:
            result += i
    return result

y = [1, 2, 3, 4, 5]
print(f"The sum is: {sum(y)}")

