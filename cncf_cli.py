import yaml  
import argparse
from pprintpp import pprint
Yamlfile = 'projects.yml'

#Creating the parser for interpeting the commands
parser = argparse.ArgumentParser()

#Adding the name argument
parser.add_argument('--name', '-n', type=str, required=True)


# Defining a function that reads the projects name from the YAML File
def get_project_name(project_name):
    with open(Yamlfile) as y:
        landscape = yaml.safe_load(y)
        for category in landscape['landscape']:
            for subcategory in category['subcategories']:
                for item in subcategory['items']:
                    if item['name'] == project_name:
                        print("Category:")
                        pprint(category['name'])
                        print("Subcategory:")
                        pprint(subcategory['name'])
                        print("Item Details:")
                        pprint(item)
                        return
        print(f"Project '{project_name}' not found.")

 #parsing the entered argument       
args = parser.parse_args()

#getting the project data
get_project_name(args.name)