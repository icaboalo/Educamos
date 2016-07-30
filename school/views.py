from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *

# Create your views here.
def classroom_view(request, pk):
    user = request.user
    if not user.is_authenticated():
        print('not authenticated')
        return HttpResponseRedirect("/login/")
    else:
        print('authenticated')
        classroom = Classroom.objects.get(pk=pk)
        subjects = {}
        subjectObjects = Subject.objects.filter(classroom=classroom)
        for subject in subjectObjects:
            name = subject.name
            subjects.setdefault('name', []).append(name)

        return render(request, 'index.html', {'classroom': classroom, 'subjects': subjects})

def subject_view(request, pk):
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect("/login/")
    else:

        return render(request, 'subject.html')