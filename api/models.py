from django.db import models


class Client(models.Model):
    
    name = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='clients', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):

    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE)
    rate = models.FloatField(default=0)
    def __str__(self):
        return self.name


class TimeLog(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    hours = models.FloatField()
    date = models.DateField(auto_now=True)
    client = models.ForeignKey(Client, related_name='time_logs', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='time_logs', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='time_logs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title