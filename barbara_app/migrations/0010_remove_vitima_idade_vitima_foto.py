# Generated by Django 5.1.1 on 2024-10-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbara_app', '0009_remove_ocorrencia_nome_agressor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vitima',
            name='idade',
        ),
        migrations.AddField(
            model_name='vitima',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_vitimas/'),
        ),
    ]
