import json
from fpdf import FPDF

with open('Assign.json') as json_file:
    Assigned=json.load(json_file)

name = Assigned["name"]
email = Assigned["email"]
basicinfo= Assigned["basicinfo"]
age= Assigned["age"]
gender= Assigned["gender"]
birth= Assigned["birth"]
address= Assigned["address"]


profiles= Assigned["profiles"]
network= Assigned["network"]
username= Assigned["username"]
url= Assigned["url"]

obj= Assigned["obj"]
obj1= Assigned["obj1"]

skil= Assigned["skil"]
skil1= Assigned["skil1"]
skil2= Assigned["skil2"]
skil3= Assigned["skil3"]
skil4= Assigned["skil4"]
skil5= Assigned["skil5"]
skil6= Assigned["skil6"]

education= Assigned["education"]
col= Assigned["col"]
col1= Assigned["col1"]
col2=Assigned["col2"]
col3=Assigned["col3"]
col4=Assigned["col4"]

shs=Assigned["shs"]
shs1=Assigned["shs1"]
shs2=Assigned["shs2"]
shs3=Assigned["shs3"]
shs4=Assigned["shs4"]

hs=Assigned["hs"]
hs1=Assigned["hs1"]
hs2=Assigned["hs2"]
hs3=Assigned["hs3"]

andd=Assigned["andd"]
andd1=Assigned["andd1"]
andd2=Assigned["andd2"]
andd3=Assigned["andd3"]
andd4=Assigned["andd4"]
andd5=Assigned["andd5"]
andd6=Assigned["andd6"]

addinfo=Assigned["addinfo"]
addinfo1=Assigned["addinfo1"]
addinfo2=Assigned["addinfo2"]
addinfo3=Assigned["addinfo3"]

oth=Assigned["oth"]
oth1=Assigned["oth1"]
oth2=Assigned["oth2"]

finalpdf=FPDF('P', 'mm', 'Letter' )

finalpdf.set_auto_page_break(auto=True, margin=20)
finalpdf.add_page()

finalpdf.set_font('times', 'B', 20)
finalpdf.set_margins(top=20, left=20,right=20)

finalpdf.cell(0,0, name, align='C', ln=True)
finalpdf.set_font('times', '', 11)

finalpdf.cell(0,10, email, align= 'C', ln=True)
finalpdf.line(10,43,208,43)
finalpdf.set_font('times', 'B', 17)
finalpdf.cell(0,20, basicinfo, align='L', ln=True)
finalpdf.set_font('times', '', 14)
finalpdf.cell(0,-8, age, align='L', ln=True)
finalpdf.cell(0,18,gender, align='L', ln=True)
finalpdf.cell(0,-8,birth, align='L', ln=True)
finalpdf.line(10,69,208,69)
finalpdf.set_font('times', 'B', 17)
finalpdf.cell(0,28, profiles, align='L', ln=True)
finalpdf.set_font('times','',14)
finalpdf.cell(0,-17, network, align='L', ln=True)
finalpdf.set_font('times', '', 14)
finalpdf.cell(0,26, username, align='L', ln=True )
finalpdf.set_font('times', 'I', 11)
finalpdf.cell(0,-17, url, align='L', ln=True)
finalpdf.line(10,93,208,93)
finalpdf.set_font('times', 'B', 17)
finalpdf.cell(0,35,obj, align='L', ln=True)
finalpdf.set_font('times', '',14)
finalpdf.cell(0,-23, obj1, align='L', ln=True)
finalpdf.line(10,109,208,109)
finalpdf.set_font('times', 'B', 17)
finalpdf.cell(0,43, skil, align='L', ln=True)
finalpdf.set_font('times', '', 14)
finalpdf.cell(0,-30, skil1, align='L', ln=True)
finalpdf.cell(0,39, skil2, align='L', ln=True)
finalpdf.cell(0,-29, skil3, align='L', ln=True)
finalpdf.cell(0,39, skil4, align='L', ln=True)
finalpdf.cell(0,-28, skil5, align='L', ln=True)
finalpdf.cell(0,39, skil6, align='L', ln=True)
finalpdf.line(10,152,208,152)
finalpdf.set_font('times', 'B', 17)
finalpdf.cell(0,-15, education, align='L', ln=True)
finalpdf.set_font('times', 'B', 15)
finalpdf.cell(0,35, col, align='L', ln=True)
finalpdf.set_font('times', '', 13)
finalpdf.cell(0,-25, col1, align='L', ln=True)
finalpdf.cell(0,40, col2, align='L', ln=True)
finalpdf.cell(0,-30, col3, align='L', ln=True)
finalpdf.cell(0,40, col4, align='L', ln=True)
finalpdf.set_font('times', 'B',15)
finalpdf.cell(0,-22, shs, align='L', ln=True)
finalpdf.set_font('times', '', 13)
finalpdf.cell(0,30, shs1, align='L', ln=True)
finalpdf.cell(0,-15, shs2, align='L', ln=True)
finalpdf.cell(0,25, shs3, align='L', ln=True)
finalpdf.cell(0,-15, shs4, align='L', ln=True)
finalpdf.set_font('times', 'B',15)
finalpdf.cell(0,30, hs, align='L', ln=True)
finalpdf.set_font('times', '', 13)
finalpdf.cell(0,-20, hs1, align='L', ln=True)
finalpdf.cell(0,35, hs2, align='L', ln=True)
finalpdf.cell(0,-27, hs3, align='L', ln=True)

finalpdf.add_page()
finalpdf.set_margins(top=20, left=20,right=20)

finalpdf.line(10,26,208,26)
finalpdf.set_font('times','B',17)
finalpdf.cell(0,5, andd, align='L', ln=True)

finalpdf.set_font('times', 'B', 17)
finalpdf.cell(0,18, andd1, align='L', ln=True)
finalpdf.set_font('times', 'I', 13)
finalpdf.cell(0,-9, andd3, align='L', ln=True)
finalpdf.set_font('times', '', 15)
finalpdf.cell(0,19, andd2, align='L', ln=True)
finalpdf.set_font('times', 'B', 17)
finalpdf.cell(0,5, andd1, align='L', ln=True)
finalpdf.set_font('times', 'I', 13)
finalpdf.cell(0,6, andd5, align='L', ln=True)
finalpdf.set_font('times', '', 15)
finalpdf.cell(0,5, andd4, align='L', ln=True)
finalpdf.set_font('times', 'B', 17)
finalpdf.cell(0,18, andd1, align='L', ln=True)
finalpdf.set_font('times', 'I', 13)
finalpdf.cell(0,-7, andd5, align='L', ln=True)
finalpdf.set_font('times', '', 15)
finalpdf.cell(0,17, andd6, align='L', ln=True)

finalpdf.line(10,105,208,105)
finalpdf.set_font('times', 'B', 17)
finalpdf.cell(0,10, addinfo, align='L', ln=True)
finalpdf.set_font('times', '', 13)
finalpdf.cell(0,5, addinfo1, align='L', ln=True)
finalpdf.cell(0,5, addinfo2, align='L', ln=True)
finalpdf.cell(0,5, addinfo3, align='L', ln=True)


finalpdf.line(10,133,208,133)
finalpdf.set_font('times', 'B', 17)
finalpdf.cell(0,15, oth, align='L', ln=True)
finalpdf.set_font('times', '', 13)
finalpdf.cell(0,5, oth1, align='L', ln=True)
finalpdf.cell(0,5, oth2, align='L', ln=True)

finalpdf.output("LACSON_MARYLOUI YESHA.pdf")