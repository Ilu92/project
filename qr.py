import pyqrcode  # импорт библиотеки  

string = "Not long ago I only started learning python" # название строки которую хотим написать

url = pyqrcode.create(string)

url.png("one.png", scale=100) # название картинки и размер знака