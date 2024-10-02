from django.shortcuts import render


def renderTemplate(request):
    myDict={"name":"Arnada Kaewprapan"}
    return render(request, 'templatesApp/firstTemplate.html',context=myDict)


def renderEmployee(request):
    myDict={"id":6604101401,"name":"Arnada Kaewprapan","sal":50000}
    return render(request, 'templatesApp/employeeTemplate.html',context=myDict)