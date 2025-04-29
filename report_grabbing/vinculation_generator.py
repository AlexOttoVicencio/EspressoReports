
import sys
import json
import os
from jinja2 import Environment,FileSystemLoader
from weasyprint import HTML, CSS

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Now import works
from tools.data_extraction import DataDrill

#create an object
file_vinculation= DataDrill("Postulaciones Vinc Socio","postulacionesVinc28abril.csv")

#ask for the data now we can process it
vinculation_data=file_vinculation.getData()

###1.We got the data!!! nicee
#print(vinculation_data)

###2.Now we make a folder inside reports where to store out pdfs!!!
reports_folder='./reports/vinculation_form_reports'

### making sure it doesn
if not os.path.exists(reports_folder):
    os.mkdir(reports_folder)
    print(f"Folder {reports_folder} was created")
else:
    print(f"Folder {reports_folder} already exists")

#3 Add the template that I want to use to put the data

env = Environment(loader=FileSystemLoader('html_templates'))
template = env.get_template('vinculation_report.html')

#4 Iterating through the pandas report

#Make a filename for the reports

report_name="Innovacion_Vinc_Socio"


#now we iterate  each row for a report

for index,row in vinculation_data.iterrows():
    #
    output_filename=f"reports/vinculation_form_reports/{report_name}_{index+1}_{row["nombre"]}.pdf"
    row["investigadores"] = json.loads(row["investigadores"])
    row["patrocinadores"] = json.loads(row["patrocinadores"])
    row["proy_previos"] = json.loads(row["proy_previos"])
    row["plan_presupuesto"] = json.loads(row["plan_presupuesto"])
    rendered_html = template.render(row)
    HTML(string=rendered_html).write_pdf(output_filename)
    