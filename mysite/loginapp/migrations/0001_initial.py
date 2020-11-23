# Generated by Django 3.1.3 on 2020-11-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=150)),
                ('sub', models.CharField(max_length=30)),
                ('diff', models.IntegerField(choices=[(1, 'Simple'), (2, 'Hard')])),
            ],
        ),
    ]
