from django.shortcuts import render

# Create your views here.
def projects(request):
    return render(request, 'projects/index.html')

def project_detail(request, project_id):
    
    return render(request, 'projects/detail.html', {'project_id': project_id})