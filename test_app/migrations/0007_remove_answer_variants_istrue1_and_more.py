# Generated by Django 4.0 on 2022-01-11 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0006_alter_testeduser_options_alter_answer_point_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer_variants',
            name='istrue1',
        ),
        migrations.RemoveField(
            model_name='answer_variants',
            name='istrue2',
        ),
        migrations.RemoveField(
            model_name='answer_variants',
            name='istrue3',
        ),
        migrations.RemoveField(
            model_name='answer_variants',
            name='istrue4',
        ),
        migrations.RemoveField(
            model_name='answer_variants',
            name='istrue5',
        ),
        migrations.RemoveField(
            model_name='answer_variants',
            name='istrue6',
        ),
        migrations.AddField(
            model_name='answer_variants',
            name='numbers_true',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Номери правильних варіантів через кому'),
        ),
    ]
