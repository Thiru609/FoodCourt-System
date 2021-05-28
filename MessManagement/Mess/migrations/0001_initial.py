# Generated by Django 2.2.5 on 2019-10-26 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('Admin_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('Food_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Cost', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='mess',
            fields=[
                ('Mess_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Block', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q')], max_length=1)),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('Student_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Balance', models.FloatField(max_length=100)),
                ('Mess_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mess.mess')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('Order_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Time', models.DateField()),
                ('Food_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mess.food')),
            ],
        ),
    ]
