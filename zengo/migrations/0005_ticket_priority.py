# Generated by Django 2.2.10 on 2020-02-28 18:25

from django.db import migrations
import konst.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("zengo", "0004_zendeskuser_alias"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="priority",
            field=konst.models.fields.ConstantChoiceCharField(
                choices=[
                    ("urgent", "urgent"),
                    ("high", "high"),
                    ("normal", "normal"),
                    ("low", "low"),
                ],
                default="low",
                max_length=8,
            ),
            preserve_default=False,
        ),
    ]
