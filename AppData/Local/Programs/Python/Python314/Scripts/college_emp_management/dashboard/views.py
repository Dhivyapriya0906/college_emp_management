from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from reportlab.pdfgen import canvas

import openpyxl

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")

        return render(request, "dashboard/login.html", {
            "error": "Invalid Username or Password"
        })

    return render(request, "dashboard/login.html")


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {
        "employee_count": 35,
        "present_count": 28,
        "leave_count": 3,
        "department_count": 5,
    }

    return render(request, "dashboard/dashboard.html", context)


def reports(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, "dashboard/reports.html")


def logout_view(request):
    logout(request)
    return redirect("login")
def download_pdf(request):

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename="Employee_Report.pdf"'

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold",18)
    p.drawString(180,800,"College Employee Management")

    p.setFont("Helvetica",14)

    p.drawString(50,760,"Reports Summary")

    p.drawString(50,720,"Total Employees : 35")

    p.drawString(50,690,"Present Today : 28")

    p.drawString(50,660,"Leave Today : 3")

    p.drawString(50,630,"Departments : 5")

    p.drawString(50,600,"Attendance Percentage : 92%")

    p.save()

    return response

def download_excel(request):

    workbook = openpyxl.Workbook()

    sheet = workbook.active

    sheet.title = "Employee Report"

    sheet.append(["Category","Value"])

    sheet.append(["Total Employees",35])

    sheet.append(["Present",28])

    sheet.append(["Leave",3])

    sheet.append(["Departments",5])

    sheet.append(["Attendance %","92%"])

    response = HttpResponse(

        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

    response["Content-Disposition"] = 'attachment; filename=Employee_Report.xlsx'

    workbook.save(response)

    return response