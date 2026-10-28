from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
import csv
def insert_data(self):
    with open('D:\\Django\\venv\\Scripts\\projectBusiness\\Business-employment-data-september-2022-quarter-csv.csv') as FO:
        IDO=csv.reader(FO)
        next(IDO)
        for row in IDO:
            bo=Business(series_reference=row[0],period=row[1],Data_value=row[2],Suppressed=row[3],STATUS=row[4],UNITS=row[5],Magnitude=row[6],Subject=row[7],Group=row[8],Series_title_1=row[9])
            bo.save()



    return HttpResponse('data is inserted successfully')

def delete_data(self):
    Business.objects.all().delete()
    return HttpResponse('data is deleted successfully')