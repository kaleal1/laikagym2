# Generated by Django 4.0.5 on 2022-07-17 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gimnasio', '0002_remove_routine_routineexcercise_routineexcercise'),
    ]

    operations = [
        migrations.RenameField(
            model_name='routineexcercise',
            old_name='ExcerciseId',
            new_name='Excercise',
        ),
        migrations.RenameField(
            model_name='routineexcercise',
            old_name='RoutineId',
            new_name='Routine',
        ),
    ]
