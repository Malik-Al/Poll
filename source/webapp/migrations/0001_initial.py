# Generated by Django 2.2 on 2020-08-08 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='Опрос')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Текст')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='webapp.Poll', verbose_name='Опрос')),
            ],
        ),
    ]