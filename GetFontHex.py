from PIL import Image, ImageFont, ImageDraw
import sys


def GetData(a, b):
    image = Image.new("1", [16, 16], color=0)  # 创建黑底图片
    draw_obj = ImageDraw.Draw(image)  # 创建一个draw对象
    if b == 1:
        font = ImageFont.truetype(font_path, 16, encoding="unic")
    else:
        font = ImageFont.truetype('%WINDIR%\\Fonts\\STXINWEI.TTF', encoding="unic")

    for char in a:
        for i in range(16):
            for j in range(16):
                draw_obj.point((i, j), 0)  # 初始化图像为黑色
        draw_obj.text((0, 0), char, fill=255, font=font)  # 在图片上覆盖白色字体
        image.save("3.bmp")
        data = [0] * 32
        fstring = [""] * 32

        for x in range(32):
            for y in range(8):
                data[x] += int(image.getpixel((x % 16, y + int((x / 16)) * 8)) / 255) * (2**(y % 8))
            fstring[x] = str("0x{:02x}".format(data[x]))

        print('\n\t{' + ','.join(fstring[:16]) + ',\n\t' + ','.join(fstring[16:]) + '},' + f'//\"{char}\",')


font_path = '%WINDIR%\\Fonts\\simsun.ttc'  # 可自定义为其他字体

# 读取命令行
try:
    string = str(sys.argv[1])
    argv_flag = 1
except:
    string = str(input())
    argv_flag = 0

GetData(string, 1)
if argv_flag:
    exit(0)  # 如果命令行传入参数则处理完后结束

while True:
    try:
        string = str(input())
        GetData(string, 2)
    except KeyboardInterrupt:
        exit(0)
