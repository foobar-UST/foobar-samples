import json
from config import db

# Insert into 'catalogs'
with open('./assets/seller_catalogs_extra_fake_data_cambo.json') as json_file:
    fake_catalogs = json.load(json_file)
    batch = db.batch()

    for catalog in fake_catalogs:
        docRef = db.document(f'sellers/{catalog["seller_id"]}/catalogs/{catalog["id"]}')

        batch.set(docRef, {
            'id': catalog['id'],
            'title': catalog['title'],
            'title_zh': catalog.get('title_zh', None),
            'available': catalog['available']
        })

    batch.commit()

    print('insert success.')