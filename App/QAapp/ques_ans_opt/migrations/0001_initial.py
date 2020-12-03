# Generated by Django 3.1.4 on 2020-12-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iterations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('question_answer_1', models.CharField(max_length=256)),
                ('question_answer_2', models.CharField(max_length=256)),
                ('question_answer_3', models.CharField(max_length=256)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('option1', models.CharField(max_length=256)),
                ('option2', models.CharField(max_length=256)),
                ('answer', models.CharField(max_length=256)),
            ],
        ),
    ]
