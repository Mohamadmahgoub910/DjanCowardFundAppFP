# Generated by Django 3.2.4 on 2021-12-05 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set(),
        ),
    ]