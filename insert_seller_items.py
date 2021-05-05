import json
from config import db

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Insert into 'items'
with open('./assets/seller_items_fake_data.json') as json_file:
    fake_items = json.load(json_file)

    # Split into multiple batches due to firestore insert limit.
    batches = chunks(list(fake_items), 5)

    for b in batches:
        batch = db.batch()

        for item in b:
            docRef = db.document(f'sellers/{item["seller_id"]}/items/{item["id"]}')

            batch.set(docRef, {
                'id': item['id'],
                'title': item['title'],
                'title_zh': item.get('title_zh', None),
                'description': item.get('description', None),
                'description_zh': item.get('description_zh', None),
                'catalog_id': item['catalog_id'],
                'seller_id': item['seller_id'],
                'price': item['price'],
                'image_url': item.get('image_url', None),
                'count': item['count'],
                'available': item['available']
            })

        batch.commit()

    print('insert success.')