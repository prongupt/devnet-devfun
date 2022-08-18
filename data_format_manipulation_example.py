from pprint import pprint



import yaml
"""This section is for demonstrating serializing and deserializing function for YAML data format using the YAML 
python library"""
# with open('yaml_example.yml', 'r') as file:
#     print("Converting the YAML file into a Python object ('dictionary')")
#     users = yaml.safe_load(file)
# for each_user in users:
#     for info in (users[each_user]):
#         users[each_user]['location']['city'] = "Dallas"
#     print("----------")
# pprint(users)
#
# with open ('yaml_edited_example.yml', 'w') as file:
#     yaml.dump(users, file, default_flow_style=False)

import json
# """This section is for demonstrating serializing and deserializing function for JSON data format using the in-built
# JSON python library"""
# with open('json_example.yml', 'r') as file:
#     print("Converting the YAML file into a Python object ('dictionary')")
#     users = json.load(file)
#
# for each_user in users:
#     for info in (users[each_user]):
#         users[each_user]['location']['city'] = "Dallas"
#     print("----------")
# pprint(users)
#
# with open ('json_edited_example.yml', 'w') as file:
#     json.dump(users, file, indent=4)


import xml.etree.ElementTree as ET
"""This section is for demonstrating serializing and deserializing function for XML data format using the ElementTree 
python library"""
with open('xml_example.xml', 'r') as file:
    mytree = ET.parse(file)
    myroot = mytree.getroot()

user = myroot.find('user')
print(user.find('name').text)
print('Tags in the XML tree:')
for element in myroot:
    print(element.tag)
for role in user.findall('roles'):
    print(role.text)

user.find('location').find('city').text = "Dallas"
with open('xml_edited_example.xml', 'w') as file:
    mytree.write(file, encoding='Unicode')



"""
Need to look into the MiniDOM XML parser - figure out how to complete this part. Also the lab example on the 
ondemandlearning Cisco website is great. Potentially look at completing that lab again.
"""
import xml.dom.minidom as MD
"""This section is for demonstrating serializing and deserializing function for XML data format using the MiniDom
python library"""
with open('xml_example.xml', 'r') as file:
    dom = MD.parse(file)

print("The tags in the XML:")
for node in dom.childNodes:
    printTags
print(user.find('name').text)
print('Tags in the XML tree:')
for element in myroot:
    print(element.tag)
for role in user.findall('roles'):
    print(role.text)

user.find('location').find('city').text = "Dallas"
with open('xml_edited_example.xml', 'w') as file:
    mytree.write(file, encoding='Unicode')
