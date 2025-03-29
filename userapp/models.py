from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import RegexValidator


class userreg(models.Model):
    fullname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)  # Should be hashed using make_password()
    email = models.EmailField()
    profile = models.ImageField(null=True, blank=True, upload_to='profiles/')



    def __str__(self):
        return self.fullname

class Complaints(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]

    user = models.ForeignKey(userreg, on_delete=models.CASCADE)  # ✅ Link complaint to user
    name = models.CharField(max_length=255)  # ✅ Store name directly
    email = models.EmailField()  # ✅ Store email directly
    phone = models.CharField(max_length=15)  # ✅ Keep phone, since it's not in userreg
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=20, decimal_places=7, default=0.0)
    longitude = models.DecimalField(max_digits=20, decimal_places=7, default=0.0)
    photo = models.ImageField(upload_to='complaint_photos/%Y/%m/%d/', blank=True, null=True)
    description = models.TextField()
    status_code = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    aadhaar_photo = models.ImageField(upload_to='aadhaar_photos/%Y/%m/%d/', blank=True, null=True)
    category = models.ForeignKey('adminapp.Category', on_delete=models.SET_NULL, null=True)
    assigned_officer = models.ForeignKey('adminapp.Officer', on_delete=models.SET_NULL, null=True, blank=True)
    date_of_incident = models.DateField(blank=True, null=True)
    proof_of_work = models.ImageField(upload_to='proof_of_work/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return f"Complaint by {self.name} - {self.status_code}"



from django.db import models

class Feedback(models.Model):
    user = models.ForeignKey('userreg', on_delete=models.CASCADE)  # Linking feedback to a user
    rate = models.PositiveIntegerField()  # Rating (out of 5)
    feedback = models.TextField()  # User's feedback text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for feedback submission

    def __str__(self):
        return f"Feedback from {self.user.name} - {self.rate}/5"
