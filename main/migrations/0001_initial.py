# Generated by Django 4.1.4 on 2022-12-15 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aluno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("telefone", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("data_nascimento", models.DateField(null=True)),
                ("description", models.TextField()),
            ],
        ),
    ]
