from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
def func_open() :
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    photo2 = PhotoImage(file = filename)
    print("사진의 크기 가로 세로 크기 : %d x %d"%(photo.width(),photo.height()))
    print("사진의 크기 가로 세로 크기 : %d x %d"%(photo2.width(),photo2.height()))
    # print("사진의 0,0의 좌표의 RGB값을 튜플로 보자 : %s" % photo.get(0,0))
    print(photo.get(0,0))
    print(photo2.get(0,0))
    pLabel.configure(image = photo)
    pLabel.image = photo
    
    width = photo2.width()
    height = photo2.height()
    for y in range(height) :
        for x in range(width) :
            r, g, b = photo2.get(x, y)
            grey = int((r+g+b)/3)
            photo2.put("#%02x%02x%02x" % (grey, grey, grey), (x, y))

    pLabel2.configure(image = photo2)
    pLabel2.image = photo2
    

def func_exit() :
    window.quit()
    window.destroy()

## 메인 코드  부분 ##
window = Tk()
window.geometry("500x500")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel2 = Label(window, image = photo)
pLabel.pack(expand=1, anchor = CENTER, side=LEFT)
pLabel2.pack(expand=1, anchor = CENTER, side=RIGHT)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.mainloop()
