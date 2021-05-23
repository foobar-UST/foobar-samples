import json
import uuid

# Read file
json_file = open('./assets/seller_sections_fake_data_cambo.json' , 'r') 
items = json.load(json_file);
json_file.close()

for item in items:
    item['id'] = str(uuid.uuid4())
    item['group_id'] = str(uuid.uuid4())

# Write file
json_file = open('./assets/seller_sections_fake_data_cambo.json' , 'w') 
json.dump(items, json_file)
json_file.close()