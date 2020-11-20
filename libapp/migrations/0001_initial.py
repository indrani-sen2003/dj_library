# Generated by Django 2.2.16 on 2020-10-29 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('dod', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=100)),
                ('isbn', models.CharField(help_text='unique code required', max_length=10, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libapp.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='bookinstance',
            fields=[
                ('uniqueid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('due_back', models.DateField()),
                ('status', models.CharField(choices=[('i', 'issued'), ('a', 'available'), ('r', 'reserved')], max_length=1)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libapp.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='libapp.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libapp.Lang'),
        ),
    ]
