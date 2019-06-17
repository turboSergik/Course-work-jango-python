from django.db import models


class Edit(models.Model):
    question_num = models.CharField(max_length=256)
    question = models.CharField(max_length=256)
    fi_answer = models.TextField()

    se_answer = models.TextField()
    th_answer = models.TextField()
    fo_answer = models.TextField()
    fv_answer = models.TextField()
    correct_answer = models.CharField(max_length=256)