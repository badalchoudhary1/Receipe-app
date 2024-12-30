from django.db import models

class Reciepe(models.Model):
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe/")
    created_at = models.DateTimeField(auto_now_add=True)  # New field to track when the recipe is created

    def __str__(self):
        return self.receipe_name
