"""
Defining the task of recomputing recommendations based on db
"""
from core.models import Paper

import csv
from celery import shared_task


@shared_task
def export_paper_table():
    papers = Paper.objects.all()

    with open('paper_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['uid', 'title', 'abstract', 'fl_subject', 'sl_subject'])  # Add column headers

        for paper in papers:
            writer.writerow([paper.uid, paper.title, paper.abstract, paper.fl_subject, paper.sl_subject])  # Write data rows

    print('Data export completed.')