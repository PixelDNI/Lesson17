# Generated by Django 4.2.4 on 2023-09-10 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='surname',
            field=models.CharField(default='Haski', max_length=70),
            preserve_default=False,
        ),
    ]
