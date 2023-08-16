from celery.app import shared_task
from celery_progress.backend import ProgressRecorder
from random import random
import time

@shared_task(bind=True)
def randomizer(self, duration):
    for i in range(10):
        time.sleep(duration)
        self.update_state(
            state="PROGRESS",
            meta={'current': random.randint(1, 100), 'total': 100, 'percent': i / 100,}
        )
    return "Done"
