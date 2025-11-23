from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formsubmission",
            name="nam_sinh",
            field=models.DateField(blank=True, null=True),
        ),
    ]
