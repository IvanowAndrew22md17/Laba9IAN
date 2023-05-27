from PIL import Image,ImageFilter
import os
x = input("введите номер задания:")

#9.1
def f1():
    a = "1.jpg"
    b = "2.png"
    c = "3.jpg"
    d = "4.png"
    e = "5.jpg"
    g = [a, b, c, d, e]
    for file in g:
        img = Image.open(file)
        newimg = img.filter(ImageFilter.SMOOTH)
        newimg.show()
        try:
            os.mkdir("C:/Users/Запасной/Desktop/прога/Laba9IAN")
        except:
            pass
        newimg.save("C:/Users/Запасной/Desktop/прога/Laba9IAN/newimg.png")
if x==1:
    f1()

#9.2
def f2():
    a = "1.jpg"
    b = "2.png"
    c = "3.jpg"
    d = "4.png"
    e = "5.jpg"
    g = [a, b, c, d, e]
    for file in g:
        if file.endswith('.jpg') or file.endswith('.png'):
            img = Image.open(file)
            new_img = img.filter(ImageFilter.SMOOTH)
            new_img.show()
            try:
                os.mkdir("C:/Users/Запасной/Desktop/прога/Laba9IAN")
            except:
                pass
            new_img.save("C:/Users/Запасной/Desktop/прога/Laba9IAN/new_img.png")
if x==2:
    f2()

#9.3
def f3():
    t=0
    with open('data.csv', 'r') as s:
        l = s.readlines()
        print("Список:")
        for line in l[1:]:
            prod, col, pr = line.strip().split(',')
            t += int(col) * int(pr)
            print(f"{prod} - {col} шт. за {pr} руб.")
        print(f"Итого: {t} руб.")
if x==3:
    f3()
if x< 0 or x > 3:
    print("Такой задачи нет(")