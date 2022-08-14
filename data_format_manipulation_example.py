import yaml
import json
from pprint import pprint


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



with open('json_example.yml', 'r') as file:
    print("Converting the YAML file into a Python object ('dictionary')")
    users = json.load(file)

for each_user in users:
    for info in (users[each_user]):
        users[each_user]['location']['city'] = "Dallas"
    print("----------")
pprint(users)

with open ('json_edited_example.yml', 'w') as file:
    json.dump(users, file, indent=4)
