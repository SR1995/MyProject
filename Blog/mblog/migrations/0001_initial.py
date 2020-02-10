# Generated by Django 3.0.2 on 2020-02-09 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('author', models.CharField(choices=[('admin', 'MZ'), ('other', 'other')], default='MZ', max_length=20)),
                ('type', models.CharField(choices=[('C语言', 'C语言'), ('Python', 'Python'), ('Django', 'Django'), ('数据结构', '数据结构'), ('算法', '算法')], default='C语言', max_length=30)),
                ('Bnumber', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]