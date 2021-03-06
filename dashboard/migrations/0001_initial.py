# Generated by Django 2.0.2 on 2018-03-28 19:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Educator',
            fields=[
                ('user',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to=settings.AUTH_USER_MODEL)),
                ('title', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('about_me', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EducatorAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Account')),
                ('educator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Educator')),
            ],
        ),
        migrations.CreateModel(
            name='EducatorAdvice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('educator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Educator')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to=settings.AUTH_USER_MODEL)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.SmallIntegerField()),
                ('family_size',
                 models.CharField(choices=[('LE3', 'Less or equal to 3'), ('GT3', 'Greater than 3')], max_length=3)),
                ('parent_status', models.CharField(choices=[('T', 'Living together'), ('A', 'Apart')], max_length=1)),
                ('mother_education', models.SmallIntegerField()),
                ('father_education', models.SmallIntegerField()),
                ('guardian', models.CharField(choices=[('mother', 'Mother'), ('father', 'Father'), ('other', 'Other')],
                                              max_length=10)),
                ('mother_job', models.CharField(
                    choices=[('teacher', 'Teacher'), ('health', 'Health Related'), ('services', 'Services'),
                             ('at_home', 'At Home'), ('other', 'Other')], max_length=10)),
                ('father_job', models.CharField(
                    choices=[('teacher', 'Teacher'), ('health', 'Health Related'), ('services', 'Services'),
                             ('at_home', 'At Home'), ('other', 'Other')], max_length=10)),
                ('travel_time', models.SmallIntegerField()),
                ('do_extra_activity', models.BooleanField()),
                ('wants_higher_education', models.BooleanField()),
                ('has_internet', models.BooleanField()),
                ('has_relationship', models.BooleanField()),
                ('family_relation_quality', models.SmallIntegerField()),
                ('free_time', models.SmallIntegerField()),
                ('go_out_time', models.SmallIntegerField()),
                ('health_status', models.SmallIntegerField()),
                ('department',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Department')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_time', models.SmallIntegerField()),
                ('failures', models.SmallIntegerField()),
                ('absences', models.SmallIntegerField()),
                ('has_family_support', models.BooleanField()),
                ('take_paid_class', models.BooleanField()),
                ('midterm_grade', models.SmallIntegerField()),
                ('final_grade', models.SmallIntegerField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
                ('educator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Educator')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('is_anonymous', models.BinaryField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentReviewItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.SmallIntegerField()),
                ('review_item',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.ReviewItem')),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('student_review',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to='dashboard.StudentReview')),
            ],
        ),
        migrations.AddField(
            model_name='studentreviewitem',
            name='student_review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.StudentReview'),
        ),
        migrations.AddField(
            model_name='studentreview',
            name='educator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Educator'),
        ),
        migrations.AddField(
            model_name='studentreview',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Student'),
        ),
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Year'),
        ),
        migrations.AddField(
            model_name='educatoradvice',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='educator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Educator'),
        ),
        migrations.AddField(
            model_name='course',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Term'),
        ),
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Year'),
        ),
        migrations.AlterUniqueTogether(
            name='studentreviewitem',
            unique_together={('student_review', 'review_item')},
        ),
        migrations.AlterUniqueTogether(
            name='educatoraccounts',
            unique_together={('educator', 'account')},
        ),
    ]
