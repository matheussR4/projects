# Generated by Django 4.1.4 on 2022-12-25 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0008_alter_ingresso_tipo_alter_sessao_encerrada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='projecao',
            field=models.CharField(choices=[('2D', '2D'), ('3D', '3D')], max_length=2, verbose_name='Projeção'),
        ),
        migrations.AlterField(
            model_name='sessao',
            name='projecao',
            field=models.CharField(choices=[('2D', '2D'), ('3D', '3D')], max_length=2, verbose_name='Projeção'),
        ),
    ]
