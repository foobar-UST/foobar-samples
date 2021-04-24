import json
from config import db

# Insert into 'item_categories'
with open('./assets/item_categories_fake_data.json') as json_file:
    fake_categories = json.load(json_file)
    batch = db.batch()

    for category in fake_categories:
        docRef = db.document(f'item_categories/{category["id"]}')

        batch.set(docRef, {
            'id': category['id'],
            'tag': category['tag'],
            'title': category['title'],
            'title_zh': category['title_zh'],
            'image_url': category.get('image_url', None)
        })

    batch.commit()

    print('insert success.')