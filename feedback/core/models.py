from django.db import models

# Create your models here.


from django.db import models

class Feedback(models.Model):
    rating = models.PositiveSmallIntegerField(default=1)  # Star rating from 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating: {self.rating}"
