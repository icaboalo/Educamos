from django.db import models

# Create your models here.

STATE_CHOICES = (
    (1, ''),
    (2, ''),
    (3, ''),
    (4, ''),
    (5, ''),
    (6, ''),
    (7, ''),
    (8, ''),
    (9, ''),
    (10, ''),
    (11, ''),
    (12, ''),
    (13, ''),
    (14, ''),
    (15, ''),
    (16, ''),
    (17, ''),
    (18, ''),
    (19, ''),
    (20, ''),
    (21, ''),
    (22, ''),
    (23, ''),
    (24, ''),
    (25, ''),
    (26, ''),
    (27, ''),
    (28, ''),
    (29, ''),
    (30, ''),
    (31, ''),
    (32, ''),
)


class School(models.Model):
    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

    # Relations

    # Attributes
    name = models.CharField(max_length=30)
    state = models.IntegerField(choices=STATE_CHOICES)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    class Meta:
        verbose_name = 'Classroom'
        verbose_name_plural = 'Classrooms'

    # Relations
    school = models.ForeignKey(School)

    # Attributes
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Subject(models.Model):

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    # Relations
    classroom = models.ForeignKey(Classroom)

    # Attributes
    name = models.CharField(max_length=20)
    # professor = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Schedule(models.Model):

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'

    DAY_CHOICES = (
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miercoles'),
        (4, 'Jueves'),
        (5, 'Viernes'),
    )

    # Attributes
    subject = models.ForeignKey(Subject)

    # Relations
    day = models.IntegerField(choices=DAY_CHOICES)
    start_hour = models.TimeField()
    end_hour = models.TimeField()
