from email.policy import default
import re
from django.shortcuts import render



#setting the session get, set, delete
#################################################################
# def setsession(request):
#     request.session['name'] = 'SUYOG'
#     request.session['lname'] = 'OJHA'
#     return render(request, 'student/setsession.html')

# def getsession(request):
#     # name = request.session['name'] 
#     name = request.session.get('name') 
#     lname = request.session.get('lname') 
#     return render(request, 'student/getsession.html', {'name': name, 'lname': lname})


# def delsession(request):
#     if 'name' in request.session:
#         del request.session['name']
#     return render(request, 'student/delsession.html')


#################################################################



# def setsession(request):
#     request.session['name'] = 'SUYOG'
#     request.session['lname'] = 'ojha'
#     return render(request, 'student/setsession.html')

# def getsession(request):
#     name = request.session.get('name') 
#     keys = request.session.keys()
#     items = request.session.items()
#     # age = request.session.setdefault('age', '20')
#     return render(request, 'student/getsession.html', {'name': name, 'keys': keys, 'items': items})


# def delsession(request):
#     request.session.flush()
#     return render(request, 'student/delsession.html')







########################################################################################



# def setsession(request):
#     request.session['name'] = 'SUYOG'
#     request.session.set_expiry(600)
#     return render(request, 'student/setsession.html')

# # def getsession(request):
# #     name = request.session.get('name') 
# #     return render(request, 'student/getsession.html', {'name': name})


# def getsession(request):
#     name = request.session['name'] 
#     print(request.session.get_session_cookie_age)
#     print(request.session.get_expiry_age)
#     print(request.session.get_expiry_date)
#     print(request.session.get_expire_at_browser_close)
#     return render(request, 'student/getsession.html', {'name': name})


# def delsession(request):
#     request.session.flush()
#     request.session.clear_expired()
#     return render(request, 'student/delsession.html')


########################################################################





def setsession(request):
    request.session['name'] = 'SUYOG'
    # request.session.set_expiry(600)
    return render(request, 'student/setsession.html')

# def getsession(request):
#     name = request.session.get('name') 
#     return render(request, 'student/getsession.html', {'name': name})


def getsession(request):
    name = request.session['name'] 
    return render(request, 'student/getsession.html', {'name': name})


def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')

########################################################################