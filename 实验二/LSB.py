from PIL import Image
import numpy as np

# 将字符串转换成二进制,不够8位补齐8位
def StringtoBin(data):
    bin_data = ''
    for c in data:
        temp = bin(ord(c)).replace('0b', '')
        temp = temp.rjust(8, '0')
        bin_data = bin_data + temp
    return bin_data


def encode(path, data):
    data = StringtoBin(data)
    print("二进制数据："+data)
    # 加载图片，并读取其高度和宽度
    image = Image.open(path)
    height = image.size[0]  # 高度
    width = image.size[1]  # 宽度
    count = 0
    # 密文数据长度须小于图片大小
    if width * height * 3 < len(data):
        print("数据过长，无法加密！")
        return
    image = np.array(image)
    # 遍历该三通道图片的所有像素点
    for h in range(height):
        if count == len(data):
            break
        for w in range(width):
            if count == len(data):
                break
            for c in range(3):
                channel = image[h][w][c]
                image[h][w][c] = channel - channel % 2 + eval(data[count])
                count = count + 1
                if count == len(data):
                    break
    image = Image.fromarray(image)
    image.save('encode.png')
    return count


def decode(path, key):
    data_bit = ""
    # 加载含密文的图片
    image = Image.open(path)
    height = image.size[0]
    width = image.size[1]
    image = np.array(image)
    count = 0
    # 遍历图片所有像素点
    for h in range(height):
        if count == key:
            break
        for w in range(width):
            if count == key:
                break
            for c in range(3):
                # 依次读取各像素的最低bit位，构成的数据长度等于密文长度时为止
                data_bit = data_bit + str(image[h][w][c] % 2)
                count = count + 1
                if count == key:
                    break
    print("提取到的二进制数据："+data_bit)
    data = ""
    idx = 0
    # 每8位构成一个字符
    while(True):
        if idx == len(data_bit):
            break
        a = chr(int(data_bit[idx:idx+8]))
        data = data + chr(int(data_bit[idx:idx+8], 2))
        idx = idx + 8
    print("解密信息："+data)

if __name__ == "__main__":
    img_path = r'C:\Users\PH\Desktop\a\信息安全\实验\实验二\lena.png'
    encode_img_path = r'C:\Users\PH\Desktop\a\信息安全\实验\实验二\encode.png'
    data = 'CQUWATERMASKEXP'
    key = encode(img_path, data)
    decode(encode_img_path, key)



