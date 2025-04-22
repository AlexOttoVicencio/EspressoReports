
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now import works
from tools.data_extraction import DataDrill




#this is how you can get data from the drill

#create an object
file_tesis= DataDrill("PostulacionesTesis","tesis_form_data.csv")


#ask for the data
tesis_data=file_tesis.getData()

print(tesis_data)
