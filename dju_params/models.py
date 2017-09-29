from django.db import models

# Create your models here.

class StartLog(models.Model):
    gitsha1 = models.CharField(
        max_length=40,
    )

    timestart = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.gitsha1


def stampstart(sha1):
    s = StartLog(gitsha1=sha1)
    s.save()
