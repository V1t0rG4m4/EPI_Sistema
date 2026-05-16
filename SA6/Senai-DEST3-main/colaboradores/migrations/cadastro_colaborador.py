from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Colaborador",
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
                ("nome", models.CharField(max_length=120, null=False, blank=False)),
                ("matricula", models.CharField(max_length=30, unique=True, null=False, blank=False)),
                ("setor", models.CharField(max_length=80, null=False, blank=False)),
                ("cargo", models.CharField(max_length=80, null=False, blank=False)),
                ("ativo", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ["nome"],
            },
        ),
    ]