class Space:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
    
    def setDimensions(self, _x1, _y1, _x2, _y2):
        self.x1 = _x1
        self.y1 = _y1
        self.x2 = _x2
        self.y2 = _y2

    def getRect(self):
        return self.x1, self.y1, self.x2, self.y2

 
    def addImage(self,pdf,img):
        pdf.image(img,self.x1,self.y1,self.getWidth(), self.getHeight())
    
    #Disable this when done dividing
    def drawRect2(self, pdf):
        pdf.rect(self.x1 , self.y1 , self.getWidth(), self.getHeight())
#        self.drawTop(pdf)
#        self.drawBottom(pdf)
#        self.drawLeft(pdf)
#        self.drawRight(pdf)
    
    def drawRect(self, pdf):
        pdf.rect(self.x1 , self.y1 , self.getWidth(), self.getHeight())
#        self.drawTop(pdf)
#        self.drawBottom(pdf)
#        self.drawLeft(pdf)
#        self.drawRight(pdf)
    
    def getTop(self):
        return self.x1, self.y1, self.x2, self.y1
        
    def drawTop(self ,pdf):
        pdf.line(* self.getTop())
    
    def getBottom(self):
        return self.x1, self.y2, self.x2, self.y2
    
    def drawBottom(self, pdf):
        pdf.line(*self.getBottom())
    

    def getLeft(self):
        return self.x1, self.y1, self.x1, self.y2
        
    def drawLeft(self, pdf):
        pdf.line(*self.getLeft())

    def getRight(self):
        return self.x2, self.y1, self.x2, self.y2
        
    def drawRight(self, pdf):
        pdf.line(* self.getRight())


    def setCEllTitles(self, pdf, txt):
        pdf.set_xy ( self.x1, self.y1)
        pdf.cell(self.getWidth(), self.getHeight(), txt,0,0, 'C', False)
    
    def setCEllTitlesRJustify(self, pdf, txt):
        pdf.set_xy ( self.x1, self.y1)
        pdf.cell(self.getWidth(), self.getHeight(), txt,0,0, '', False)

    
    def getX1(self):
        return self.x1
        

    def getY1(self):
        return self.y1

    def getX2(self):
        return self.x2

    def getY2(self):
        return self.y2 

    def getWidth(self):
        return int((self.x2 - self.x1))
    
    def getHeight(self):
        _height = int(self.y2) - int(self.y1)
        return (_height)
 
    def setLeft(self, _mSpace, _len):
        if _len > _mSpace.getWidth():
            raise Exception("Sorry there is not enough space for your request")
        self.y1 = _mSpace.getY1()
        self.y2 = _mSpace.getY2()
        self.x2 = _mSpace.getX1() + _len
        self.x1 = _mSpace.getX1() 
        _ret = Space()
        _ret.setDimensions(self.getX2(),self.getY1(),_mSpace.getX2(),_mSpace.getY2())
        return _ret

    def setRight(self, _mSpace, _len):
        if _len > _mSpace.getWidth():
            raise Exception("Sorry there is not enough space for your request")
        self.y1 = _mSpace.getY1()
        self.y2 = _mSpace.getY2()
        self.x2 = _mSpace.getX2()
        self.x1 = _mSpace.getX2()  - _len
        _ret = Space()
        _ret.setDimensions(_mSpace.getX1(),_mSpace.getY1(),self.getX1(), self.getY2()  )
        return _ret  

    def setTop(self, _mSpace, _len):    
        if _len > _mSpace.getHeight():
            raise Exception("Sorry there is not enough space for your request")    
        self.x1 = _mSpace.getX1()
        self.y1 = _mSpace.getY1()
        self.x2 = _mSpace.getX2()
        self.y2 = _mSpace.getY1() + _len
        _ret = Space()
        _ret.setDimensions(self.getX1(), self.getY2(),_mSpace.getX2(),_mSpace.getY2()  )
        return _ret 
    
    def setBottom(self, _mSpace, _len):    
        if _len > _mSpace.getHeight():
            raise Exception("Sorry there is not enough space for your request")    
        self.x1 = _mSpace.getX1()
        self.y1 = _mSpace.getY2() - _len
        self.x2 = _mSpace.getX2()
        self.y2 = _mSpace.getY2() 
        _ret = Space()
        _ret.setDimensions(_mSpace.getX1(),_mSpace.getY1() ,_mSpace.getX2() , self.getY1())
        return _ret 