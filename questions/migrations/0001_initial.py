# Generated by Django 3.2.5 on 2021-07-22 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('question', models.CharField(max_length=255)),
                ('relevance_marks', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ('-modified_on', '-created_on'),
                'get_latest_by': 'modified_on',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('marks', models.IntegerField(default=0)),
                ('ip_address', models.CharField(blank=True, max_length=50, null=True)),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
            ],
            options={
                'ordering': ('-modified_on', '-created_on'),
                'get_latest_by': 'modified_on',
                'abstract': False,
            },
        ),
    ]
