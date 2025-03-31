import os




##This class gets a list of lists and a name,I'll be equipped to do reports on its own with OOP
class Report_Engine:
    
    def __init__(self,name:str,data: list[list[str]]):
        self.name=name
        self.data=data
        self.lenght=len(data)
        self.output_folder="reports"


#I get list of fields from the first row of the data ex: name,age,gender, etc...
    def get_fields(self):
        return self.data[0]
    



    def make_reports(self):
        print("making report")
         
        
                    