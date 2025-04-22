from django.db import models
from django.contrib.auth.models import User
class School(models.Model):
    class Meta:
        verbose_name='学校'
        verbose_name_plural='学校'
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    school_name=models.CharField(max_length=200,verbose_name='学校名称')
    def __str__(self):
        return self.school_name
class Class(models.Model):
    class Meta:
        verbose_name='班级'
        verbose_name_plural='班级'
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    class_name=models.CharField(max_length=200,verbose_name='班级名称')
    def __str__(self):
        return self.class_name
class Activity(models.Model):
    class Meta:
        verbose_name='活动'
        verbose_name_plural='活动'
    _class=models.ForeignKey(Class, on_delete=models.CASCADE)
    start_time=models.DateTimeField(max_length=200,verbose_name='开始时间')
    end_time=models.DateTimeField(max_length=200,verbose_name='结束时间')
    activity_name=models.CharField(max_length=200,verbose_name='活动名称')
    activity_description=models.CharField(max_length=200,verbose_name='活动描述')
    def __str__(self):
        return "开始时间:"+str(self.start_time)+'\n结束时间:'+str(self.end_time)+'\n活动名称:'+self.activity_name+'\n活动描述:'+self.activity_description