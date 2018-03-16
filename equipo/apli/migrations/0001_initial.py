# Generated by Django 2.0.2 on 2018-02-23 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='jugador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('estatura', models.DecimalField(decimal_places=1, max_digits=3)),
                ('pais', models.CharField(max_length=100)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apli.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='torneo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('lugar', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('equipo', models.ManyToManyField(blank=True, null=True, to='apli.equipo')),
            ],
        ),
    ]
