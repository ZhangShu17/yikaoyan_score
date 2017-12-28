#!/usr/bin/python2.7 
# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Students_info(models.Model):
    '''
    记录学员姓名，学校，专业，单科和总分，以及排名
    '''
    name=models.CharField(max_length=30)
    university=models.CharField(max_length=50)
    major=models.CharField(max_length=50)
    english_score=models.IntegerField()
    math_score=models.IntegerField()
    political_score=models.IntegerField()
    major_score=models.IntegerField()
    total_score=models.IntegerField()
    rank=models.IntegerField()
    objects=models.Manager()
    def __unicode__(self):
        return self.name