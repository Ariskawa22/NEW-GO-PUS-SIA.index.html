# Generated by Django 3.0 on 2021-07-02 17:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20210703_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bukuinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('158987a1-d1b2-454c-ab93-20d63c03fd44'), primary_key=True, serialize=False),
        ),
    ]
