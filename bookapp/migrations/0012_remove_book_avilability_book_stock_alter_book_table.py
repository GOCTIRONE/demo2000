# Generated by Django 4.1.3 on 2022-11-18 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookapp", "0011_alter_book_avilability"),
    ]

    operations = [
        migrations.RemoveField(model_name="book", name="avilability",),
        migrations.AddField(
            model_name="book",
            name="stock",
            field=models.IntegerField(blank=True, default=0, editable=False),
        ),
        migrations.AlterModelTable(name="book", table="Book",),
    ]
