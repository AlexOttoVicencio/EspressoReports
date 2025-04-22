import csv
import pandas as pd


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
    #We open it, read it line by line then put it in a list
    def getData(self):
        
       
       data = pd.read_csv(self.filename, encoding="utf-8",sep=",")
       #print(data.head())
       return data
                
            

               
            
#this is how you can get data from the drill

#create an object
#file_tesis= DataDrill("PostulacionesTesis","tesis_form_data.csv")
#file_tesis.greet()

#ask for the data
#tesis_data=file_tesis.getData()



