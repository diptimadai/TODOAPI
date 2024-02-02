from django.db import models

class TODO(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title}-{self.description}"
    