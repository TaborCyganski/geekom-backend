# Generated by Django 4.1.7 on 2024-05-17 15:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('geekom', '0006_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Description_of_conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=500, null=True)),
                ('Conversation_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geekom.conversation')),
            ],
        ),
    ]
