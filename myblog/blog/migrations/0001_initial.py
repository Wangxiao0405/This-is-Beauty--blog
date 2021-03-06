# Generated by Django 2.1 on 2019-01-02 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.IntegerField()),
                ('dist', models.IntegerField(choices=[(1, '朝阳区'), (2, '海淀区'), (3, '东城区'), (4, '西城区'), (5, '石景山')], default=1)),
                ('shi', models.IntegerField()),
                ('hall', models.IntegerField()),
                ('floor', models.IntegerField(choices=[(1, '低层'), (2, '中层'), (3, '高层')], default=1)),
                ('school', models.IntegerField(choices=[(1, '是'), (2, '否')], default=1)),
                ('subway', models.IntegerField(choices=[(1, '是'), (2, '否')], default=2)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_email', models.BooleanField(default=False)),
                ('img', models.ImageField(upload_to='img/', verbose_name='头像')),
                ('phone', models.CharField(max_length=11, verbose_name='电话')),
                ('company', models.CharField(max_length=30, verbose_name='所在公司')),
                ('job', models.CharField(max_length=20, verbose_name='所从事的职业')),
                ('science', models.CharField(max_length=30, verbose_name='感兴趣的方面')),
                ('reason', models.CharField(max_length=200, verbose_name='开通博客的理由')),
                ('real_name', models.CharField(max_length=10, verbose_name='真实姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('sex', models.IntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别')),
                ('salary', models.IntegerField(verbose_name='月薪')),
                ('isadv', models.IntegerField()),
                ('u', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KeyWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
        ),
    ]
