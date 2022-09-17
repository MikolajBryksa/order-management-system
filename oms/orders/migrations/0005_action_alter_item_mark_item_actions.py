# Generated by Django 4.1.1 on 2022-09-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_item_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Printing', 'Printing'), ('Lamination', 'Lamination'), ('Slicing', 'Slicing'), ('Sticking', 'Sticking'), ('Milling', 'Milling'), ('Cutting', 'Cutting'), ('Laser', 'Laser'), ('Engraver', 'Engraver'), ('Resin', 'Resin'), ('Fastening', 'Fastening'), ('Folding', 'Folding')], max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='mark',
            field=models.CharField(choices=[('Print', 'Print'), ('Engraver', 'Engraver'), ('Foil', 'Foil'), ('Sticker', 'Sticker'), ('Outsource', 'Outsource'), ('Without', 'Without'), ('Custom', 'Custom')], max_length=50),
        ),
        migrations.AddField(
            model_name='item',
            name='actions',
            field=models.ManyToManyField(to='orders.action'),
        ),
    ]
