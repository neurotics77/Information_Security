import matplotlib.pyplot as plt
import numpy as np
# 绘制标准字母统计频率条形图
# 字母及其统计频率
letter = ['E', 'T', 'A', 'O', 'N', 'I', 'S', 'R', 'H', 'L', 'D', 'C', 'U', 'P', 'F', 'M', 'W', 'Y', 'B', 'G', 'V', 'K',
          'Q', 'X', 'J', 'Z']
f_standard = [0.123, 0.096, 0.081, 0.079, 0.072, 0.072, 0.066, 0.06, 0.051, 0.04, 0.037, 0.032, 0.031, 0.023, 0.023, 0.023, 0.02,
              0.019, 0.016, 0.016, 0.009, 0.005, 0.002, 0.002, 0.001, 0.001]
z = np.linspace(0, 26, 26)
plt.xlabel('letter')
plt.ylabel('frequency')
plt.bar(x=z, height=f_standard, width=0.8)
plt.xticks(z, letter)
plt.title('Standard Letter Frequency')

# 绘制给定密文的字母统计频率图
str = 'UZ QSO VUOHXMOPV GPOZPEVSG ZWSZ OPFPESX UDBMETSX AIZ VUEPHZ HMDZSHZO WSFP APPD TSVP QUZW YMXUZUHSX EPYEPOPDZSZUFPO MB ZWP FUPZ HMDJ UD TMOHMQ'
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
length = len("".join(str.split()))
f_ciphertext = [] # 密文字母频率
for i in range(26):
    f_ciphertext.append(str.count(alphabet[i]) / length)
temp = dict(zip(alphabet, f_ciphertext))
alphabet, f_ciphertext = zip(*sorted(temp.items(), key=lambda x: x[1], reverse=True))
plt.figure()
plt.xlabel('letter')
plt.ylabel('frequency')
plt.bar(x=z, height=f_ciphertext, width=0.8)
plt.xticks(z, alphabet)
plt.title('Ciphertext Letter Frequency')
alphabet = list(alphabet)

# 调整替换表的映射关系
def revise_table(a, b):
    idx1 = alphabet.index(a)
    idx2 = alphabet.index(b)
    alphabet[idx1] = b
    alphabet[idx2] = a

revise_table('W','E') # W和E交换
revise_table('M','U') # M和U交换
revise_table('Q','B') # Q和B交换
revise_table('H','O') # H和O交换
revise_table('E','D') # E和S交换
revise_table('V','X') # V和X交换
revise_table('H','F') # H和F交换
revise_table('F','J') # F和J交换
revise_table('D','J') # D和J交换
revise_table('A','Y') # A和Y交换
revise_table('Y','B') # Y和B交换
revise_table('T','B') # T和B交换
revise_table('I','J') # I和J交换

plaintext = ""
replacetable = dict(zip(alphabet, letter))
# 按照替换表进行解密
for i in range(len(str)):
    if str[i] == ' ':
        plaintext = plaintext + ' '
        continue
    plaintext = plaintext + replacetable[str[i]]

cnt = 0
# 输出替换表
print("替换表对应关系如下（密文，明文）：")
for i in sorted(replacetable):
    cnt = cnt + 1
    if cnt < 13:
        end_char = ' '
    else:
        end_char = '\n'
        cnt = 0
    print((i, replacetable[i]), end = end_char)
# 输出明文
print("对应的明文为：")
print(plaintext)
plt.show()
