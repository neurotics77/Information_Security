import random
import gmpy2

# 随机生成两个不相等的大素数p和q
def get_p_q(num_bits):
    while (1):
        p = random.randrange(2 ** (num_bits - 1) + 1, 2 ** num_bits, 2) # 随机生成指定bit位数的数字
        if gmpy2.is_prime(p):
            break
    while (1):
        q = random.randrange(2 ** (num_bits - 1) + 1, 2 ** num_bits, 2) # 随机生成指定bit位数的数字
        if gmpy2.is_prime(q) & (p != q):
            break
    print('p : %i'%p)
    print('q : %i'%q)
    return p, q

# 计算n
def get_n(p, q):
    n = p * q
    print('n : %i' %n)
    return n

# 计算n的欧拉函数值
def get_euler(p, q):
    return (p - 1) * (q - 1)

# 计算与M互质的e
def get_e(M):
    while (1):
        e = random.randint(1, M)
        if gmpy2.gcd(e, M) == 1:
            print('e : %i' %e)
            return e

# 计算e和M的模反元素d
def get_d(e, M):
    d = gmpy2.invert(e, M)
    print('d : %i' %d)
    return d

def encrypt(text, e, n):
    # 将字符串转换为字节序列后，再转为整数进行加密
    num = int.from_bytes(bytes(text, encoding='utf-8'), 'big')
    print('num : %i' %num)
    num_encrypt = gmpy2.powmod(num, e, n)
    return num_encrypt

def decrypt(ciphertext, d, n):
    num_decrypt = gmpy2.powmod(ciphertext, d, n)
    # 将解密后的数字明文先转换为字节序列，再转换为字符串
    return str(int(num_decrypt).to_bytes((num_decrypt.bit_length() + 7) // 8, 'big'), encoding='utf-8')

def RSA(text, num_bits):
    p, q = get_p_q(num_bits)
    n = get_n(p, q)
    M = get_euler(p, q)
    e = get_e(M)
    d = get_d(e, M)
    ciphertext = encrypt(text, e, n)
    print('密文（16进制）：%#x' % ciphertext)
    plaintext = decrypt(ciphertext, d, n)
    print('明文：%s' %plaintext)

if __name__ == "__main__":
    num_bits = input('请输入密钥长度：')
    text = 'CQUINFORMATIONSECURITYEXP1'
    RSA(text, int(num_bits)//2)