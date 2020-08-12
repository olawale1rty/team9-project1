# Generated by Django 3.1 on 2020-08-09 08:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MagazinePosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='magazine_pics')),
                ('title', models.CharField(max_length=100)),
                ('article', models.TextField()),
                ('category', models.CharField(choices=[('fashion', 'FASHION'), ('beauty', 'BEAUTY'), ('art', 'ART')], default='fashion', max_length=50)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
