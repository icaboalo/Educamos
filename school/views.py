import os
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from school.forms import AudioForm
from .models import *
from audio.models import *

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
            subjects.setdefault('subject', []).append(subject)

        dictionary = {'classroom': classroom, 'subjects': subjects, 'user': user}
        print(dictionary)
        return render(request, 'index.html', dictionary)

def subject_view(request, pk):
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect("/login/")
    else:
        subject = Subject.objects.get(pk=pk)
        audios = {}
        audio_objects = Audio.objects.filter(subject=subject)
        for audio in audio_objects:
            audios.setdefault('audio', []).append(audio)
        print(audios)
        dictionary = {'subject': subject, 'audios': audios, 'professor': user.is_professor}
        print(user.username)

        if request.method == 'POST':
            form = AudioForm(request.POST, request.FILES)
            print(request.FILES)
            if form.is_valid():
                print('is valid')
                file = request.FILES['file']
                instance = Audio(file=file, name=form.data['name'], subject=subject)
                instance.save()
                return HttpResponse(json.dumps({'hola': 'holi'}),  content_type = "application/json")
            else:
                print('is no valid',  form.errors)
                # return HttpResponseRedirect('/login/')
        else:
            print('nu ma')
            form = AudioForm()
            dictionary = {'subject': subject, 'audios': audios, 'professor': user.is_professor, 'form': form}
            return render(request, 'subject.html', dictionary)
        """
        else:
            print('ke pedo')
            return render(request, 'subject.html', dictionary)
"""
