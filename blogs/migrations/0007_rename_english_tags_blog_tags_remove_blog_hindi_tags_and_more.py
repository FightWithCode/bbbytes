# Generated by Django 4.2.4 on 2023-08-30 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0006_alter_blog_english_tags_alter_blog_front_image_233_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blog",
            old_name="english_tags",
            new_name="tags",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="hindi_tags",
        ),
        migrations.AlterField(
            model_name="blog",
            name="language",
            field=models.CharField(
                choices=[("English", "English"), ("Hindi", "Hindi")],
                default="English",
                max_length=10,
            ),
        ),
    ]
