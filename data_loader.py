import csv
import os
from reports import Report_Engine
#Class that reads the file you need 
class Data_Reader:
    def __init__(self,filename:str):
        self.filename="data/"+filename


    def get_filename(self):
        return self.filename

    
    def get_file(self):
        print("Checking if your file exists....")

        if(os.path.isfile(self.filename)):
            print("file found, beggining to process....")
            with open(self.filename, mode='r', encoding="ANSI", newline='') as file:
                reader = csv.reader(file, delimiter=";")
                data = [row for row in reader]
                return data
    
        else:
            print("your file was not found check spelling")
        

####-----------------------------------------------------------###############

#report = Data_Reader("tesis_post_impct.csv")

#print(report.get_filename()+"es el nombre del archivo")

#reports_data=report.get_file()
#print(len(reports_data))


#ahora le damos todo al ReportEngine y dejamos q tome el csv y haga un output con los reportes

#my_reports = Report_Engine("Tesis de postgrado con impacto",reports_data)

#my_reports.make_reports()

