# Generated by Django 2.2 on 2019-05-12 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Greet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greettitle', models.CharField(max_length=255)),
                ('greetdate', models.DateField()),
                ('greettime', models.TimeField()),
                ('greetlocation', models.TextField()),
                ('greetagenda', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'greetings',
                'db_table': 'greet',
            },
        ),
        migrations.DeleteModel(
            name='Meeting',
        ),
        migrations.AlterModelOptions(
            name='meetingtype',
            options={'verbose_name_plural': 'meeting types'},
        ),
        migrations.AlterModelTable(
            name='meetingtype',
            table='meeting type',
        ),
    ]
