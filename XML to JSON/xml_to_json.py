import xmltodict
import json

#Function to convert XML to JSON
def convert_xml_to_json(xml_file_path):
    try:
        with open(xml_file_path, 'r') as xml_data:
            # Parse the XML data into a dictionary using xmltodict
            data_dict = xmltodict.parse(xml_data.read())
            
            # Convert the dictionary to JSON 
            json_data = json.dumps(data_dict, indent=4)
            
            return json_data
    except FileNotFoundError:
        return "Error: The specified XML file was not found."

if __name__ == "__main__":
    xml_file_path = input('Enter XML file: ')
    
    # Calling the function to convert the XML to JSON
    json_data = convert_xml_to_json(xml_file_path)
    
    print(json_data)
