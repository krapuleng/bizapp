# Generated by Django 3.2.6 on 2022-01-06 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appcash', '0004_auto_20220106_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashapp_cashtransaction',
            name='transactionAccount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcash.transactionaccount'),
        ),
        migrations.AlterField(
            model_name='cashapp_cashtransaction',
            name='transactiontype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcash.cashapp_transactiontype'),
        ),
    ]
