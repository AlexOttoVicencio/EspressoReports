import sys
import json
import os
from jinja2 import Environment,FileSystemLoader
from weasyprint import HTML, CSS

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Now import works
from tools.data_extraction import DataDrill


#this is how you can get data from the drill

#create an object
file_tesis= DataDrill("PostulacionesTesis","postulacionesTesis29Abril.csv")


#ask for the data
tesis_data=file_tesis.getData()

#make a folder

tesis_folder = './reports/tesis_reports'

### making sure it doesnt exist and then make a folder
if not os.path.exists(tesis_folder):
    os.mkdir(tesis_folder)
    print(f"Folder {tesis_folder} was created")
else:
    print(f"Folder {tesis_folder} already exists")

#add the folder where templates are stored, then make a 
env = Environment(loader=FileSystemLoader('html_templates'))
template = env.get_template('tesis_report.html')

#4 Iterating through the pandas report

#Make a filename for the reports

report_name="Tesis_de_Postgrado_con_Impacto"


#now we iterate  each row for a report

for index,row in tesis_data.iterrows():
    #
    output_filename=f"reports/tesis_reports/{report_name}_{index+1}_{row["nombre"]}.pdf"
    
    
    row["profesor_guia"] = json.loads(row["profesor_guia"])
    row["plan_presupuesto"] = json.loads(row["plan_presupuesto"])
    rendered_html = template.render(row)
    HTML(string=rendered_html).write_pdf(output_filename)
    
