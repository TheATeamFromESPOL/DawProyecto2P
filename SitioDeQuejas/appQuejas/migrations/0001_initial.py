# Generated by Django 2.1 on 2018-08-19 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=500)),
                ('fechaCreacion', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePersona', models.CharField(max_length=255)),
                ('apellidoPersona', models.CharField(max_length=255)),
                ('profesion', models.CharField(max_length=100)),
                ('numeroContacto', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Queja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('fechaCreacion', models.DateField(auto_now=True)),
                ('imagen', models.ImageField(upload_to='imgs/')),
                ('descripcion', models.CharField(max_length=1000)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appQuejas.Categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='queja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appQuejas.Queja'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
