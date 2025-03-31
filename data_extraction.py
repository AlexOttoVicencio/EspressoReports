import csv

##Este objeto hace
#le doy un nombre y me devuelve una lista de listas list[list[]] con todos los datos
#maneja todo tipo de extraccion de datos

class DataDrill :
    def __init__(self,name:str,filename:str):
        self.name =name
        #User has to put the filename and the data in the data folder and it'll be handled
        self.filename= "data/"+filename


    def greet(self):
        print(f"the filename is {self.name} and the filename is: {self.filename}")


    #leemos el csv
    def getData(self):
        data_list=[]
        with open(self.filename, mode="r", encoding="ISO-8859-1") as file:  
            csv_reader = csv.reader(file)
            
            for row in csv_reader:
                print("roooooooooooooooooooooooooooooooooooooooooooow")
                print(row)
            print(data_list)
            

        

#this is how you can get data from the drill

#create an object
file_tesis= DataDrill("PostulacionesTesis","tesis_form_data.csv")
file_tesis.greet()

#ask for the data
file_tesis.getData()

