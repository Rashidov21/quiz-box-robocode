from django.db import models
from django_quill.fields import QuillField

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
    author = models.ForeignKey(LeadUser, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    times_taken = models.IntegerField(default=0, editable=False)
    image = models.ImageField(
        upload_to='quiz_image/', blank=True, null=True)

    @property
    def question_count(self):
        ''' Method to get num of Qs for this quiz, used in Serializer'''
        return self.questions.count()

    class Meta:
        verbose_name_plural = "Quizzes"
        ordering = ['id']

    def __str__(self):
        return self.title


class Question(models.Model):
    label = QuillField()
    order = models.PositiveIntegerField(blank=True, null=True)
    point = models.PositiveIntegerField(default=3.3)
    image = models.ImageField(
        upload_to='question_image/', blank=True, null=True)
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return str(self.label)


class Answer(models.Model):
    text = models.TextField(max_length=150)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return str(self.text)
