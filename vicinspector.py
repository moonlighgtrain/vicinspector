#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:ChenK
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
# OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.
给VIC软件的z3d文件添加提取工具
"""
import sys,os,argparse,shutil,copy
import lxml.etree as etree
import zipfile
from zipfile import PyZipFile
#点类
class Point:
    lri_tag = "inspector_point"
    label_tag = "P"
    count = 0
    ref_pos = "1000 1000"
    rt = "ref_pos"
    def __init__(self,count1,ref_pos1):
        self.count = count1
        if isinstance(ref_pos1,list):
            self.ref_pos = " ".join(ref_pos1)
        
    def getElement(self):
        element = None
        root = None
        if self.count == 0:
            root = etree.Element(self.lri_tag,lri = self.lri_tag,label = self.label_tag+str(self.count))
            element = etree.SubElement(root,self.rt)
            element.text = self.ref_pos
        else:
            root = etree.Element(self.lri_tag,lri = "_".join([self.lri_tag,str(self.count-1)]),label = self.label_tag+str(self.count))
            element = etree.SubElement(root,self.rt)
            element.text = self.ref_pos
        return root
#圆形类
class Circle:
    lri_tag = "inspector_disc"
    label_tag = "C"
    count = 0
    ref_pos = "1000 1000"
    rt = "ref_pos"
    raduis = "50"
    def __init__(self,count1,ref_pos1,radius1):
        self.count = count1
        self.radius = radius1
        if isinstance(ref_pos1,list):
            self.ref_pos = " ".join(ref_pos1)    
    def getElement(self):
        element = None
        root = None
        if self.count == 0:
            root = etree.Element(self.lri_tag,lri = self.lri_tag,label = self.label_tag+str(self.count),radius=self.radius)
            element = etree.SubElement(root,self.rt)
            element.text = self.ref_pos
        else:
            root = etree.Element(self.lri_tag,lri = "_".join([self.lri_tag,str(self.count-1)]),label = self.label_tag+str(self.count),radius=self.radius)
            element = etree.SubElement(root,self.rt)
            element.text = self.ref_pos
        return root
#矩形类
class Rectangular:
    lri_tag = "inspector_rect"
    label_tag = "R"
    count = 0
    ref_pos = "1000 1000"
    rt = "ref_pos"
    height = "50"
    width = "50"
    def __init__(self,count1,ref_pos1,height1,width1):
        self.count = count1
        self.height = height1
        self.width = width1
        if isinstance(ref_pos1,list):
            self.ref_pos = " ".join(ref_pos1)    
    def getElement(self):
        element = None
        root = None
        if self.count == 0:
            root = etree.Element(self.lri_tag,lri = self.lri_tag,label = self.label_tag+str(self.count),height=self.height,width=self.width)
            element = etree.SubElement(root,self.rt)
            element.text = self.ref_pos
        else:
            root = etree.Element(self.lri_tag,lri = "_".join([self.lri_tag,str(self.count-1)]),label = self.label_tag+str(self.count),height=self.height,width=self.width)
            element = etree.SubElement(root,self.rt)
            element.text = self.ref_pos
        return root
#引伸计类
class Extensometer:
    lri_tag = "inspector_extensometer"
    label_tag = "E"
    count = 0
    ref_pos = "1000 1000 1000 1200"
    rt = "ref_pos"
    def __init__(self,count1,ref_pos1):
        self.count = count1
        if isinstance(ref_pos1,list):
            self.ref_pos = " ".join(ref_pos1)    
    def getElement(self):
        element = None
        root = None
        if self.count == 0:
            root = etree.Element(self.lri_tag,lri = self.lri_tag,label = self.label_tag+str(self.count))
            element = etree.SubElement(root,self.rt)
            element.text = self.ref_pos
        else:
            root = etree.Element(self.lri_tag,lri = "_".join([self.lri_tag,str(self.count-1)]),label = self.label_tag+str(self.count))
            element = etree.SubElement(root,self.rt)
            element.text = self.ref_pos
        return root    
#直线类
class Line:
    lri_tag = "inspector_line"
    label_tag = "L"
    count = 0
    ref_pos = "1000 1000 1000 1200"
    rt = "ref_pos"
    def __init__(self,count1,ref_pos1):
        self.count = count1
        if isinstance(ref_pos1,list):
            self.ref_pos = " ".join(ref_pos1)    
    def getElement(self):
        element = None
        root = None
        if self.count == 0:
            root = etree.Element(self.lri_tag,lri = self.lri_tag,label = self.label_tag+str(self.count))
            element = etree.SubElement(root,self.rt)
            element.text = self.ref_pos
        else:
            root = etree.Element(self.lri_tag,lri = "_".join([self.lri_tag,str(self.count-1)]),label = self.label_tag+str(self.count))
            element = etree.SubElement(root,self.rt)
            element.text = self.ref_pos
        return root    
class Polygon():
    lri_tag = "inspector_polygon"
    label_tag = "S"
    count = 0
    ref_pos = "1000 1000 1200 1000 1050 900"
    rt = "ref_pos"
    def __init__(self,count1,ref_pos1):
        self.count = count1
        if isinstance(ref_pos1,list):
            self.ref_pos = " ".join(ref_pos1)    
    def getElement(self):
        element = None
        root = None
        if self.count == 0:
            root = etree.Element(self.lri_tag,lri = self.lri_tag,label = self.label_tag+str(self.count))
            element = etree.SubElement(root,self.rt)
            element.text = self.ref_pos
        else:
            root = etree.Element(self.lri_tag,lri = "_".join([self.lri_tag,str(self.count-1)]),label = self.label_tag+str(self.count))
            element = etree.SubElement(root,self.rt)
            element.text = self.ref_pos
        return root           
#使用方法

def usage():
    print('''
使用方法：
vicinspector脚本是用于z3d文件添加提取工具，用法是
vicinspector [C\\:z3d文件路径\test.z3d]
''')
#检查文件路径
def checkFilePath(filePath):
    #filePath=' '.join(sys.argv[1:])
    print("输入的文件路径为"+str(filePath))
    if not os.path.exists(filePath):
        print("输入的文件路径不存在，请确认")
        sys.exit()
    elif os.path.isfile(filePath):
        if not os.path.basename(filePath).endswith(".z3d"):
            print("输入的文件不是z3d文件，请确认")
            sys.exit()
    else:
        print("输入的路径为文件夹，请确认")
        sys.exit()
#打印xml单元列表
def printElement(xmlElement):
    for i in xmlElement:
        print(etree.tostring(i,pretty_print=True))
#找到label最大值,并返回Element下标
def findMaxLabel(xmlElement):
    index = 0
    value = 0
    if existElement(xmlElement):
        for i in range(0,len(xmlElement)):
            label = xmlElement[i].get("label")
            label = int(label[1:])
            if int(label) > value:
                value = int(label)
                index = i
        value+=1
    return [index,value] 
#判断元素是否存在
def existElement(element):
    if len(element) == 0:
        return False
    return True
#备份.z3d文件
def bakZ3d(filePath):
    filedir = os.path.dirname(filePath)
    filebase = os.path.basename(filePath)
    newbase = "".join(filebase.split(".z3d")+["_bak",".z3d"])
    newfile = os.path.join(filedir,newbase)
    if os.path.exists(newfile):
        return "备份文件已存，跳过备份"
    else:
        shutil.copy(filePath,newfile)
        return "已备份原文件，后缀为_bak"
#把xml写入z3d
def writeFile(filepath,root):
    s = etree.tostring(root, encoding="utf-8", xml_declaration=True,pretty_print=True, doctype='<!DOCTYPE vpml>').decode('utf-8')
    # Save the xml inside a zip archive
    your_delet_file="project.xml"
    #old_zipfile='archive.zip' #新文件
    new_zipfile='new.z3d' #新文件
    #filebase = os.path.basename(filepath)
    #newbase = "".join(filebase.split(".z3d")+["_new",".z3d"])
    #newfile = os.path.join(filedir,newbase)
    zin = zipfile.ZipFile (filepath, 'r') #读取对象
    zout = zipfile.ZipFile (new_zipfile, 'w') #被写入对象
    for item in zin.infolist():
        buffer = zin.read(item.filename)
        if (item.filename!= your_delet_file): #剔除要删除的文件
            zout.writestr(item, buffer) #把文件写入到新对象中
    #用新文件覆盖旧文件
    zout.writestr("project.xml", s)
    zout.close()
    zin.close()
    shutil.move(new_zipfile,filepath)
    
    print("已完成写入操作")
#点增加业务
def addPoint(root,position):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_point")  
        index,maxCount=findMaxLabel(inspectorElement)
        #print(inspectorElement)
        lenP = len(position)
        if lenP <= 2:
            CPoint =Point(maxCount,position)
            addElement = CPoint.getElement()
            i.append(addElement)
        elif lenP%2 == 0:
            for j in range(0,lenP,2):
                PoTemp = [position[j],position[j+1]]
                CPoint =Point(maxCount,PoTemp)
                addElement = CPoint.getElement()
                i.append(addElement)
                maxCount +=1
        else:
            print("输入的position位置x y有误，不是偶数对，请检查")
            sys.exit()
        #print(type(CPoint.getElement()))
        #print(type(inspectorElement))
        #print(etree.tostring(CPoint.getElement(),pretty_print=True))
        #printElement(root)
        
        #printElement(inspectorElement)
#圆增加业务
def addCircle(root,position,radius):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_disc")  
        index,maxCount=findMaxLabel(inspectorElement)
        #print(inspectorElement)
        lenP = len(position)
        if lenP <= 2:
            ClassTemp =Circle(maxCount,position,radius)
            addElement = ClassTemp.getElement()
            i.append(addElement)
        elif lenP%2 == 0:
            for j in range(0,lenP,2):
                PoTemp = [position[j],position[j+1]]
                ClassTemp =Circle(maxCount,PoTemp,radius)
                addElement = ClassTemp.getElement()
                i.append(addElement)
                maxCount +=1
        else:
            print("输入的position位置x y有误，不是偶数对，请检查")
            sys.exit()        
        #printElement(root)
#矩形增加业务
def addRectangular(root,position,height,width):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_rect")  
        index,maxCount=findMaxLabel(inspectorElement)
        #print(inspectorElement)
        lenP = len(position)
        if lenP <= 2:
            ClassTemp =Rectangular(maxCount,position,height,width)
            addElement = ClassTemp.getElement()
            i.append(addElement)
        elif lenP%2 == 0:
            for j in range(0,lenP,2):
                PoTemp = [position[j],position[j+1]]
                ClassTemp =Rectangular(maxCount,PoTemp,height,width)
                addElement = ClassTemp.getElement()
                i.append(addElement)
                maxCount +=1
        else:
            print("输入的position位置x y有误，不是偶数对，请检查")
            sys.exit()        
        #printElement(root)
#引伸计增加业务
def addExtensometer(root,position):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_extensometer")  
        index,maxCount=findMaxLabel(inspectorElement)
        #print(inspectorElement)
        lenP = len(position)
        '''
        if lenP <= 4:
            ClassTemp =Extensometer(maxCount,position)
            addElement = ClassTemp.getElement()
            i.append(addElement)
        '''
        if lenP%4 == 0:
            for j in range(0,lenP,4):
                PoTemp = [position[j],position[j+1],position[j+2],position[j+3]]
                ClassTemp =Extensometer(maxCount,PoTemp)
                addElement = ClassTemp.getElement()
                i.append(addElement)
                maxCount +=1
        else:
            print("输入的position位置x1 y1 x2 y2有误，不是偶数对，请检查")
            sys.exit()        
        #printElement(root)    
def addLine(root,position):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_line")  
        index,maxCount=findMaxLabel(inspectorElement)
        #print(inspectorElement)
        lenP = len(position)
        if lenP < 4:
            '''
            ClassTemp =Extensometer(maxCount,position)
            addElement = ClassTemp.getElement()
            i.append(addElement)
            '''
            print("输入的position位置x1 y1 x2 y2有误，少于4个，不是偶数对，请检查")
            sys.exit()
        elif lenP%2 == 0:
            '''
            for j in range(0,lenP,2):
                PoTemp = [position[j],position[j+1],position[j+2],position[j+3]]
                ClassTemp =Extensometer(maxCount,PoTemp)
                addElement = ClassTemp.getElement()
                i.append(addElement)
                maxCount +=1
            '''
            ClassTemp =Line(maxCount,position)
            addElement = ClassTemp.getElement()
            i.append(addElement)
        else:
            print("输入的position位置x1 y1 x2 y2……有误，不是偶数对，请检查")
            sys.exit()        
#多边形增加业务
def addPolygon(root,position):
     #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_polygon")  
        index,maxCount=findMaxLabel(inspectorElement)
        #print(inspectorElement)
        lenP = len(position)
        if lenP < 6:
            '''
            ClassTemp =Extensometer(maxCount,position)
            addElement = ClassTemp.getElement()
            i.append(addElement)
            '''
            print("输入的position位置x1 y1 x2 y2 x3 y3……有误，少于6个，不是偶数对，请检查")
            sys.exit()
        elif lenP%2 == 0:
            '''
            for j in range(0,lenP,2):
                PoTemp = [position[j],position[j+1],position[j+2],position[j+3]]
                ClassTemp =Extensometer(maxCount,PoTemp)
                addElement = ClassTemp.getElement()
                i.append(addElement)
                maxCount +=1
            '''
            ClassTemp =Polygon(maxCount,position)
            addElement = ClassTemp.getElement()
            i.append(addElement)
        else:
            print("输入的position位置x1 y1 x2 y2 x3 y3……有误，不是偶数对，请检查")
            sys.exit()     
#检查复制元素
def checkCopyElement(inspectorElement):
    if not existElement(inspectorElement):
            print("缺少需要复制的源工具，请在.z3d文件中创建一个需要复制的工具")
            return False
    return True

             
#复制点业务
def copyPoint(root,step,number):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    I=int(number[0])
    #stepList = " ".split(step)
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_point")  
        index,maxCount=findMaxLabel(inspectorElement)
        if checkCopyElement(inspectorElement):
            for j in inspectorElement:
                #找到当前工具单元的编号
                #count = int(j.get("label")[1:0])+1
                #print(j[0].text)
                position = j[0].text.split(" ")
                #print(len(position))
                #print(position[0],position[1])
                #temp =0

                for k in range(maxCount,maxCount+I):
                    #temp +=1
                    #print(position[0],step[0])
                    position[0] = str(float(position[0])+float(step[0]))
                    position[1] = str(float(position[1])+float(step[1]))
                    ClassTemp = Point(k,position)
                    addElement = ClassTemp.getElement()
                    i.append(addElement)
                maxCount = maxCount+I
        
            
        #print(inspectorElement)
        #lenP = len(position)
        '''
        if lenP <= 2:
            CPoint =Point(maxCount,position)
            addElement = CPoint.getElement()
            i.append(addElement)
        elif lenP%2 == 0:
            for j in range(0,lenP,2):
                PoTemp = [position[j],position[j+1]]
                CPoint =Point(maxCount,PoTemp)
                addElement = CPoint.getElement()
                i.append(addElement)
                maxCount +=1
        else:
            print("输入的position位置x y有误，不是偶数对，请检查")
            sys.exit()    
        '''
#点阵列复制业务
def arrayCopyPoint(root,step,number):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    I=int(number[0])
    #stepList = " ".split(step)
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_point")  
        index,maxCount=findMaxLabel(inspectorElement)
        if checkCopyElement(inspectorElement):
            for j in inspectorElement:
                position = j[0].text.split(" ")
                xTemp = position[0]
                yTemp = position[1]
                for k in range(maxCount+1,maxCount+I+2):       
                    for l in range(maxCount+1,maxCount+I+2):
                        #temp +=1
                        #print(position[0],step[0])
                        if xTemp == position[0] and yTemp == position[1]:
                            xTemp = str(float(xTemp)+float(step[0]))
                            maxCount-=1
                            continue
                        maxCount+=1
                        ClassTemp = Point(maxCount,[xTemp,yTemp])
                        addElement = ClassTemp.getElement()
                        i.append(addElement)
                        xTemp = str(float(xTemp)+float(step[0]))
                    yTemp = str(float(yTemp)+float(step[1]))
                    xTemp = position[0]
                #maxCount = maxCount+I
#圆阵列复制业务
def arrayCopyCircle(root,step,number):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    I=int(number[0])
    #stepList = " ".split(step)
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_disc")  
        index,maxCount=findMaxLabel(inspectorElement)
        if checkCopyElement(inspectorElement):
            for j in inspectorElement:
                position = j[0].text.split(" ")
                radius = j.get("radius")
                xTemp = position[0]
                yTemp = position[1]
                for k in range(maxCount+1,maxCount+I+2):       
                    for l in range(maxCount+1,maxCount+I+2):
                        #temp +=1
                        #print(position[0],step[0])
                        if xTemp == position[0] and yTemp == position[1]:
                            xTemp = str(float(xTemp)+float(step[0]))
                            maxCount-=1
                            continue
                        maxCount+=1
                        ClassTemp = Circle(maxCount,[xTemp,yTemp],radius)
                        addElement = ClassTemp.getElement()
                        i.append(addElement)
                        xTemp = str(float(xTemp)+float(step[0]))
                    yTemp = str(float(yTemp)+float(step[1]))
                    xTemp = position[0]                    
#圆复制业务
def copyCircle(root,step,number):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    I=int(number[0])
    #stepList = " ".split(step)
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_disc")  
        index,maxCount=findMaxLabel(inspectorElement)
        if checkCopyElement(inspectorElement):
            for j in inspectorElement:
                position = j[0].text.split(" ")
                radius = j.get("radius")
                for k in range(maxCount,maxCount+I):
                    position[0] = str(float(position[0])+float(step[0]))
                    position[1] = str(float(position[1])+float(step[1]))
                    ClassTemp = Circle(k,position,radius)
                    addElement = ClassTemp.getElement()
                    i.append(addElement)
                maxCount = maxCount+I
#矩形复制业务
def copyRectangular(root,step,number):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    I=int(number[0])
    #stepList = " ".split(step)
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_rect")  
        index,maxCount=findMaxLabel(inspectorElement)
        if checkCopyElement(inspectorElement):
            for j in inspectorElement:
                position = j[0].text.split(" ")
                height = j.get("height")
                width = j.get("width")
                for k in range(maxCount,maxCount+I):
                    position[0] = str(float(position[0])+float(step[0]))
                    position[1] = str(float(position[1])+float(step[1]))
                    """
                    print("k=",k)
                    print("maxCount=",maxCount)
                    print("number=",I)
                    """
                    ClassTemp = Rectangular(k,position,height,width)
                    addElement = ClassTemp.getElement()
                    i.append(addElement)
                maxCount = maxCount+I    
#矩形阵列复制业务
def arrayCopyRectangular(root,step,number):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    I=int(number[0])
    #stepList = " ".split(step)
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_rect")  
        index,maxCount=findMaxLabel(inspectorElement)
        if checkCopyElement(inspectorElement):
            for j in inspectorElement:
                position = j[0].text.split(" ")
                height = j.get("height")
                width = j.get("width")
                xTemp = position[0]
                yTemp = position[1]
                for k in range(maxCount+1,maxCount+I+2):       
                    for l in range(maxCount+1,maxCount+I+2):
                        #temp +=1
                        #print(position[0],step[0])
                        if xTemp == position[0] and yTemp == position[1]:
                            xTemp = str(float(xTemp)+float(step[0]))
                            maxCount-=1
                            continue
                        maxCount+=1
                        ClassTemp = Rectangular(maxCount,[xTemp,yTemp],height,width)
                        addElement = ClassTemp.getElement()
                        i.append(addElement)
                        xTemp = str(float(xTemp)+float(step[0]))
                    yTemp = str(float(yTemp)+float(step[1]))
                    xTemp = position[0]                          
#引伸计复制业务
def copyExtensometer(root,step,number):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    I=int(number[0])
    #stepList = " ".split(step)
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_extensometer")  
        index,maxCount=findMaxLabel(inspectorElement)
        if checkCopyElement(inspectorElement):
            for j in inspectorElement:
                position = j[0].text.split(" ")
                for k in range(maxCount,maxCount+I):
                    position[0] = str(float(position[0])+float(step[0]))
                    position[1] = str(float(position[1])+float(step[1]))
                    position[2] = str(float(position[2])+float(step[0]))
                    position[3] = str(float(position[3])+float(step[1]))
                    ClassTemp = Extensometer(k,position)
                    addElement = ClassTemp.getElement()
                    i.append(addElement)
                maxCount = maxCount+I  
#引伸计阵列复制业务
def arrayCopyExtensometer(root,step,number):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    I=int(number[0])
    #stepList = " ".split(step)
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_extensometer")  
        index,maxCount=findMaxLabel(inspectorElement)
        if checkCopyElement(inspectorElement):
            for j in inspectorElement:
                position = j[0].text.split(" ")
                xTemp = position[0]
                yTemp = position[1]
                xTemp2 = position[2]
                yTemp2 = position[3]
                for k in range(maxCount+1,maxCount+I+2):       
                    for l in range(maxCount+1,maxCount+I+2):
                        #temp +=1
                        #print(position[0],step[0])
                        if xTemp == position[0] and yTemp == position[1] and xTemp2==position[2] and yTemp2 == position[3]:
                            xTemp = str(float(xTemp)+float(step[0]))
                            xTemp2 = str(float(xTemp2)+float(step[0]))
                            maxCount-=1
                            continue
                        maxCount+=1
                        ClassTemp = Extensometer(maxCount,[xTemp,yTemp,xTemp2,yTemp2])
                        addElement = ClassTemp.getElement()
                        i.append(addElement)
                        xTemp = str(float(xTemp)+float(step[0]))
                        xTemp2 = str(float(xTemp2)+float(step[0]))
                    yTemp = str(float(yTemp)+float(step[1]))
                    yTemp2 = str(float(yTemp2)+float(step[1]))
                    xTemp = position[0]
                    xTemp2 = position[2]                           
#直线复制业务
def copyLine(root,step,number):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    I=int(number[0])
    #stepList = " ".split(step)
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_line")  
        index,maxCount=findMaxLabel(inspectorElement)
        if checkCopyElement(inspectorElement):
            for j in inspectorElement:
                position = j[0].text.split(" ")
                
                for k in range(maxCount,maxCount+I):
                    '''
                    position[0] = str(float(position[0])+float(step[0]))
                    position[1] = str(float(position[1])+float(step[1]))
                    position[2] = str(float(position[2])+float(step[0]))
                    position[3] = str(float(position[3])+float(step[1]))
                    '''
                    for l in range(0,len(position),2):
                        position[l] = str(float(position[l])+float(step[0]))
                        position[l+1] = str(float(position[l+1])+float(step[1]))
                    ClassTemp = Line(k,position)
                    addElement = ClassTemp.getElement()
                    i.append(addElement)
                maxCount = maxCount+I  
#直线阵列复制业务
def arrayCopyLine(root,step,number):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    I=int(number[0])
    #stepList = " ".split(step)
    for i in plotdataElement:
        inspectorElement = i.xpath("./inspector_line")  
        index,maxCount=findMaxLabel(inspectorElement)
        if checkCopyElement(inspectorElement):
            for j in inspectorElement:
                position = j[0].text.split(" ")
                '''
                xTemp = position[0]
                yTemp = position[1]
                xTemp2 = position[2]
                yTemp2 = position[3]
                '''
                Temp = copy.copy(position)
                for k in range(maxCount+1,maxCount+I+2):       
                    for l in range(maxCount+1,maxCount+I+2):
                        #temp +=1
                        #print(position[0],step[0])
                     
                
                        if Temp == position:
                            for m in range(0,len(position),2):
                                Temp[m]=str(float(Temp[m])+float(step[0]))
                            maxCount-=1
                            continue
                        maxCount+=1
                        ClassTemp = Line(maxCount,Temp)
                        addElement = ClassTemp.getElement()
                        i.append(addElement)
                        for m in range(0,len(position),2):
                            Temp[m]=str(float(Temp[m])+float(step[0]))
                        '''
                        xTemp = str(float(xTemp)+float(step[0]))
                        
                        xTemp2 = str(float(xTemp2)+float(step[0]))
                    '''
                    for m in range(0,len(position),2):
                       Temp[m+1]=str(float(Temp[m+1])+float(step[1]))
                       Temp[m]=position[m]
                    '''
                    yTemp = str(float(yTemp)+float(step[1]))
                    yTemp2 = str(float(yTemp2)+float(step[1]))
                    xTemp = position[0]
                    xTemp2 = position[2]
                    '''
#设置完美绘图
def setColormap(root):
    #找到plotdata元素
    plotdataElement = root.xpath("/project/plotdata")
    for i in plotdataElement:
        Element = i.xpath("./option[@name='color_map_ncol']") 
        Element[0].set("value","256")
        Element = i.xpath("./option[@name='contour_labels']")
        Element[0].set("value","16")
        Element = i.xpath("./option[@name='opacity']")
        Element[0].set("value","1") 
        Element = i.xpath("./option[@name='strain_unit']")
        Element[0].set("value","1")
        
#主程序
#命令流输入z3d文件名

filePath = None
__desc__ = '''
使用方法：
vicinspector脚本是用于z3d文件添加提取工具，用法是
vicinspector [C\\:z3d文件路径\test.z3d] -t 点 -m 复制
'''
parser = argparse.ArgumentParser(prog="vicinspector",usage="%(prog)s .z3d文件路径 -t 矩形 -m 复制 -s 100 0 -n 2", description=__desc__,epilog="---结束---")
parser.add_argument("-v","--version",help = "显示版本信息",action="version",version="%(prog)s 1.0")
parser.add_argument("filePath",help = ".z3d文件路径",nargs = "+", default = " ", type = str)
parser.add_argument("-t", "--tool", help = "查询工具类型：点、直线、圆、矩形、引伸计、多边形，默认矩形", nargs = '?',default = "矩形",type = str,dest = "tool")
parser.add_argument("-m","--mode", help = "模式：增加、复制，阵列复制，默认复制", nargs= '?', default = "复制",type = str, dest = "mode")
parser.add_argument("-p", "--position", help = "工具位于图像像素位置（x y）：默认1000 1000，即图像上水平位置1000垂直位置1000",nargs = "+",default = "1000 1000", type = str, dest = "position", required = False)
parser.add_argument("-s", "--step", help ="复制工具的像素步长（x y）：默认0 0", nargs="+",default = "100 100", type = str, dest = "step", required = False )
parser.add_argument("-n", "--number", help = "复制工具个数：默认1",nargs = "?", default = "1", type = str, dest = "number", required = False)
parser.add_argument("-r","--radius",help = "圆形工具半径（像素），默认50",nargs = "?",default = "50",type = str,dest="radius",required=False)
parser.add_argument("-u","--height",help="矩形工具高度（像素），默认50",nargs="?",default="50",type=str,dest="height",required=False)
parser.add_argument("-w","--width",help=r"矩形工具宽度（像素）,默认50",nargs="?",default="50",type=str,dest="width",required=False)
parser.add_argument("--colormap",help="完美绘图",action="store_true",dest="colormap",required=False)
args = parser.parse_args()
filePath = " ".join(args.filePath)
if filePath == ' ':
    print("没有输入文件路径，请输入vicinspector -h获取帮助")
    sys.exit()
checkFilePath(filePath)
'''
try:
    options, args = getopt.getopt(sys.argv[1:],"hp:",["help"])
except getopt.GetoptError as optError:
    print("输入命令行有错误，请检查"+optError)
    sys.exit()
for name, value in options:
    if name in ('-h','--help'):
        usage()
        sys.exit()
    if name in ('-p',):
        #filePath = value
        #checkFilePath(filePath)
        pass
filePath = ' '.join(args)
if filePath == ' ':
    print("没有输入文件路径，请输入vicinspector -h获取帮助")
    sys.exit()
checkFilePath(filePath)
'''
'''
if len(sys.argv)<2:
    print("没有输入z3d文件路径，请使用命令流：vicinspector [C\\:z3d文件路径\test.z3d]")
    time.sleep(2)
    sys.exit()
else:
    filePath=' '.join(sys.argv[1:])
    print("输入的文件路径为"+str(filePath))

#检查z3d文件是否存在，读取z3d文件
if not os.path.exists(filePath):
    print("输入的文件路径不存在，请确认")
    sys.exit()
elif os.path.isfile(filePath):
    if not os.path.basename(filePath).endswith(".z3d"):
        print("输入的文件不是z3d文件，请确认")
        sys.exit()
else:
    print("输入的路径为文件夹，请确认")
    sys.exit()
'''    
    
#读取project.xml
zipF = PyZipFile(filePath, 'r')
parser = etree.XMLParser(remove_blank_text=True)
root = etree.fromstring(zipF.read("project.xml"), parser)
zipF.close()
#判断模式
if args.colormap:
    setColormap(root)
if args.tool == "点" and args.mode == "增加":
    print("进入点增加")
    addPoint(root,args.position)
elif args.tool == "圆" and args.mode == "增加":
    print(args.tool,args.mode,sep=" ")
    addCircle(root,args.position,args.radius)
elif args.tool == "矩形" and args.mode == "增加":
    print(args.tool,args.mode,sep=" ")
    addRectangular(root,args.position,args.height,args.width)
elif args.tool == "引伸计" and args.mode =="增加":
    print(args.tool,args.mode,sep=" ")
    addExtensometer(root,args.position)
elif args.tool == "直线" and args.mode == "增加":
    print(args.tool,args.mode,sep=" ")
    addLine(root,args.position)
elif args.tool == "多边形" and args.mode == "增加":
    print(args.tool,args.mode,sep=" ")
    addPolygon(root,args.position)
elif args.tool == "点" and args.mode == "复制":
    print(args.tool,args.mode,sep=" ")
    copyPoint(root,args.step,args.number)
elif args.tool == "点" and args.mode == "阵列复制":
    print(args.tool,args.mode,sep=" ")
    arrayCopyPoint(root,args.step,args.number)  
elif args.tool == "圆" and args.mode == "阵列复制":
    print(args.tool,args.mode,sep=" ")
    arrayCopyCircle(root,args.step,args.number)
elif args.tool == "圆" and args.mode == "复制":
    print(args.tool,args.mode,sep=" ") 
    copyCircle(root,args.step,args.number)
elif args.tool == "矩形" and args.mode == "复制":
    print(args.tool,args.mode,sep=" ")
    copyRectangular(root,args.step,args.number)
elif args.tool == "矩形" and args.mode == "阵列复制":
    print(args.tool,args.mode,sep=" ")
    arrayCopyRectangular(root,args.step,args.number)
elif args.tool == "引伸计" and args.mode == "复制":
    print(args.tool,args.mode,sep=" ")
    copyExtensometer(root,args.step,args.number) 
elif args.tool == "引伸计" and args.mode == "阵列复制":
    print(args.tool,args.mode,sep=" ")
    arrayCopyExtensometer(root,args.step,args.number)
elif args.tool == "直线" and args.mode == "复制":
    print(args.tool,args.mode,sep=" ")
    copyLine(root,args.step,args.number) 
elif args.tool == "直线" and args.mode == "阵列复制":
    print(args.tool,args.mode,sep=" ")
    arrayCopyLine(root,args.step,args.number)
    #print(etree.tostring(root))
#复制原来的.z3d为备份，把新的project.xml写入文件
print(bakZ3d(filePath))
writeFile(filePath,root)
#找到plotdata元素
'''
plotdataElement = root.xpath("/project/plotdata")
for i in [plotdataElement[0]]:
    inspectorElement = i.xpath("./inspector_point")
 
    index,maxCount=findMaxLabel(inspectorElement)
    CPoint =Point(maxCount,args.position)
    #print(type(CPoint.getElement()))
    print(type(inspectorElement))
    print(etree.tostring(CPoint.getElement(),pretty_print=True))
    #printElement(CPoint.getElement())
    
    printElement(inspectorElement)
'''   
#print(etree.tostring(plotdataElement[1]))
#print(type(root.xpath("//inspector_point")))
#iPoints = root.xpath("//inspector_point")
#s = etree.tostring(root)
#print(s)
#for i in iPoints:
#    print(etree.tostring(i))
#修改project.xml

