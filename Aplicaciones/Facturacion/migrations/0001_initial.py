# Generated by Django 4.2.7 on 2024-01-17 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_bg', models.AutoField(primary_key=True, serialize=False)),
                ('apellido_bg', models.CharField(max_length=150)),
                ('nombre_bg', models.CharField(max_length=150)),
                ('edad_bg', models.IntegerField()),
                ('fotografia_portada', models.FileField(blank=True, null=True, upload_to='autor')),
            ],
        ),
        migrations.CreateModel(
            name='GeneroLiterario',
            fields=[
                ('id_bg', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_bg', models.CharField(max_length=150)),
                ('descripcion_bg', models.TextField()),
                ('fotografia_referencia', models.FileField(blank=True, null=True, upload_to='genero')),
            ],
        ),
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('id_bg', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_bg', models.CharField(max_length=150)),
                ('descripcion_bg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_bg', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_bg', models.CharField(max_length=150)),
                ('editorial_bg', models.CharField(max_length=150)),
                ('fecha_publicacion_bg', models.DateField()),
                ('fotografia_portada', models.FileField(blank=True, null=True, upload_to='portada')),
                ('autor_bg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Facturacion.autor')),
                ('genero_bg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Facturacion.generoliterario')),
            ],
        ),
        migrations.AddField(
            model_name='autor',
            name='profesion_bg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Facturacion.profesion'),
        ),
    ]
