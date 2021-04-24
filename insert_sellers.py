import json
from firebase_admin import firestore
from config import db

# Insert into 'sellers'
with open('./assets/sellers_fake_data.json') as json_file:
    fake_sellers = json.load(json_file)
    batch = db.batch()

    for seller in fake_sellers:
        docRef = db.document(f'sellers/{seller["id"]}')

        location = {
            'address': seller['location']['address'],
            'address_zh': seller['location']['address_zh'],
            'geopoint': firestore.GeoPoint(
                seller['location']['geopoint']['lat'],
                seller['location']['geopoint']['long']
            )
        }

        batch.set(docRef, {
            'id': seller['id'],
            'name': seller['name'],
            'name_zh': seller.get('name_zh', None),
            'description': seller.get('description', None),
            'description_zh': seller.get('description_zh', None),
            'website': seller.get('website', None),
            'phone_num': seller['phone_num'],
            'location': location,
            'image_url': seller.get('image_url', None),
            'min_spend': seller['min_spend'],
            'order_rating': seller['order_rating'],
            'delivery_rating': seller.get('delivery_rating', None),
            'rating_count': seller['rating_count'],
            'type': seller['type'],
            'online': seller['online'],
            'notice': seller.get('notice', None),
            'opening_hours': seller['opening_hours'],
            'tags': seller['tags']
        })

    batch.commit()

    print('insert success.')