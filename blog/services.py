from django.db import connection


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_blog():
    with connection.cursor() as cursor:
        cursor.execute("""
                SELECT * FROM blog_blog
                ORDER BY created_date DESC
        """)


def get_comments():
    with connection.cursor() as cursor:
        cursor.execute("""
                SELECT * FROM blog_comments
                ORDER BY created_date DESC
        """)
