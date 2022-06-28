#!python

class LetterDims:
    def __init__(self):
        self.pwidth = 612
        self.pheight= 792 
        self.intop = 72
        self.mmtop = 2.8346
        
        self.topMargin=0
        self.leftMargin=0
        self.rightMargin=0
        self.bottomMargin=0
        pass
    def set_top_margin_in(self, ln):
        self.topMargin = self.intop * ln
        
        
    def set_left_margin_in(self, ln):
        self.leftMargin = self.intop * ln    

    def set_right_margin_in(self, ln):
        self.rightMargin = self.intop * ln  
        
    def set_bottom_margin_in(self, ln):
        self.bottomMargin = self.intop * ln           
        
    def get_intop(self):
        return self.intop
        
    def get_page_width(self):
        return self.pwidth
        
    def get_page_height(self):
        return self.pheight
        
    def get_top_left_crnr_prntbl(self):
        x= self.leftMargin
        y=self.topMargin
        return x,y 
        
    def get_top_right_crnr_prntbl(self):
        y=self.topMargin
        x= self.pwidth - self.leftMargin
        return x,y
        
    def get_bottom_left_crnr_prntbl(self):
        x= self.leftMargin
        y=self.pheight - self.topMargin
        return x,y 
        
    def get_bottom_right_crnr_prntbl(self):
        x= self.pwidth - self.leftMargin
        y=self.pheight - self.topMargin
        return x,y 