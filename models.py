from django.db import models
from django.contrib.auth.models import User  # For user-related models

# Case Model
class CaseDetails(models.Model):
    # case_id = models.OneToOneField(User, on_delete=models.CASCADE)
    case_suspect = models.CharField(max_length=20)
    case_type = models.CharField(max_length=100)
    case_description = models.TextField()
    case_judge = models.CharField(max_length=20)
    case_lawyer = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    prev_hearing_date = models.DateTimeField()
    next_hearing_date = models.DateTimeField()
    case_location = models.TextField()
    # Add more fields as needed

    def __str__(self):
        return self.case_suspect

# Previous Historical Cases
class PrevCases(models.Model):
    # pc_img = models.ImageField()
    pc_title = models.CharField(max_length=100)
    pc_description = models.TextField()
    # pc_lawyers = models.CharField(max_length=200)
    # pc_result = models.TextField()
    # pc_more_details = models.URLField()

    def __str__(self):
        return self.pc_title

class ContactUs(models.Model):
    username = models.CharField(max_length=30)
    useremail = models.CharField(max_length=30)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.username






"""
# User Model (Customized from Django's built-in User model)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)  # Judge, Lawyer, Litigant, Court Staff, etc.
    # Add more user-related fields as needed

# Hearing Model
class Hearing(models.Model):
    date_and_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    presiding_judge = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    cases = models.ManyToManyField(Case)

    
# Document Model
class Document(models.Model):
    document_type = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    upload_date = models.DateTimeField()
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    # Add more fields as needed

# Party Model
class Party(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)
    role = models.CharField(max_length=50)  # Plaintiff, Defendant, etc.
    cases = models.ManyToManyField(Case)

# Legal Counsel Model
class LegalCounsel(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)
    cases = models.ManyToManyField(Case)

# Calendar/Event Model
class CalendarEvent(models.Model):
    event_type = models.CharField(max_length=50)
    date_and_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    cases = models.ManyToManyField(Case)

# Notifications/Alerts Model
class Notification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Case Notes Model
class CaseNote(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    note = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Evidence Model
class Evidence(models.Model):
    evidence_type = models.CharField(max_length=50)
    description = models.TextField()
    source = models.CharField(max_length=100)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    # Add more fields as needed

# Payment/Finance Model (if applicable)
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

# Settings/Configuration Model
class Settings(models.Model):
    # Define your system-wide settings fields here
    pass

# Audit Log Model
class AuditLog(models.Model):
    action = models.CharField(max_length=100)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

# Access Control Model
class AccessControl(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # Define fields for permissions and roles here
    pass

# Statistics/Analytics Model (if needed)
class Statistics(models.Model):
    # Define fields for statistical data here
    pass

# Location/Room Model
class Location(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed

# User Activity Model
class UserActivity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
"""