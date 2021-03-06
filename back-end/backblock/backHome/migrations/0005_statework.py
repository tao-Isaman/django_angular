# Generated by Django 2.1.7 on 2019-03-03 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backHome', '0004_auto_20190303_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='stateWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'Working'), ('1', 'WorkFinished')], max_length=50)),
                ('Working', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backHome.Work')),
                ('studentWork', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backHome.Student')),
            ],
        ),
    ]
