# Generated by Django 4.2.8 on 2024-01-12 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_alter_category_options_alter_book_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookissueretrunhistory',
            old_name='borrow_list',
            new_name='account',
        ),
    ]
