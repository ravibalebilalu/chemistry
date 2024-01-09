import os
import csv
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemistry.settings')
django.setup()



def string_to_bool(value):
    if value.lower() == "true":
        return True
    elif value.lower() == "false" or value == "":
        return False
    else:
        return False
def none_int(value):
    if value:
        return int(value)
    else:
        return 0

def data_from_csv(file_path):
    # Import the model within the function
    from periodic_table.models import Element
    print("assining values started") 
    with open(file_path, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            
            element_name = Element(
                atomic_number =  row['AtomicNumber'],
                element = row['Element'],
                symbol = row['Symbol'],
                atomic_mass = row['AtomicMass'],
                number_of_neutrons =  row['NumberofNeutrons'],
                number_of_protons =  row['NumberofProtons'],
                number_of_electrons =  row['NumberofElectrons'],
                period = row['Period'],
                group =  row['Group'],
                phase = row['Phase'],
                radioactive =  row['Radioactive'],
                natural =  row['Natural'],
                metal =  row['Metal'],
                nonmetal =  row['Nonmetal'],
                metalloid =  row['Metalloid'],
                types = row["Type"],
                atomic_radius =  row['AtomicRadius'],
                electronegativity =  row['Electronegativity'],
                first_ionization =  row['FirstIonization'],
                density =  row['Density'],
                melting_point =  row['MeltingPoint'],
                boiling_point =  row['BoilingPoint'],
                number_of_isotopes =  row['NumberOfIsotopes'],
                discoverer = row['Discoverer'],
                year =  row['Year'],
                specific_heat =  row['SpecificHeat'],
                number_of_shells = row['NumberofShells'],
                number_of_valence = row['NumberofValence']

            )

             
            element_name.save() 
        print("done")
         
         
         
#for loading new data from csv file
#file_path = "final_table.csv"
#data_from_csv(file_path)

from periodic_table.models import Element
per_element = Element.objects.filter(atomic_number=1).values()
result = per_element[0]
print(result['id'])
 
 

 

