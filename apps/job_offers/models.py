from django.db import models


# Create your models here.
class JobOffer(models.Model):
    company_name = models.CharField(max_length=120)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=240)
    job_description = models.TextField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.CharField(max_length=240)
    state = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
