import firebase_admin
from config import db

db.document('test/test2').set({
     'field1': 'value1',
     'field2': 'value2'
})

print('write success.')