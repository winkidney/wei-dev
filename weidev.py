#!/usr/bin/env python
#coding:utf-8
#weidev.py - GUI development tools for weichat development
#version 0.1 - by winkidney -2014-05-08

import sys
from PyQt4.QtCore import *  
from PyQt4.QtGui import * 
from sample_msg import (recv_msg_event,
                        recv_msg_link,
                        recv_msg_location,
                        recv_msg_video,
                        recv_msg_voice,
                        recv_msg_image,
                        recv_msg_text,
                        )
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  

class WeiDev(QDialog):
    
    def __init__(self):
        super(WeiDev, self).__init__()
        
        self.initUI()
    def build_list(self):
        msg_type = QStringList()  
        msg_type.append(self.tr(""))  
        msg_type.append(self.tr(""))
        return    
    def build_radios(self):
        tmp_layout = QVBoxLayout()
        tmp_widget = QWidget(self)
        self.type_radios = QButtonGroup(tmp_widget)
        self.radio_dict = {'text' : recv_msg_text,
                      'image' : recv_msg_image,
                      'event' : recv_msg_event,
                      'location' : recv_msg_location,
                      'voice' : recv_msg_voice,
                      'video' : recv_msg_video,
                      }
        tmp_widget.setLayout(tmp_layout)
        self.type_radios.buttonClicked.connect(self.echo_msg)
        #label_send = QLabel(self.tr("发出的信息"))
        #tmp_layout.addWidget(label_send)
        for item in self.radio_dict.items():
            radio = QRadioButton(item[0])
            #radio.clicked.connect(self.echo_msg)
            self.type_radios.addButton(radio)
            tmp_layout.addWidget(radio)
        return tmp_widget
    
    def build_info(self):
        tmp_layout = QGridLayout()
        tmp_widget = QWidget(self)
        tmp_widget.setLayout(tmp_layout)
        
        label_from = QLabel(self.tr("from-user"))
        self.line_from = QLineEdit(self)
        
        label_to = QLabel(self.tr("to-user"))
        self.line_to = QLineEdit(self)
        
        tmp_layout.addWidget(label_from, 0, 0)
        tmp_layout.addWidget(self.line_from, 0, 1)
        tmp_layout.addWidget(label_to, 1, 0)
        tmp_layout.addWidget(self.line_to, 1, 1)
        
        return tmp_widget
        
    def echo_msg(self):
        name = str(self.type_radios.checkedButton().text())
        self.current_type = name
        msg = self.radio_dict.get(name)
        if msg:
            self.msg_send_area.setText(self.tr(msg))
            
            
    def initUI(self):      
        
        label_post = QLabel(self.tr("请求地址："))
        self.line_post_url = QLineEdit(self)
        
        
        self.msg_send_area = QTextEdit("", self)
        
        label_response = QLabel(self.tr("响应正文"))
        self.msg_response_area = QTextEdit("", self)
        
        self.postit = QPushButton(self.tr("提交请求"), self)
        self.postit.WidgetWidth = 60
        
        self.postit.clicked.connect(self.send_msg)
        
        
        
        layout=QGridLayout()
        
        layout.addWidget(label_post, 0, 0)
        layout.addWidget(self.line_post_url, 0, 1)
        layout.addWidget(self.build_info(), 0, 3)
        
        layout.addWidget(self.build_radios(), 1, 0)
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
    wei_dev = WeiDev()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
