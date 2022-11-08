#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

# 判断是否为素数
def isprime(x):
    print("isprime")
    if x == 2 | x == 1:
        return False
    for i in range(2, int(x ** 0.5)):
        if (x % i) == 0:
            return False
    return True


# 辗转相除法判断两数互质
def gcd(a, b):
    print("gcd")
    if a < b:
        temp = a
        a = b
        b = temp
    while b > 0:
        temp = a % b
        a = b
        b = temp
    if a == 1:
        return True
    else:
        return False


# 随机生成两个不相等的素数p和q
def get_p_q():
    print("get_pq")
    while (1):
        p = random.randint(100, 1000)
        if isprime(p):
            break
    while (1):
        q = random.randint(100, 1000)
        if isprime(q) & (p != q):
            break
    return p, q


# 计算n的欧拉函数值
def get_euler(p, q):
    print("get_euler")
    return (p - 1) * (q - 1)

# 计算与M互质的e
def get_e(M):
    print("get_e")
    while (1):
        e = random.randint(1, M)
        if gcd(e, M):
            return e

# 计算e和M的模反元素d
def get_d(e, M):
    print("get_d")
    i = 1
    while(1):
        temp = (M * i + 1) % e
        if temp == 0:
            return (M * i + 1) / e
        i = i + 1

def encryption(plaintext, e, n):
    print("encryption")
    # ciphertext = []
    # for i in range(len(plaintext)):
    #     x = ord(plaintext[i])
    #     cnt = 1
    #     temp = x % n
    #     while(cnt != e):
    #         cnt = cnt + 1
    #         temp = (temp * (x % n)) % n
    #     ciphertext.append(chr(temp))
    # return ciphertext
    ciphertext = []
    num = ''
    for i in range(len(plaintext)):
        x = ord(plaintext[i])
        num = num + str(x)
    cnt = 1
    temp = eval(num) % n
    while(cnt != e):
        cnt = cnt + 1
        temp = (temp * (eval(num) % n)) % n
    print(temp)
    ciphertext.append(chr(temp))
    print(num)
    return ciphertext

def decrypt(plaintext, d, n):
    ans = []
    for i in range(len(plaintext)):
        x = ord(plaintext[i])
        cnt = 1
        temp = x % n
        while(cnt != d):
            cnt = cnt + 1
            temp = (temp * (x % n)) % n
        ans.append(chr(temp))
    return ans

def RSA(plaintext):
    p, q = get_p_q()
    n = p * q
    M = get_euler(p, q)
    e = get_e(M)
    d = get_d(e, M)
    ciphertext = encryption(plaintext, e, n)
    print(ciphertext)
    print("".join(ciphertext))
    ans = decrypt(ciphertext, d, n)
    print("".join(ans))

if __name__ == "__main__":
    plaintext = 'CQUINFORMATIONSECURITYEXP1'
    RSA(plaintext)