# Generated by Django 3.2 on 2021-12-10 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photos',
            options={'verbose_name_plural': 'Photos'},
        ),
        migrations.AddField(
            model_name='photos',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.album'),
        ),
    ]
