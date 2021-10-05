from django.db import connection

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
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
    return data