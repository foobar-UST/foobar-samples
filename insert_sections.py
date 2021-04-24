import json
import pytz
from datetime import datetime, timedelta
from firebase_admin import firestore
from config import db

# Insert into 'sections'
with open('./assets/sections_fake_data.json') as json_file:
    fake_sections = json.load(json_file)
    batch = db.batch()

    for index, section in enumerate(fake_sections):
        docRef = db.document(f'sellers/{section["seller_id"]}/sections/{section["id"]}')

        delivery_location = {
            'address': section['delivery_location']['address'],
            'address_zh': section['delivery_location']['address_zh'],
            'geopoint': firestore.GeoPoint(
                section['delivery_location']['geopoint']['lat'],
                section['delivery_location']['geopoint']['long']
            )
        }

        now_time = datetime.now(pytz.timezone('Asia/Hong_Kong')) + timedelta(days=index)
        cutoff_time = datetime.strptime(section["cutoff_time"], '%H:%M') 
        delivery_time = datetime.strptime(section["delivery_time"], '%H:%M')

        new_cutoff_time = now_time.replace(hour=cutoff_time.hour, minute=cutoff_time.minute)
        new_delivery_time = now_time.replace(hour=delivery_time.hour, minute=delivery_time.minute)

        batch.set(docRef, {
            'id': section['id'],
            'title': section['title'],
            'title_zh': section.get('title_zh', None),
            'group_id': section['group_id'],
            'seller_id': section['seller_id'],
            'seller_name': section['seller_name'],
            'seller_name_zh': section.get('seller_name_zh', None),
            'description': section['description'],
            'description_zh': section.get('description_zh', None),
            'delivery_cost': section['delivery_cost'],
            'delivery_time': new_delivery_time,
            'delivery_location': delivery_location,
            'cutoff_time': new_cutoff_time,
            'max_users': section['max_users'],
            'joined_users_count': section.get('joined_users_count', 0),
            'joined_users_ids': section.get('joined_users_count', []),
            'image_url': section.get('image_url', None),
            'state': section['state'],
            'available': section['available'],
        })

    batch.commit()

    print('insert success.')