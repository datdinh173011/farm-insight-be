from django.db import migrations, models


def reset_nam_sinh_to_zero(apps, schema_editor):
    FormSubmission = apps.get_model("forms", "FormSubmission")
    FormSubmission.objects.all().update(nam_sinh=0)


class Migration(migrations.Migration):
    dependencies = [
        ("forms", "0002_alter_formsubmission_nam_sinh"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formsubmission",
            name="nam_sinh",
            field=models.PositiveIntegerField(default=1980, blank=True, null=True),
        ),
        migrations.RunPython(
            reset_nam_sinh_to_zero,
            migrations.RunPython.noop,
        ),
    ]
