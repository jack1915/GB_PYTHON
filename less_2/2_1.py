if __name__ == '__main__':
    i = int(input("Введите число "))

    h = (format(i, '#x'))
    print(h)  # ('0xfff')
print(hex(i))
if hex(i) == h:
    print("Задача решена верно")
else:
    ("Задачу надо доработать")
