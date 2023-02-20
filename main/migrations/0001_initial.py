# Generated by Django 4.1.7 on 2023-02-20 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('direction', models.CharField(choices=[('Backend', 'Backend'), ('Frontend', 'Frontend'), ('UX/UI', 'UX/Ui'), ('Fullstack', 'Fullstack')], max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
            ],
        ),
    ]
