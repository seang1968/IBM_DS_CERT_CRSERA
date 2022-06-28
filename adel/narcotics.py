import pandas as pd
import openpyxl as xl
from openpyxl import workbook as wbk
import datetime
from dateutil.relativedelta import *
from dateutil.rrule import *
from dateutil.relativedelta import *
from datetime import datetime, timedelta, date
import datetime
from fpdf import FPDF
from Space import Space
from LetterDims import LetterDims
from random import randint
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus import Image


#from SpaceX import SpaceX
months_in_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
mon_in_year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days_in_week =['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
pwidth = 612
pheight= 792 
neglect_top = 0.0559
neglect_bottom = 0.034
neglect_left = 0.1136
neglect_right = 0.045
btm_page_num_and_name=0.04
page_num_width = 0.162
patient_name_width_1 = 0.27

def makeFileName():
    randomNumber = randint(1, 10000000)
    date =  datetime.datetime.now()
    print ('tempFileName= ', tempFileName:=f'{date.month}_{date.day}_{date.year}_{randomNumber}.pdf')
    return tempFileName

def getNextMonth():
    date =  datetime.datetime.now()
    m = date.month
    y = date.year
    m+=1
    if (m > 12 ): 
        m = 1
        y+=1
    m2=m+1
    y2 = y
    if (m2> 12):
        m2 = 1
        y2+=1
    return m,y,months_in_year[m-1], mon_in_year[m-1], m2, y2, months_in_year[m2-1], mon_in_year[m2-1]


def get_mon_year():
    dates=getNextMonth()
    return f'{dates[2]}/{dates[1]}'
    
def get_days_of_month():
    dates=getNextMonth()
    bdate="{:04d}".format(dates[1])+"-"+"{:02d}".format(dates[0])+"-"+"01"
    dateb = datetime.datetime.strptime(bdate, "%Y-%m-%d")
    edate="{:04d}".format(dates[5])+"-"+"{:02d}".format(dates[4])+"-"+"01"
    datee = datetime.datetime.strptime(edate, "%Y-%m-%d")
    for adate in  pd.date_range (dateb, datee - timedelta(days=1)):
        yield(adate.strftime('%a')+' '+'{:02d}'.format(adate.day) +'-'+ adate.strftime('%b'))
        




class PageX:
    _page_width=8.5
    _page_height=11

    _patient_of_y = 10.2
    _font_name = "Helvetica"
    _font_name_bold = "Helvetica-Bold"
    _sub_normal_Font_size = 8
    _normal_Font_size = 9
    _2nd_Font_size = 11
    _3rd_Font_size = 14
    _table_end=7.5
    _v_text_y_shift=-7.75
    _v_text_1st=2
    _v_text_2nd=5
    _v_text_3rd=8
    _logo_y=1
    _dob_y=1.25
    _clinc_y=1.5
    _medication_y=1.75
    _2nd_set_x=5
    _margin_x = 1.2
    _table_end=7.6
    _table_top=2.1
    _table_bottom=9.75
    _date_day_col=2.5/16
    _dose_col=1.5/16
    Phar_sig=3/16
    
    
    def text_centered(self, left, right, top, bottom, txt):
        self.pdf.saveState()
        self.pdf.setFont(PageX._font_name_bold,PageX._sub_normal_Font_size)  
        width= right- left
        height = bottom - top
        txt_width=self.pdf.stringWidth(txt,PageX._font_name_bold,PageX._sub_normal_Font_size)/72
        half_txt_width=txt_width/2
        cell_mid_point=left+width/2
        txt_begin=cell_mid_point-half_txt_width
        txt_y=bottom-0.2*height
        self.pdf.drawString(txt_begin*inch,txt_y*inch,txt)
        self.pdf.restoreState() 
        
        
    def draw_mid_table(self, func):
        num_items = 0
        x= func()
        
        for d in x:
            num_items += 1
        
        num_items+=1
        
        
        self.pdf.saveState()
        table_height=PageX._table_bottom - PageX._table_top
        _cell_height = table_height / num_items
        
        _header_height=PageX._table_top +  _cell_height
        self.pdf.line(PageX._margin_x*inch,_header_height*inch,  PageX._table_end*inch  ,_header_height*inch)
        
        
        
        table_width=PageX._table_end-PageX._margin_x
        line1_pos_=PageX._margin_x+table_width*(PageX._date_day_col)
        line1_pos=line1_pos_*inch
        line2_pos_=PageX._margin_x+table_width*(PageX._date_day_col+PageX._dose_col)
        line2_pos=line2_pos_*inch
        line3_pos_=PageX._margin_x+table_width*(PageX._date_day_col+PageX._dose_col *2)
        line3_pos=line3_pos_*inch
        line4_pos_=PageX._margin_x+table_width*(PageX._date_day_col+PageX._dose_col *3)
        line4_pos=line4_pos_*inch
        line5_pos_=PageX._margin_x+table_width*(PageX._date_day_col+PageX._dose_col *3+PageX.Phar_sig)
        line5_pos=line5_pos_*inch
        line6_pos_=PageX._margin_x+table_width*(PageX._date_day_col+PageX._dose_col *3+PageX.Phar_sig*2)
        line6_pos=line6_pos_*inch
        line7_pos_=PageX._margin_x+table_width*(PageX._date_day_col+PageX._dose_col *4+PageX.Phar_sig*2)
        line7_pos=line7_pos_*inch        
        
        self.text_centered(PageX._margin_x, line1_pos_ ,  PageX._table_top , _header_height, 'Date/Day')
        self.text_centered(line1_pos_ , line2_pos_ ,  PageX._table_top , _header_height, 'Dose')
        self.text_centered(line2_pos_ , line3_pos_ ,  PageX._table_top , _header_height, 'C/O')
        self.text_centered(line3_pos_ , line4_pos_ ,  PageX._table_top , _header_height, 'Time')
        self.text_centered(line4_pos_ , line5_pos_ ,  PageX._table_top , _header_height, 'Phar/SIG')
        self.text_centered(line5_pos_ , line6_pos_ ,  PageX._table_top , _header_height, 'Pat/SIG')
        self.text_centered(line6_pos_ , line7_pos_ ,  PageX._table_top , _header_height, 'Returns')
        self.text_centered(line7_pos_ , PageX._table_end ,  PageX._table_top , _header_height, 'Assessed')
        
        left= PageX._margin_x
        right = line1_pos_ 
        top = _header_height
        for d in func():
            txt = d
            bottom = top + _cell_height
            self.text_centered(left,right,top,bottom,txt)
            self.pdf.line(PageX._margin_x*inch,bottom*inch,PageX._table_end*inch,bottom*inch)
 
            top = bottom
        
#        text_centered(self, left, right, top, bottom, txt):
        
        self.pdf.line(PageX._margin_x*inch,PageX._table_top*inch,  PageX._table_end*inch  ,PageX._table_top*inch)
        self.pdf.line(PageX._margin_x*inch,PageX._table_bottom*inch,  PageX._table_end*inch  ,PageX._table_bottom*inch)
        self.pdf.line(PageX._margin_x*inch,PageX._table_top*inch,  PageX._margin_x*inch  ,PageX._table_bottom*inch)
        self.pdf.line(PageX._table_end*inch,PageX._table_top*inch,  PageX._table_end*inch  ,PageX._table_bottom*inch)
  
        self.pdf.line(line1_pos,  PageX._table_top*inch , line1_pos, PageX._table_bottom*inch)
        self.pdf.line(line2_pos,  PageX._table_top*inch , line2_pos, PageX._table_bottom*inch)
        self.pdf.line(line3_pos,  PageX._table_top*inch , line3_pos, PageX._table_bottom*inch)
        self.pdf.line(line4_pos,  PageX._table_top*inch , line4_pos, PageX._table_bottom*inch)
        self.pdf.line(line5_pos,  PageX._table_top*inch , line5_pos, PageX._table_bottom*inch)
        self.pdf.line(line6_pos,  PageX._table_top*inch , line6_pos, PageX._table_bottom*inch)
        self.pdf.line(line7_pos,  PageX._table_top*inch , line7_pos, PageX._table_bottom*inch)
        
        
        self.pdf.restoreState() 

    def print_top_table(self):
        self.pdf.saveState()
        dob_str="Date of B:- "
        clinic_str="CLINIC:- "
        medication_str="Medication: -"
        flavor_str="Flavor:- "
        No_of_Carriers_str="No of Carriers:- "
        name_str="NAME:- "
        if self.id  != 0:
            dob_str+= row['BirthDate']
            clinic_str+=row['Clinic']
            medication_str+=row['Medicine']
            flavor_str+=row['Flavor']
            No_of_Carriers_str+=str(row['No_of_Carriers'])
            name_str+=row['PatientName']
        self.pdf.setFont(PageX._font_name,PageX._normal_Font_size)   
        self.pdf.drawString(PageX._margin_x*inch,PageX._dob_y*inch,dob_str) 
        self.pdf.drawString(PageX._margin_x*inch,PageX._clinc_y*inch,clinic_str) 
        self.pdf.drawString(PageX._2nd_set_x*inch,PageX._clinc_y*inch,No_of_Carriers_str) 
        self.pdf.drawString(PageX._margin_x*inch,PageX._medication_y*inch,medication_str) 
        self.pdf.drawString(PageX._2nd_set_x*inch,PageX._medication_y*inch,flavor_str) 
        self.pdf.setFont(PageX._font_name_bold,PageX._2nd_Font_size)
        self.pdf.drawString(PageX._2nd_set_x*inch,PageX._dob_y*inch,name_str) 
  #      txt_width=self.pdf.stringWidth(self.row['PatientName'],PageX._font_name_bold,PageX._2nd_Font_size)/72
  #      _txt_begin= PageX._table_end - txt_width
  #      self.pdf.setFont(PageX._font_name_bold,PageX._2nd_Font_size)
  #      self.pdf.drawString(_txt_begin*inch,PageX._patient_of_y*inch,self.row['PatientName'])
 
        self.pdf.restoreState()    
    
    
    def __init__(self, _pdf,_id,_num_pages=0,_row=None):
        self.pdf = _pdf
        self.id = _id
        self.num_pages = _num_pages
        self.row = _row
        self.page_of = ''
        pass
    
    
    
    def process(self, func1, func2):
        self.draw_mid_table(func2)
        self.add_logo()
        self.add_wallaces_drug_store()
        self.add_date_mon_year(func1)
        self.print_top_table()
        self.page_of_calc()
        self.page_of_print()
        self.print_bottom_Patient_name()
        pass
    
    def savePage(self):
        self.pdf.showPage()
    
    def page_of_calc(self):
        if self.id  == 0:
            return
        self.page_of = f'Patient {self.id} of {self.num_pages}'
    def page_of_print(self):
        self.pdf.saveState()
        self.pdf.setFont(PageX._font_name_bold,PageX._normal_Font_size)
        if self.id  == 0:
            return
        self.pdf.drawString(PageX._margin_x*inch,PageX._patient_of_y*inch,self.page_of)
        self.pdf.restoreState()
        
    def print_bottom_Patient_name(self):
        self.pdf.saveState()
        if self.id  == 0:
            return
        txt_width=self.pdf.stringWidth(self.row['PatientName'],PageX._font_name_bold,PageX._2nd_Font_size)/72
        _txt_begin= PageX._table_end - txt_width
        self.pdf.setFont(PageX._font_name_bold,PageX._2nd_Font_size)
        self.pdf.drawString(_txt_begin*inch,PageX._patient_of_y*inch,self.row['PatientName'])
        self.pdf.rotate(90)
        self.pdf.drawString(PageX._v_text_1st*inch,PageX._v_text_y_shift*inch,self.row['PatientName'])
        self.pdf.drawString(PageX._v_text_2nd*inch,PageX._v_text_y_shift*inch,self.row['PatientName'])
        self.pdf.drawString(PageX._v_text_3rd*inch,PageX._v_text_y_shift*inch,self.row['PatientName'])
        self.pdf.restoreState()
    def add_logo(self):
        self.pdf.saveState()
        import PIL
        from PIL import Image
        image = Image.open('logo2.png')
        image_width, image_height = image.size
        self.pdf.drawInlineImage(image, PageX._margin_x*inch,(PageX._logo_y-.35)*inch,.9*inch,(0.9*image_height/image_width)*inch)
        self.pdf.restoreState()
    
    def add_wallaces_drug_store(self):
        self.pdf.saveState()  
        txt="Wallaces Drug Store"
        txt_width=self.pdf.stringWidth(txt,PageX._font_name_bold,PageX._3rd_Font_size)/72
        txt_begin=4.25-txt_width/2
        self.pdf.setFont(PageX._font_name_bold,PageX._3rd_Font_size)
        self.pdf.drawString(txt_begin*inch,PageX._logo_y*inch,txt)
        self.pdf.restoreState()
    
    def add_date_mon_year(self, func):
        self.pdf.saveState() 
        txt= func()
        txt_width=self.pdf.stringWidth(txt,PageX._font_name_bold,PageX._2nd_Font_size)/72
        txt_begin = PageX._table_end - txt_width
        self.pdf.setFont(PageX._font_name_bold,PageX._2nd_Font_size)
        self.pdf.drawString(txt_begin*inch,PageX._logo_y*inch,txt)        
        self.pdf.restoreState()
#        canvas.drawImage(self, image, x,y, width=None,height=None,mask=None)
#        print(txt_width)
#canvas.stringWidth(self, text, fontName, fontSize, encoding=None)

patients= pd.read_excel('narco.xlsx')
patients.rename(columns={'Patient #': 'id',
                   'Patient Name': 'PatientName',
                   'No. Of Carries': 'No_of_Carriers' ,
                        'Flavor ': 'Flavor',
                        'CLINC': 'Clinic'},
          inplace=True, errors='raise')
patients=patients[patients['PatientName'].notnull()]
patients['id']=patients.index + 1
print('num_null_patient_name' , num_null_patient_name := sum(pd.isnull(patients['PatientName'])))
print('num_null_BirthDate' , num_null_BirthDate := sum(pd.isnull(patients['BirthDate'])))
print('num_null_Medicine' , num_null_Medicine := sum(pd.isnull(patients['Medicine'])))
print('num_null_Clinic' , num_null_Clinic := sum(pd.isnull(patients['Clinic'])))
print('num_null_Flavor' , num_null_Flavor := sum(pd.isnull(patients['Flavor'])))
patients["Flavor"].fillna("----", inplace = True)
patients["Clinic"].fillna("----", inplace = True)
patients["Medicine"].fillna("----", inplace = True)

file_name= makeFileName()
dt=getNextMonth()
c = canvas.Canvas(f'{dt[2]}_{dt[1]}.pdf', pagesize=letter, bottomup=0)

page=PageX(c, 0)
page.process(get_mon_year, get_days_of_month)


page.savePage()
for index, row in patients.iterrows():
    page=PageX(c, index+1, patients.shape[0]+1, row)
    page.process(get_mon_year, get_days_of_month)
    page.savePage()
c.save()

