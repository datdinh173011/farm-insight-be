from django.db import migrations


def rename_slug_to_template_type(apps, schema_editor):
    table = apps.get_model("forms", "FormTemplate")._meta.db_table
    with schema_editor.connection.cursor() as cursor:
        columns = [
            col.name
            for col in schema_editor.connection.introspection.get_table_description(
                cursor, table
            )
        ]
    if "template_type" in columns:
        return
    if "slug" not in columns:
        return
    schema_editor.execute(
        f'ALTER TABLE {schema_editor.quote_name(table)} '
        f'RENAME COLUMN {schema_editor.quote_name("slug")} '
        f'TO {schema_editor.quote_name("template_type")}'
    )


class Migration(migrations.Migration):
    dependencies = [
        ("forms", "0003_alter_formsubmission_nam_sinh"),
    ]

    operations = [
        migrations.RunPython(rename_slug_to_template_type, migrations.RunPython.noop),
    ]
