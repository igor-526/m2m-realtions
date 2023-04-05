# Generated by Django 4.2 on 2023-04-04 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_rename_tag_id_scope_tag_alter_scope_arcticle_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='arcticle_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag'),
        ),
    ]
