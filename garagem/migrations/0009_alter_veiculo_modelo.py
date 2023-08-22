# Generated by Django 4.1.7 on 2023-05-05 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0008_alter_veiculo_modelo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="veiculo",
            name="modelo",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="garagem.modelo"),
        ),
    ]
