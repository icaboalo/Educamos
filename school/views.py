from django.http import HttpResponseRedirect
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

        dictionary = {'classroom': classroom, 'subjects': subjects, 'professor': user.is_professor}
        print(dictionary)
        return render(request, 'index.html', dictionary)

def subject_view(request, pk):
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect("/login/")
    else:
        subject = Subject.objects.get(pk=pk)

        if request.method == 'POST':
            print(request.user)
            form = AudioForm(request.POST)
            if form.is_valid():

                return HttpResponseRedirect('/materia/' + str(subject.pk))

        else:
            audios = {}
            audio_objects = Audio.objects.filter(subject=subject)
            for audio in audio_objects:
                print(audio.file.url)
                audios.setdefault('audio', []).append(audio)
            print(audios)
            dictionary = {'subject': subject, 'audios': audios, 'professor': user.is_professor}
            return render(request, 'subject.html', dictionary)