from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from sqlparse.sql import Case

from .models import *

# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#
#         if password == confirm_password:
#             # Create a new user
#             user = User.objects.create_user(username=username, password=password)
#             # You can add additional user-related fields here
#             # user.profile.role = 'UserType'
#             # user.profile.save()
#
#             # Log the user in
#             login(request, user)
#             return redirect('login')  # Redirect to the home page after registration
#         else:
#             # Passwords don't match; handle the error accordingly
#             return render(request, 'register.html', {'error': 'Passwords do not match'})
#
#     return render(request, 'register.html')
#
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')  # Redirect to the home page after login
#         else:
#             # Authentication failed; handle the error accordingly
#             return render(request, 'login.html', {'error': 'Invalid username or password'})
#
#     return render(request, 'login.html')

def index(request):
    case = PrevCases.objects.all()
    dict = {
        'case': case
    }
    return render(request, 'index.html', dict)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'Services.html')

def contact(request):
    return render(request, 'contact.html')

"""
def case(request):
    # uid = request.session['log_id']
    FetchCase = CaseDetails.objects.get(C_Id=id)
    c_id = FetchCase.CASEID
    c_type = FetchCase.CASETYPE
    FetchCases = CaseDetails.objects.values('caseid').filter(CASEID__lte=c_id, streamid=c_type)
    casedata = CaseDetails.objects.filter(id__in=FetchCases).values()
    return render(request, 'casedetails.html', {'casedata': casedata})

def suspectdetails(request):
    if request.method == "POST":
        CASEID = request.POST.get("CASEID")
        
        FetchCase = CaseDetails.objects.filter(C_Id=id).first()
        
        if FetchCase is not None:
            FetchCase.CASEID = CASEID
            FetchCase.save()
        else:
            query = CaseDetails(CASEID=CASEID)
            query.save()
            
        return redirect(case)
    else:
        return redirect(case)
"""
