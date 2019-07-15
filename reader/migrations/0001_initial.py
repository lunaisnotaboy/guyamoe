# Generated by Django 2.2.3 on 2019-07-14 15:43

from django.db import migrations, models
import django.db.models.deletion
import reader.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='series_artist', to='reader.Person')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='series_author', to='reader.Person')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='HitCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='Hits')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_number', models.PositiveIntegerField()),
                ('volume_cover', models.ImageField(blank=True, upload_to=reader.models.path_file_name)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.Series')),
            ],
            options={
                'unique_together': {('volume_number', 'series')},
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('chapter_number', models.FloatField()),
                ('folder', models.CharField(blank=True, max_length=255, null=True)),
                ('page_count', models.PositiveSmallIntegerField()),
                ('volume', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('uploaded_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reader.Group')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.Series')),
            ],
            options={
                'ordering': ('chapter_number',),
                'unique_together': {('chapter_number', 'series', 'group')},
            },
        ),
    ]