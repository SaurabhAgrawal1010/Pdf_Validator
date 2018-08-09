#For text to JSON atom we are taking as input the PDF-text and based on a configuration file
#extracting key fields and attributes that needs to be validated
#This is completely configurable and scalable to support multiple attributes from the PDF
#The configuration file represents the structure/metadata of PDF and hence it will be account specific

#Input ==> A text stream
#Configuration ==> An input configuration file that contains the following information:
#   - Attribute information - Name
#   - Attribute information - Regular Expression to fetch the attribute from text string
#Output ==> A JSON output file giving out the name,value pair

import re
import json

def handle(req):

    if (re.search('ERROR:', req)):
        return req
    
    data = req
   
    try:
        with open('function/config.json') as con:
            jsn = json.load(con)
    except:
        return "ERROR: text-to-json-extract: Invalid Configuration file\n"
    
    extracted_values = {}
   
    #loop on all required atributes as present in the configuration file and extract value based on regex pattern 
    for j in jsn['field_details']:
        
        reg = j['regex']
        regex = re.compile(reg)
        result = '' 
        
        if (regex.search(data)):
            result = regex.search(data).group(1)
        
        if (re.search(',', result)):
            result = result.replace(',', '.')
        
        #prepare and add the result to a dictionary 
        extracted_values[j['entity']] = result
    
    #convert the dictionary to JSON format for exchange over HTTP 
    extracted_values = json.dumps(extracted_values)
    return extracted_values
