#[10950]반복문, A+B - 3
from re import T

T = int(input())
for T in range(T):
    num1, num2 = map(int, input().split())
    print (num1 + num2) 