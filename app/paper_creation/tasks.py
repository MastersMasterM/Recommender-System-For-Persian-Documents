"""
Defining the task of recomputing recommendations based on db
"""
from time import sleep
from celery import shared_task


@shared_task
def recompute_embeddings():
    print('Recomputing Recommendation started....')
    sleep(10)
    print('Embeddings computed')
