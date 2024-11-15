from PIL import Image, ImageFont, ImageDraw
import sys


def GetData(a):
    image = Image.new("1", [16, 16], color=0)  # 创建黑底图片
    draw_obj = ImageDraw.Draw(image)  # 创建一个draw对象
    font = ImageFont.truetype('%WINDIR%\\Fonts\\simsun.ttc', 16, encoding="unic")
    for char in a:
        for i in range(16):
            for j in range(16):
                draw_obj.point((i, j), 0)
        draw_obj.text((0, 0), char, fill=255, font=font)  # 在图片上覆盖白色字体
        data = [0] * 32
        fstring = [""] * 32

        for x in range(32):
            for y in range(7, -1, -1):
                data[x] += int(image.getpixel((x % 16, y + int((x / 16)) * 8)) / 255) * (2**(y % 8))
            fstring[x] = str("0x{:02x}".format(data[x]))

        print('\n\t{' + ','.join(fstring[:16]) + ',\n\t' + ','.join(fstring[16:]) + '},' + f'//\"{char}\",')


# 读取命令行
try:
    string = str(sys.argv[1])
    argv_flag = 1
except:
    string = str(input())
    argv_flag = 0

GetData(string)
if argv_flag:
    exit(0)

while True:
    try:
        string = str(input())
        GetData(string)
    except:
        exit(0)
