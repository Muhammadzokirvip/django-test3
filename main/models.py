from django.db import models

class LoginSigin(models.Model):
    login_name = models.CharField(max_length=255)
    email = models.EmailField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.ImageField()


class Download(models.Model):
    title = models.CharField(max_length=255)
    percentage_complete = models.IntegerField()
    is_complete = models.BooleanField(default=False)


class Upload(models.Model):
    title = models.CharField(max_length=255)
    percentage_complete = models.IntegerField()
    is_complete = models.BooleanField(default=False)


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    percentage_complete = models.IntegerField()
    is_complete = models.BooleanField(default=False)


class MonthlyIncome(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    date_recorded = models.DateField()

    
class Message(models.Model):
    sender_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    content = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Message from {self.sender_name} on {self.timestamp}"


class Message(models.Model):
    sender_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    content = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Message from {self.sender_name} on {self.timestamp}"


class TopActiveMember(models.Model):
    name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    views = models.IntegerField()
    country = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    comments = models.IntegerField()

    def __str__(self):
        return f"{self.name} from {self.country}"
