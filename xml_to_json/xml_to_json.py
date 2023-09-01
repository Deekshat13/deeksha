import xmltodict

import json

 

def convert_xml_to_json(xml_file):

    with open(xml_file, 'r') as xml_data:

        data_dict = xmltodict.parse(xml_data.read())

        json_data = json.dumps(data_dict, indent=4)

        return json_data

 

xml_file_path = input('Enter the file ')

json_data = convert_xml_to_json(xml_file_path)

print(json_data)
