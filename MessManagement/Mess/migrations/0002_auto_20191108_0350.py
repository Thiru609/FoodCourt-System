# Generated by Django 2.2.5 on 2019-11-07 22:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Mess', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('Food_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mess.food')),
            ],
        ),
        migrations.DeleteModel(
            name='admin',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Food_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Order_id',
        ),
        migrations.AddField(
            model_name='order',
            name='Mess_id',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.PROTECT, to='Mess.mess'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='Student_id',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.PROTECT, to='Mess.student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.AutoField(default=-1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='Password',
            field=models.CharField(max_length=256),
        ),
        migrations.AddField(
            model_name='cart',
            name='Order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mess.order'),
        ),
    ]
