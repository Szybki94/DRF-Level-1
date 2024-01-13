from django.db import models


# Create your models here.
class JobOffer(models.Model):
    company_name = None
    company_email = None
    job_title = None
    job_description = None
    salary = None
    city = None
    state = None
    created_at = None
    available = None

# Modele:
# Dla projektu wymagany jest tylko jeden model, który można nazwać JobOffer. Powinien on zawierać następujące pola:
# - company_name
# - company_email
# - job_title
# - job_description
# - salary
# - city
# - state
# - created_at
# - available
