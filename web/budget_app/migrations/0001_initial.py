# Generated by Django 2.1.2 on 2018-10-02 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled', max_length=180)),
                ('total_budget', models.FloatField()),
                ('remaining_budget', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('withdrawal', 'Withdrawal'), ('deposit', 'Deposit')], default='Deposit', max_length=15)),
                ('amount', models.FloatField()),
                ('description', models.TextField(blank=True, null=True)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='budget_app.Budget')),
            ],
        ),
    ]
