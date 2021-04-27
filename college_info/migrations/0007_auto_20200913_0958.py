

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('college_info', '0006_auto_20200913_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 13, 4, 28, 28, 977694, tzinfo=utc)),
        ),
    ]
