# Generated by Django 5.0.1 on 2024-04-02 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='post',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='conversacion',
            name='estatus',
            field=models.CharField(choices=[('enviado', 'Enviado'), ('recibido', 'Recibido'), ('leido', 'Leído')], max_length=10),
        ),
    ]
