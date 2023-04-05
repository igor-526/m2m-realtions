# Generated by Django 4.2 on 2023-04-04 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='arcticle_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope', to='articles.tag'),
        ),
    ]
