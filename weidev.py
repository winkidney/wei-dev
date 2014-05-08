#!/usr/bin/env python
#coding:utf-8
#weidev.py - GUI development tools for weichat development
#version 0.1 - by winkidney -2014-05-08

import sys
from PyQt4.QtCore import *  
from PyQt4.QtGui import * 
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  

class Example(QDialog):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
    def build_list(self):
        msg_type = QStringList()  
        msg_type.append(self.tr("文本"))  
        msg_type.append(self.tr("女"))
        return    
    def build_radios(self):
        radios = QButtonGroup(self)
        radio_list = ['text',
                      'image',
                      'rich_text',
                      'event',
                      ]
    def initUI(self):      
        
        label_post = QLabel(self.tr("请求地址："))
        self.line_post_url = QLineEdit(self)
        
        label_send = QLabel(self.tr("发出的信息"))
        self.msg_send_area = QTextEdit("", self)
        
        label_response = QLabel(self.tr("响应正文"))
        self.msg_response_area = QTextEdit("", self)
        
        self.postit = QPushButton(self.tr("提交请求"), self)
        self.postit.WidgetWidth = 60
        
        self.postit.clicked.connect(self.send_msg)
        
        layout=QGridLayout()
        
        layout.addWidget(label_post, 0, 0)
        layout.addWidget(self.line_post_url, 0, 1)
        
        layout.addWidget(label_send, 1, 0)
        layout.addWidget(self.msg_send_area, 1,1)
        
        layout.addWidget(label_response, 1, 2)
        layout.addWidget(self.msg_response_area, 1, 3)
        
        layout.addWidget(self.postit, 2,1)
        
        self.setLayout(layout)
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle('WeiDev Tools - by winkidney')
        self.show()
        
    def send_msg(self):
        text = self.msg_send_area.toPlainText()
        self.msg_response_area.setText(self.tr(text))

    def set_send_area(self,text):
        self.msg_send_area.setText(self.tr(text))
        
def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
