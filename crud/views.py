from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
def index(request):
    if request.method == 'POST':
        employee_name = request.POST.get('employeeName')
        employee_id = request.POST.get('employeeId')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone_number = request.POST.get('phoneNumber')

        # Create and save the Employee object
        Employee.objects.create(
            employeeName=employee_name,
            employeeId=employee_id,
            email=email,
            address=address,
            phoneNumber=phone_number
        )

        return redirect('index')  # Redirect to a success page or any other page

  
    return render(request,'index.html')

def employee(request):
    # Retrieve all employee objects from the database
    employees = Employee.objects.all()
    
    # Pass the employee data to the template
    context = {'employees': employees}
    
    return render(request, 'views.html', context)


def update_employee_view(request, employee_id):
    # Retrieve the employee object using the employee_id
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        # Update all fields
        employee.employeeName = request.POST.get('employeeName')
        employee.email = request.POST.get('email')
        employee.employeeId = request.POST.get('employeeId')
        employee.address = request.POST.get('address')
        employee.phoneNumber = request.POST.get('phoneNumber')

        # Save the changes
        employee.save()

        # Redirect to the employee page or any other page
        return redirect('employee')

    return render(request, 'update_employee.html', {'employee': employee})





