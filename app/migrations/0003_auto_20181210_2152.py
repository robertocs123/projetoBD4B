# Generated by Django 2.1.4 on 2018-12-11 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tipo',
            field=models.ManyToManyField(null=True, to='app.Tipo'),
        ),
    ]
