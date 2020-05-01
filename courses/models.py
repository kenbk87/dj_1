from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=1000)
    educator = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=300)
    description = models.TextField()
    num_lessons = models.PositiveSmallIntegerField(default=0)
    picture = models.ImageField(upload_to='course_picture')

    def __str__(self):
        return self.name

