from fpdf import FPDF 
import json
 
pdf = FPDF() 
pdf.add_page() 

pdf.set_font("Arial", size = 12) 
  
# create a cell 

with open("tasks.json","r") as f:
	tasklist = f.read()
	
tasklist = json.loads(tasklist)
tasks = tasklist['todo']

for k, v in tasks.items():
	pdf.cell(200, 10, txt = v['name'], align = 'L')
	pdf.ln(3)
	for k1, v1 in v.items():
		if k1 == "name":
			continue
		pdf.cell(200, 10, txt = k1 + " : " + v1, align = 'L', ln = 1)
		pdf.ln()
	pdf.ln(4)
  
# save the pdf with name .pdf 
pdf.output("export.pdf")