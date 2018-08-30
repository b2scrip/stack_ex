from django.db import models
from django.urls import reverse

class Question(models.Model):
    postid       = models.IntegerField()
    ownuserid    = models.IntegerField()
    title        = models.CharField(max_length=200,blank=True)
    content      = models.TextField() 
    score        = models.IntegerField() 
    viewcount    = models.IntegerField()   
    tags         = models.CharField(max_length=200,blank=True)
    answercount  = models.IntegerField() 
    creationdate = models.DateTimeField(auto_now_add=False, auto_now=True)
    origindate   =  models.CharField(max_length=200,blank=True)

    class Meta:
        db_table = "eos_question"
        ordering = ['-pk']

    def get_absolute_url(self):
        return reverse('eos_detail', kwargs={'pk':self.pk})
    def increase_views(self):
        self.viewcount  += 1
        self.save(update_fields=['viewcount'])


class Answer(models.Model):
    parentid     = models.IntegerField()
    ownuserid    = models.IntegerField()	
    content      = models.TextField() 
    score        = models.IntegerField() 	
    commentcount  = models.IntegerField() 
    creationdate = models.DateTimeField(auto_now_add=False, auto_now=True)
    origindate   = models.CharField(max_length=200,blank=True)
    class Meta:
        db_table = "eos_answer"
