from tkinter import *
import cv2
import os
import tkinter.messagebox as mesbox

class Win():
    def __init__(self):
        # 图片的名称
        self.cnt = 0
        self.img = None
        # 保存图片的主要位置
        self.root_path = "../get_imgs"
        # 界面
        self.window = Tk()
        self.no = Label(self.window)
        self.no.grid(column=0,row=0)
        self.window.title("获取图片信息")
        self.window.geometry("350x200")
        self.lbl = Label(self.window, text="请输入名字（拼音首字母大写,例：LiMing）：")
        self.lbl.grid(column=0, row=6)
        self.name = Entry(self.window, width=30)
        self.name.grid(column=0, row=10)
        self.btn = Button(self.window, text="确定", command=self.clicked)
        self.btn.grid(column=1, row=10)
        self.window.mainloop()
        # 程序

    # 检查字符串有中文
    def is_chinese(self,string):
        """
        检查整个字符串是否包含中文
        :param string: 需要检查的字符串
        :return: bool
        """
        for ch in string:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True

        return False

    def clicked(self):
        # 获取名称
        name = self.name.get()
        if name=="":
            mesbox.showerror("警告","输入框为空,请检查")
        else:
            if self.is_chinese(name):
                mesbox.showerror("警告", "输入框中含有汉字，请使用拼音")
            else:
                # print(name)
                path = os.path.join(self.root_path,name)
                # 先检查目录是否存在
                if not os.path.exists(path):
                    os.mkdir(path)
                # 进入该目录
                os.chdir(path)
                # 开始获取图片
                self.get_imgs()

                print("图片读取已结束，共保存了{}张图片".format(self.cnt))

    def get_imgs(self):
        cap = cv2.VideoCapture(0)

        while (1):
            ret, self.img = cap.read()
            cv2.rectangle(self.img, (156, 76), (484, 404), (0, 255, 0), 4)
            cv2.imshow("cap",self.img)
            cv2.setMouseCallback('cap', self.draw_circle)
            if cv2.waitKey(10) & 0xff == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


    def draw_circle(self,event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            self.cnt += 1
            new_img = self.img[80:400, 160:480]
            file_name = str(self.cnt) + '.jpg'
            out = cv2.resize(new_img, (160, 160), interpolation=cv2.INTER_AREA)
            cv2.imwrite(file_name, out)
            print("{} 图片保存成功".format(file_name))


if __name__ == '__main__':
    a = Win()
