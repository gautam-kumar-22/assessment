from django.db import models

# Create your models here.

# Create your models here.
class TimeStampedModel(models.Model):
    """TimeStampedModel.
    An abstract base class model that provides self-managed "created" and
    "updated" fields.
    """

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        get_latest_by = 'modified_on'
        ordering = ('-modified_on', '-created_on',)
        abstract = True


class Question(TimeStampedModel):
    question = models.TextField(max_length=255, blank=False, null=False)
    relevance_marks = models.IntegerField(blank=False, null=False, default=1)


class Result(TimeStampedModel):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(null=False, blank=False, default=0) 
    marks = models.IntegerField(null=False, blank=False, default=0)
    ip_address = models.CharField(max_length=50, null=True, blank=True)
