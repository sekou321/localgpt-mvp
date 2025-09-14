from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vote, Info

@receiver(post_save, sender=Vote)
def update_info_validated(sender, instance, **kwargs):
    info = instance.info
    info.validated = info.vote_score() >= 2  # seuil 2 votes
    info.save()
