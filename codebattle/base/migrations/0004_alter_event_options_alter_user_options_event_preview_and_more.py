# Generated by Django 4.2 on 2023-09-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_facebook_user_github_user_linkedin_user_twitter_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-end_date']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['avatar']},
        ),
        migrations.AddField(
            model_name='event',
            name='preview',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='details',
            field=models.TextField(null=True),
        ),
    ]