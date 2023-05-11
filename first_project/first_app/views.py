from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from first_app.models import Program, Student

 
from .forms import StudentForm   

def index(request):
   program_values = Program.objects.all()
   student_values = Student.objects.all()

   my_dict = {'program_rows' : program_values,
              'student_rows' : student_values }
   return render(request,'index.html',my_dict)
 
def get_student(request):    
  if request.method == 'POST':          
    form = StudentForm(request.POST)     
    if form.is_valid():
        s_name = form.cleaned_data['name']
        s_roll = form.cleaned_data['roll']
        s_year = form.cleaned_data['year']
        s_dob = form.cleaned_data['dob']
        s_degree = form.cleaned_data['degree']        
        s_branch = form.cleaned_data['branch']
        print(s_name,s_roll,s_year,s_dob,s_degree,s_branch)

        p=Program.objects.get(title='s_degree',branch='s_branch')
        if p is None:
           s=Student(program=np,roll_number=s_roll,name=s_name,year=s_year,dob=s_dob)
           s.save()
        else:
           np=Program(title=s_degree,branch=s_branch)
           np.save()
           s=Student(program=np,roll_number=s_roll,name=s_name,year=s_year,dob=s_dob)
           s.save()


    return HttpResponseRedirect('/student/')
  else: 
      form =StudentForm()
      return render(request, 'StudentForm.html', {'form': form})