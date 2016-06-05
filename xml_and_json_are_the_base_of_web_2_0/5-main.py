from car import Car
from xml.dom.minidom import Document
import json

''' Open the json file and load it into a variable to be used later '''
with open('5-main.json') as json_data:
    data = json.load(json_data)

all_brands = []
total_doors = 0

''' Create a DOM document '''
document = Document()
all_cars = document.createElement("all_cars")
document.appendChild(all_cars)

''' Iterate through data to format each dict '''
for i in data:
    car = Car(i)

    brand = car.get_brand()
    nb_doors = car.get_nb_doors()
    xml = car.to_xml_node(document)
    if brand not in all_brands:
        all_brands.append(brand)
    total_doors += nb_doors

    all_cars.appendChild(xml)

print len(all_brands)
print total_doors
last_car = Car(data[3])
print last_car
print document.toxml(encoding='utf-8')
