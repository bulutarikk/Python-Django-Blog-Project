# Generated by Django 4.2.4 on 2023-08-10 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_postmodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
