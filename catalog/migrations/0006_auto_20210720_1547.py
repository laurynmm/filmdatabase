# Generated by Django 3.2.5 on 2021-07-20 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_review_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='film',
            name='director',
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(choices=[('D', 'Director'), ('A', 'Actor')], max_length=5)),
                ('if_actor_character_role', models.CharField(blank=True, max_length=100, null=True)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.film')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.person')),
            ],
        ),
    ]
