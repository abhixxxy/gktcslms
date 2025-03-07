from django.db import models

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('Programming', 'Programming'),
        ('Data Science', 'Data Science'),
        ('Design', 'Design'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in hours")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Programming')  # Add this
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
