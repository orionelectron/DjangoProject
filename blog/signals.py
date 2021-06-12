from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Post
from .search import add_to_index, remove_from_index, query_index


@receiver(post_save, sender=Post)
def create_index(sender, instance, created, **kwargs):
    if created:
        add_to_index('posts', instance)
        
@receiver(post_delete, sender=Post)
def remove_document_from_index(sender, instance, **kwargs):
    remove_from_index('posts', instance)

