from django.db import models
from school.models import Subject

# Create your models here.
class Audio(models.Model):

    class Meta:
        verbose_name = 'Audio'
        verbose_name_plural = 'Audios'

    # Relations
    subject = models.ForeignKey(Subject)

    # Attributes
    name = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='audios/', null=True, blank=True)

    def __str__(self):
        return self.name