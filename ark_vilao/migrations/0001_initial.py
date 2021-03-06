# Generated by Django 2.2.5 on 2019-09-24 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('universos', '0001_initial'),
        ('habilidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vilao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('hab_vilao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hab_vilao', to='habilidades.Habilidades')),
                ('uni_vilao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='univer_vilao', to='universos.Universos')),
            ],
        ),
    ]
