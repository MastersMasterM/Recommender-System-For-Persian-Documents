"""
Defining the task of recomputing recommendations based on db
"""
from core.models import Paper

import pickle
from celery import shared_task


@shared_task
def export_paper_table():
    papers = Paper.objects.all()

    with open('paper_data.pkl', 'wb') as file:
        data = []
        for paper in papers:
            data.append([paper.uid, paper.title, paper.abstract, paper.fl_subject, paper.sl_subject])
        pickle.dump(data, file)

    print('Data export completed.')