# Generated by Django 5.0.1 on 2024-04-12 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0009_course_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_amount', models.CharField(verbose_name='сумма оплаты')),
                ('payment_link', models.URLField(blank=True, max_length=400, null=True, verbose_name='ссылка на оплату')),
                ('payment_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='id_of_payment')),
            ],
            options={
                'verbose_name': 'оплата курса',
                'verbose_name_plural': 'оплаты курсов',
            },
        ),
    ]
