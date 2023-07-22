from django.db import models
from ckeditor.fields import RichTextField

from apps.main.models import BaseModel


class Department(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Video(BaseModel):
    title = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='video')
    description = models.TextField()
    condition_choices = [
        ('good', 'Good'),
        ('average', 'Average'),
        ('poor', 'Poor'),
    ]
    condition = models.CharField(max_length=10, choices=condition_choices)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_comment')
    message = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Comment by {self.user.username}"


class Course(BaseModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='course_video')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='course_comment')
    photo = models.ImageField(upload_to='course/')
    degree_choices = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    degree = models.CharField(max_length=12, choices=degree_choices)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(decimal_places=2)
    discount = models.IntegerField()

    def __str__(self):
        return self.title


class Species(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Complaint(BaseModel):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_complaint')
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name='species_complaint')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_complaint')
    message = models.TextField()

    def __str__(self):
        return f"Complaint by {self.user.username}"

