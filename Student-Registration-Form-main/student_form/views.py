from django.shortcuts import render
from .models import Details
# Create your views here.
from django.http import HttpResponseRedirect
from .forms import StudentForm

def home(request):
    return render(request,'index.html',{})
    
def student_details(request):
    details_list = Details.objects.all()
    return render (request,'index1.html',{'details_list': details_list})


def student_form(request):
    submitted = False 
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/student_form?submitted=True')

    else:
        form = StudentForm
        if 'submitted' in request.GET:
            submitted = True 
    return render (request,'student_form.html',{'form':form, 'submitted': submitted})



def list_students(request,student_id):
    students_list_individual = Details.object.get(pk= student_id)
    return render (request,'students.html',{'students_list_individual': students_list_individual})


def search_students(request):
    if request.method == "POST":
        searched = request.POST['searched']
        information = Details.objects.filter(first_name__contains= searched)

        return render (request,'search_student.html',{'searched': searched,'information':information})

    else:
         return render (request,'search_student.html',{})

