from django.shortcuts import render
from testapp.models import student

# Create your views here.
def student_view(request):
    s_list=student.objects.order_by('marks')
    my_dict={'s_list':s_list}
    return render(request,'testapp/results.html',context=my_dict)
