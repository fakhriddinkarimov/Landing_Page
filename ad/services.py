import json
from collections import OrderedDict

from django.db import connection

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
def dictfetchone(cursor):
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))
def get_product_all():
    with connection.cursor() as cursor:
        cursor.execute(f"""
                   SELECT * ,ad.slug FROM ad_product as ad
                   INNER JOIN ad_productimage as ad_pr
                   ON ad.id = ad_pr.product_id
                   INNER JOIN ad_image as image
                   ON image.id = ad_pr.image_id
                   INNER JOIN ad_category as ctg
                   ON ad.category_id = ctg.id
                   ORDER BY created_date DESC
           """)
        data = dictfetchall(cursor)
    data = _format_all(data)
    return data

def all_categories():
    with connection.cursor() as cursor:
        cursor.execute("""
        SELECT * FROM ad_category
        """)
        data = dictfetchall(cursor)
    return data

def _format_all(data):
    new_data = []
    for d in data:
        if d['location']:
            region = json.loads(d['location'])['region']
            district = json.loads(d['location'])['district']
        else:
            region = None
            district = None
        new_data.append(OrderedDict([
            ('id',d['id']),
            ('title',d['title']),
            ('slug',d['slug']),
            ('decription',d['decription']),
            ('phone_number',d['phone_number']),
            ('created_date',d['created_date']),
            ('category_id',d['category_id']),
            ('product_id',d['product_id']),
            ('image',d['image']),
            ('name',d['name']),
            ('region',region),
            ('district',district),
            ('price',d['price'])
        ]))
    return new_data
def info_ad(id):
    with connection.cursor() as cursor:
        cursor.execute(f"""
                SELECT * FROM ad_product
                where id = {id}
        """)
        data = dictfetchone(cursor)
    return data

