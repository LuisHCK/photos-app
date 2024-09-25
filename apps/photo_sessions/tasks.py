from celery import shared_task
from .models import Session


@shared_task
def delete_photos(id: str | int) -> None:
    """
    Deletes all the photos for a session to free up space
    but keeps the session for record keeping
    """
    try:
        photoshoot = Session.objects.get(id=id)
        # Delete all the photos, this will free up the space
        for photo in photoshoot.photo_set.all():
            photo.clean_photos()

        # update the status of the session
        photoshoot.status = 'expired'
        photoshoot.save()
        print(f"Photos deleted for session {id}")
    except:
        print(f"Error deleting photos for session {id}")
        return
