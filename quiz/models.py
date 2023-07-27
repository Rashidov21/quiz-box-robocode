from django.db import models
from django.contrib.auth.models import User

# Create your models here.

INTEREST = (
    ("frontend", "Veb dasturlash Front-End"),
    ("backend", "Veb dasturlash Back-End"),
    ("mobil dasturlash", "Mobil dasturlash"),
    ("robototexnika", "Robototexnika"),
    ("grafik dizayn", "Grafik Dizayn"),
    ("3d", "3D modellashtirish"),
)


class LeadUser(models.model):
    full_name = models.CharField(max_length=255, blank=True)
    age = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=255, blank=True)
    interest = models.CharField(choices=INTEREST, max_length=255, blank=True)
    phone = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.full_name


class Quiz(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    times_taken = models.IntegerField(default=0, editable=False)

    @property
    def question_count(self):
        ''' Method to get num of Qs for this quiz, used in Serializer'''
        return self.questions.count()

    class Meta:
        verbose_name_plural = "Quizzes"
        ordering = ['id']

    def __str__(self):
        return self.title



