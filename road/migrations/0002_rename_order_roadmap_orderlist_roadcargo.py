# Generated by Django 4.1.2 on 2022-10-19 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_accepted_accepteddetail_dispatch_dispatchdetail_and_more'),
        ('road', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roadmap',
            old_name='order',
            new_name='orderlist',
        ),
        migrations.CreateModel(
            name='RoadCargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devoted', models.BooleanField(default=False)),
                ('dispatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.dispatch')),
                ('road', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='road.road')),
            ],
        ),
    ]