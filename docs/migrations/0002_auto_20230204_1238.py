# Generated by Django 3.2 on 2023-02-04 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='topic',
            field=models.ForeignKey(limit_choices_to=models.Q(parent__isnull=False), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sections', to='docs.topic', verbose_name='Topic'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(parent__isnull=True), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subtopics', to='docs.topic', verbose_name='Related To'),
        ),
    ]
