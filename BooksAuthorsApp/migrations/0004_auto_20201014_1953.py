# Generated by Django 2.2.4 on 2020-10-14 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksAuthorsApp', '0003_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='BooksAuthorsApp.Book'),
        ),
    ]
