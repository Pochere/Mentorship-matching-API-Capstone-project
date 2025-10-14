from django.db import models
from django.contrib.auth.models import User

# Mentor model
class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    expertise = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"Mentor: {self.user.username}"


# Mentee model
class Mentee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.CharField(max_length=150)
    goals = models.TextField(blank=True)

    def __str__(self):
        return f"Mentee: {self.user.username}"


# Mentorship Session model
class MentorshipSession(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    mentee = models.ForeignKey(Mentee, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Session between {self.mentor.user.username} and {self.mentee.user.username} on {self.date}"

""" Mentor - stores details about mentors - a OneToOneField
    that connects each mentor to a user account,
    Mentee - Stores details about mentees and is also connected to a user
    MentorshipSession - reps mentorship meetings between a mentor and mentee
    and uses ForeignKey to link both(many-to-one-relationship)

"""