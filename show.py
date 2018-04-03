import sys
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets, QtGui
from main import Ui_Dialog
from recognise import faceRecognise

import requests
import cv2

class mywindow(QtWidgets.QWidget,Ui_Dialog):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        
    def openImage(self):    # 打开文件路径 设置文件扩展名过滤,注意用双分号间隔
        img_path,imgType= QFileDialog.getOpenFileName(self,"打开图片", "",
                                                 " All Files (*);;*.jpg;;*.png;;*.jpeg;;*.bmp")

        #利用qlabel显示图片
        png = QtGui.QPixmap(img_path).scaled(self.label_input.width(), self.label_input.height())
        self.label_input.setPixmap(png)
        results,img=faceRecognise(img_path)
        png=draw_output(img)
        self.label_output.setPixmap(png.scaled(self.label_output.width(), self.label_output.height()))
        self.label_result.setText(results)

    def recognise(self):
        pic_path="data/web_url.jpg"
        web_url=self.lineEdit_url.text()
        response=requests.get(web_url)
        picture = open(pic_path, "wb")
        picture.write(response.content)
        png = QtGui.QPixmap(pic_path).scaled(self.label_input.width(), self.label_input.height())
        self.label_input.setPixmap(png)
        results,img=faceRecognise(pic_path)
        png=draw_output(img)
        self.label_output.setPixmap(png.scaled(self.label_output.width(), self.label_output.height()))
        self.label_result.setText(results)
  
                
def draw_output(img):
    height, width, bytesPerComponent = img.shape
    bytesPerLine = 3 * width
    QImg = QtGui.QImage(img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
    png=QtGui.QPixmap.fromImage(QImg)
    return png
        

app = QtWidgets.QApplication(sys.argv)

window = mywindow()
window.show()
sys.exit(app.exec_())


