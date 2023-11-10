#  Задача №3

filename = ['1.txt', '2.txt', '3.txt']
filepath = [r"C:\Users\ZOLOTOV\Desktop\py-homeworks-basic-recipes\1.txt",
            r"C:\Users\ZOLOTOV\Desktop\py-homeworks-basic-recipes\2.txt",
            r"C:\Users\ZOLOTOV\Desktop\py-homeworks-basic-recipes\3.txt"]
contents = []

for file, path in zip(filename, filepath):
    with open(path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        contents.append((file, len(lines), lines))
        
contents.sort(key=lambda x: x[1])

with open('4.txt', 'w', encoding="utf-8") as f:
    for item in contents:
        f.write(f"{item[0]}\n{item[1]}\n")
        f.writelines(item[2])