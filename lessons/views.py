from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, View

from lessons.models import Lesson
# Create your views here.





#With generic Views:
class lessonsGenericView(ListView):
    model = Lesson 
    context_object_name = 'lessons'


class lessonsDetail(DetailView):
    queryset = Lesson.objects.all()
    context_object_name = 'lesson'


""" class lessonsDetail(View):
    http_method_names = ['get']
    
    def get(self, request, id):
        lesson = Lesson.objects.get(id=id)
        students = lesson.students.all()
        context = {
            "lesson" : lesson,
            "students" : students
        }
        return render(request, 'lessons/detail.html', context) """






class lessonsView(View):
    http_method_names = ['post', 'get']
    
    def get(self, request):
        lessons = Lesson.objects.all()
        context = {
            "lessons" : lessons
        }
        return render(request, 'lessons/list.html', context)
    
    def post(self, request):
        lesson = request.POST
        new = Lesson.objects.create(name=lesson['name'])
        return self.get(request)