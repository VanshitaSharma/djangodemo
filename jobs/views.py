from django.shortcuts import render

# Create your views here.
def jobs_list(request):
    jobs=job.objects.all()
def job_details_views(request):
    pass
