from django.shortcuts import render, redirect
from .models import Employee

# Show employee list
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})


# Add employee
def add_employee(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        department = request.POST.get("department")
        salary = request.POST.get("salary")
        joining_date = request.POST.get("joining_date")

        Employee.objects.create(
            name=name,
            email=email,
            department=department,
            salary=salary,
            joining_date=joining_date
        )

        return redirect('/')

    return render(request, 'employee/add_employee.html')

#edit employee
def edit_employee(request, id):
    emp = Employee.objects.get(id=id)

    if request.method == "POST":
        emp.name = request.POST.get("name")
        emp.email = request.POST.get("email")
        emp.department = request.POST.get("department")
        emp.salary = request.POST.get("salary")
        emp.joining_date = request.POST.get("joining_date")

        emp.save()
        return redirect('/')

    return render(request, 'employee/edit_employee.html', {'emp': emp})

#delete employee
def delete_employee(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/')

#search logic
def employee_list(request):

    search = request.GET.get('search')

    if search:
        employees = Employee.objects.filter(name__icontains=search)
    else:
        employees = Employee.objects.all()

    return render(request,'employee/employee_list.html',{'employees':employees})