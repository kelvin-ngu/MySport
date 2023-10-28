# Generated by Django 4.2.6 on 2023-10-28 06:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reflection', '0002_reflection_remove_historicalselfrating_history_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reflection',
            options={'ordering': ['player', 'created_at']},
        ),
        migrations.AddField(
            model_name='reflection',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reflection',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 10, 28, 6, 57, 52, 250379, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reflection',
            name='match_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('public', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='journal_by_player', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['player', 'created_at'],
            },
        ),
    ]
