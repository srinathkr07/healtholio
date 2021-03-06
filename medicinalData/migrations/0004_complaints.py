# Generated by Django 3.0.2 on 2020-01-30 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicinalData', '0003_dosage_med_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicinalData.Prescription')),
                ('symptom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicinalData.Symptom')),
            ],
        ),
    ]
