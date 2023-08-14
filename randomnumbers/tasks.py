import random
from celery import shared_task
from randomnumbers.models import RandomNumber
import time


@shared_task()
def generate_random_number(request_id):
    """Generates a random number from 0 to 100 and persists it on the random number request"""
    rn = RandomNumber.objects.get(id=request_id)
    num = random.randrange(100)
    time.sleep(10)
    rn.number = num
    rn.save()