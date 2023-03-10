# Generated by Django 4.0.3 on 2023-02-14 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.CharField(max_length=200)),
                ('credits', models.IntegerField()),
                ('grade', models.FloatField()),
                ('create_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('credit', models.IntegerField()),
                ('create_at', models.DateTimeField()),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sju.semester')),
            ],
        ),
    ]
