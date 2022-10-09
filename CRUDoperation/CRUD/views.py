from django.shortcuts import render, redirect
from CRUD.models import EmpModel
from django.contrib import messages
from CRUD.forms import empForms

# Create your views here.
def showEmp(request):
    showall = EmpModel.objects.all()
    return render(request, 'index.html', {'data': showall})

def insertTemp(request):
    if request.method == "POST":
        if request.POST.get('empname') and request.POST.get('email') and request.POST.get('occupation') and request.POST.get('salary') and request.POST.get('gender'):
            saverecord = EmpModel()
            saverecord.empname = request.POST.get('empname')
            saverecord.email = request.POST.get('email')
            saverecord.occupation = request.POST.get('occupation')
            saverecord.salary = request.POST.get('salary')
            saverecord.gender = request.POST.get('gender')
            saverecord.save()
            messages.success(request,'Employee ' +saverecord.empname+ 'Is saved Successfully!')
            return render(request, 'insert.html')
    else:
        return render(request, 'insert.html')

def editTemp(request, id):
    editTempObj = EmpModel.objects.get(id = id)
    return render(request, 'edit.html', {"EmpModel": editTempObj})

def updateTemp(request,id):
    updateTemp = EmpModel.objects.get(id = id)
    form = empForms(request.POST, instance = updateTemp)
    if form.is_valid():
        form.save()
        messages.success(request, "form updated successfuly")
        return render(request, 'edit.html', {"EmpModel": updateTemp})

def delTemp(request,id):
    delTemp = EmpModel.objects.get(id = id)
    delTemp.delete()
    showdata = EmpModel.objects.all()
    return redirect('/')
