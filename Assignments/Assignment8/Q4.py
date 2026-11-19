# def odd(n):
#     for i in range(1,n+1):
#         if(n%2==0):
#             return 0
#         else:
#             return n
# def sum(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=odd(i)
#     return sum
# n=5
# res=sum(n)
# print(res)

def odd_sum(n):
    sum=0
    for i in range(1,n+1):
        if(i%2!=0):
            sum+=i
    return sum
n=5
res=odd_sum(n)
print(res)

