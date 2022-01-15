# Generated by Django 4.0 on 2022-01-14 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_result_persent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Відповідь користувача', 'verbose_name_plural': 'Відповіді користувачів'},
        ),
        migrations.AddField(
            model_name='test',
            name='is_active',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='test_app.test'),
        ),
        migrations.AlterField(
            model_name='questiontype',
            name='name',
            field=models.CharField(choices=[('S', 'Коротка відповідь'), ('SC', 'Одиночний вибір'), ('MC', 'Множинний вибір'), ('G', 'Grid')], default='S', max_length=2, unique=True, verbose_name='Тип питання'),
        ),
        migrations.AlterField(
            model_name='result',
            name='persent',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='result',
            name='test',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='test_app.test'),
        ),
    ]