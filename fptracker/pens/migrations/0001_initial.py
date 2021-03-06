# Generated by Django 3.0.6 on 2020-12-03 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelName', models.CharField(max_length=100)),
                ('brandName', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=7)),
                ('nibsSizes', models.CharField(choices=[('B', 'Broad'), ('M', 'Medium'), ('F', 'Fine'), ('E', 'Extra Fine')], max_length=2)),
                ('datePurchases', models.DateField()),
            ],
        ),
    ]
