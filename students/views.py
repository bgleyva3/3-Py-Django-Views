from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from students.models import Student
# Create your views here.


#With more readable formart:
class studentsView(View):
    http_method_names = ['post', 'get']

    def get(self, request):
        students = Student.objects.all()
        context = {
            "students" : students
        }
        return render(request, 'students/list.html', context)
    
    def post(self, request):
        student = request.POST
        new = Student.objects.create(name=student['name'], email=student['email'], phone=student['phone'], semester=student['semester'])
        return self.get(request)

class studentsID(View):
    http_method_names = ['get']

    def get(self, request, id):
        student = Student.objects.get(id=id)
        context = {
            "student" : student
        }
        return render(request, 'students/detail.html', context)
    



#With manual logic elaboration:
""" def students(request):
    if request.method == 'POST':
        student = request.POST
        new = Student.objects.create(name=student['name'], email=student['email'], phone=student['phone'], semester=student['semester'])
    students = Student.objects.all()
    context = {
        "students" : students
    }
    
    return render(request, 'students/list.html', context)

def students_id(request, id):
    student = Student.objects.get(id=id)
    context = {
        "student" : student
    }
    return render(request, 'students/detail.html', context) """




#With HttpResponse:
"""     def studentsView(request):
    student = Student.objects.all()
    list = ''
    print(student)
    print("-----------------------")
    for i in student: 
        list += f'''
            <li>
                <div>
                    <b>Name:</b> {i.name}
                </div>
                <div>
                    <b>Email:</b> {i.email}
                </div>
            </li>
            '''

    response = f'''
        <html>
            <body>
                <h1>Students</h1>
                <ul>
                    {list}
                </ul>
            </body>
        </html>
        '''
    
    return HttpResponse('{"hola": "mundo"}') """