from django.db import models

class questionBank(models.Model):
    question = models.CharField(max_length=300)
    bt = models.IntegerField()
    co = models.CharField(max_length=100)
    marks = models.IntegerField()
    unit = models.IntegerField()
    year = models.IntegerField()
    subname = models.CharField(max_length=100)
    flag = models.IntegerField()

    def __str__(self):
        return self.question

    class Meta:
        db_table = "questionBank"