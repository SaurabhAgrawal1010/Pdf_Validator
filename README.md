# Pdf_Validator

Pdf Validator is very usful in all the field. It first convert the pdf file to text, after that it will extract the required fields from the text based on regular expressions defined in configuration file. It convert the fields(values) in json format and after that match those values from the database values and give us the final result which will tell us the mismatch values.

FLOW:

pdf-to-text -----> text-to-json-extract -----> get-db-to-json
