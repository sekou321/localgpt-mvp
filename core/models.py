from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Info(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    contributor = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    validated = models.BooleanField(default=False)  # nouveau champ
    
    def vote_score(self):
            return self.votes.filter(vote_type='up').count() - self.votes.filter(vote_type='down').count()

    def save(self, *args, **kwargs):
        # met à jour le statut validé automatiquement
        self.validated = self.vote_score() >= 2
        super().save(*args, **kwargs)


class Vote(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(
        max_length=10,
        choices=(('up', 'Utile'), ('down', 'Non utile'))
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('info', 'user')


# Create your models here.
