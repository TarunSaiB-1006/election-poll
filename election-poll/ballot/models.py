# Create your models he
from django.db import models
import uuid
# Create your models here.
class Candidate(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    gender = models.CharField(default="M", max_length=1, choices={"M": "M", "F": "F"})
    student_class = models.CharField(max_length=3, choices={"IX": "IX", "XI": "XI"})  
    section = models.CharField(max_length=3, choices={"A": "A", "B": "B", "C": "C", "D":"D"})
    post_preference_1 = models.CharField(max_length=50)
    post_preference_2 = models.CharField(max_length=50, blank=True, null=True)
    number_of_votes = models.PositiveIntegerField(default=0)
    number_of_votes.editable = True
    logo_path = models.ImageField(blank=True, upload_to='ballot/logos/')
    image_path = models.ImageField(blank=True, upload_to='ballot/candidate_images/')

    def __str__(self):
        return f"{self.name} ({self.student_class}-{self.section})"

    class Meta:
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'
