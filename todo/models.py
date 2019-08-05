# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime 
# Create your models here.

class List(models.Model): 
    title = models.CharField(max_length=250, unique=True) 
    def __str__(self): 
        return self.title 
    class Meta: 
        ordering = ['title'] 
    class Admin: 
        pass
    

PRIORITY_CHOICES = ( 
  (1, 'Niedrig'), 
  (2, 'Mittel'), 
  (3, 'Hoch'), 
  (4, 'Diese Woche'),
) 
PRIORITY_COLOURS = {
    1: "#e6ffe6",
    2: "#ffff99",
    3: "#ff6666",
    4: "#66ccff",
}

class Item(models.Model): 
    title = models.CharField(max_length=250) 
    created_date = models.DateTimeField(default=datetime.datetime.now) 
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) 
    completed = models.BooleanField(default=False) 
    todo_list = models.ForeignKey(List) 
    estimation = models.FloatField(default=1.0)
    remaining_estimation = models.FloatField(default=1.0)
    date_finished = models.DateTimeField(default=datetime.datetime.fromtimestamp(0))
    def __str__(self): 
        return self.title 
    def priority_color(self):
        return PRIORITY_COLOURS[self.priority]
    class Meta: 
        ordering = ['-priority', 'title'] 
    class Admin: 
        pass
