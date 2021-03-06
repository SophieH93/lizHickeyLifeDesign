# Generated by Django 3.1 on 2020-09-16 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='purchase_date',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='datetime',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='item_total',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=6),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='checkout.order'),
        ),
    ]
