import yaml
from pprint import pprint
with open('yaml_example.yml', 'r') as file:
    print("Converting the YAML file into a Python object ('dictionary')")
    users = yaml.safe_load(file)

pprint(users)

for each_user in users:
    for info in (users[each_user]):
        users[each_user]['location']['city'] = "Dallas"
    print("----------")
pprint(users)

with open ('yaml_edited_example.yml', 'w') as file:
    yaml.dump(users, file, default_flow_style=False)
    