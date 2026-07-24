# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Employee
def employee_list(request):
    search = request.GET.get('search', '')

    employees = Employee.objects.all()

    if search:
        employees = employees.filter(
            Q(emp_name__icontains=search) |
            Q(email__icontains=search) |
            Q(mobile_no__icontains=search)
        )

    return render(request, 'employee_list.html', {
        'employees': employees,
        'search': search,
    })



def add_employee(request):
    if request.method == "POST":
        employee = Employee(

            emp_name=request.POST['emp_name'],
            gender=request.POST['gender'],
            mobile_no=request.POST['mobile_no'],
            alternate_mobile_no=request.POST['alternate_mobile_no'],
            email=request.POST['email'],
            religion=request.POST['religion'],
            nationality=request.POST['nationality'],
            community=request.POST['community'],
            blood_group=request.POST['blood_group'],
            dob=request.POST['dob'],

            p_door_no=request.POST['p_door_no'],
            p_street=request.POST['p_street'],
            p_town=request.POST['p_town'],
            p_district=request.POST['p_district'],
            p_state=request.POST['p_state'],
            p_country=request.POST['p_country'],

            t_door_no=request.POST['t_door_no'],
            t_street=request.POST['t_street'],
            t_town=request.POST['t_town'],
            t_district=request.POST['t_district'],
            t_state=request.POST['t_state'],
            t_country=request.POST['t_country'],

            marital_status=request.POST['marital_status'],
            spouse_name=request.POST['spouse_name'],

            employee_type=request.POST['employee_type'],
            employee_shift=request.POST['employee_shift'],

            password=request.POST['password']
        )

        employee.save()

        return redirect('employee_list')

    return render(request, 'employee_form.html')

def edit_employee(request, id):

    employee = get_object_or_404(Employee, emp_id=id)


    if request.method == "POST":

        employee.emp_name = request.POST['emp_name']
        employee.mobile_no = request.POST['mobile_no']
        employee.email = request.POST['email']
        employee.employee_type = request.POST['employee_type']
        employee.employee_shift = request.POST['employee_shift']


        employee.save()

        return redirect('employee_list')


    return render(
        request,
        'employee_edit.html',
        {
            'employee': employee
        }
    )
def view_employee(request, id):

    employee = get_object_or_404(Employee, emp_id=id)

    return render(
        request,
        'employee_view.html',
        {
            'employee': employee
        }
    )
def delete_employee(request, id):

    employee = get_object_or_404(Employee, emp_id=id)

    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')

    return render(
        request,
        'employee_delete.html',
        {
            'employee': employee
        }
    )
