from django.shortcuts import render
from .models import Semester, Subject, Chapter, Resource, Banner

# Create your views here.
def home(request):
	context = {
		 'semesters' : Semester.objects.all(),
		 'subjects' : Subject.objects.all(),
		 'chapters' : Chapter.objects.all(),
		 'resources' : Resource.objects.all(),
		 'banners' : Banner.objects.all(),
	}
	return render(request, 'main/index.html', context)

def subjects(request, id):
	context = {
		'subjects' : Subject.objects.filter(semester_name_id=id)
	}
	return render(request, 'main/subjects.html', context)


def chapters(request, id):
	context = {
		'chapters' : Chapter.objects.filter(subject_name_id=id)
	}
	return render(request, 'main/chapters.html', context)


def resources(request, id):
	context = {
		'resources' : Resource.objects.filter(chapter_title_id=id)
	}
	return render(request, 'main/resources.html', context)
