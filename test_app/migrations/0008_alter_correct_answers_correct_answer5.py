# Generated by Django 4.0 on 2022-02-07 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0007_test_by_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correct_answers',
            name='correct_answer5',
            field=models.CharField(blank=True, help_text='при наявності', max_length=100, null=True, verbose_name='Правильна відповідь 5'),
        ),
    ]
