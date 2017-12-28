from django.shortcuts import render
from .models import Students_info
# Create your views here.
def index(request):
    Students_info_list=Students_info.objects.all().order_by("total_score")
    dict_student_info={}
    for i in range(len(Students_info_list)):
        dict_student_info[i+1]=(Students_info_list[i])
    print("length=%d" % len(Students_info_list))
    print(dict_student_info)
    return render(request,'score.html',context={'list_stu':dict_student_info})