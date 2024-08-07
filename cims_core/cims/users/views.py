from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# flash messages
from django.contrib import messages
# user database
from django.contrib.auth.models import User
from .models import Diagnosis, Appointment, Medicine, Patient
# authenticate
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def index(request):
    return render(request, 'users/user_login.html')

def home(request):
    patient = Patient.objects.all().count()
    diagnosis = Diagnosis.objects.all().count()
    medicine  = Medicine.objects.all().count()
    appointments = Appointment.objects.all().count()
    return render(request, 'users/index.html',{'patient':patient,'diagnosis':diagnosis,'medicine':medicine,'appointments':appointments})

#loging
def login(request):
    return render(request, 'users/user_login.html')

def login_user(request):
    user_name = request.POST['username']
    user_password = request.POST['password']
    if User.objects.filter(username = user_name).first():
        print("This username exists")
        user = authenticate(request, username=user_name, password=user_password)
        if user is not None:
            # login
            auth_login(request,user)
            messages.success(request, 'Login Success')
            #redirect
            return redirect('/home')
        else:
            # No authenticated the credentials
            messages.error(request, 'Wrong Username or Password.')
            return render(request, 'users/user_login.html')
    else:
        messages.success(request, 'Account created.')
        return render(request, 'users/user_login.html')

@login_required
def logout_user(request):
    auth_logout(request)
    messages.success(request, 'You have logged out. Bye!')
    return redirect('/login')

def create_user(request):
    user_name = request.POST['username']
    user_password = request.POST['password']
    user_email = request.POST['email']
    if User.objects.filter(username = user_name).first():
        messages.info(request, 'Account already exists')
        return render(request, 'users/user_create.html')
    else:
        messages.success(request, 'Account created.')
        user = User.objects.create_user(user_name, user_email, user_password)
        # Redirect to a success page.
        return render(request, 'users/user_login.html')

def create_user_page(request):
    # Redirect to a success page.
    return render(request, 'users/user_create.html')



def services(request):
    return render(request, 'users/services.html')

def team(request):
    return render(request, 'users/team.html')

def appointments(request):
    appointment_data = Appointment.objects.all().count()
    data = {'appointment_data':appointment_data,}
    return render(request, 'users/appointments.html',data)

def make_appointment(request):
    if request.POST:
        user_name = request.POST['name']
        doctor = request.POST['doctor']
        time = request.POST['time']
        if Appointment.objects.filter(patient_name = user_name).first():
            messages.info(request, 'Patient  appointmentalready exists')
            return redirect('/diagnosis')
        else:
            messages.success(request, 'Appointment created.')
            user = Appointment.objects.create(patient_name =user_name,doctor=doctor,time=time)
            # Redirect to a success page.
            return redirect('/appointment')
    else:
        return render('/appointment')



def diagnosis(request):
    diagnosis_data = Diagnosis.objects.all()
    data_count = Diagnosis.objects.all().count()
    return render(request, 'users/diagnosis.html',{'diagnosis_data':diagnosis_data,'data_count':data_count} )

def diagnize(request):
    if request.POST:
        name = request.POST['Patient_Name']
        user_test = request.POST['test']
        diagnose = request.POST['diagnosis']
        if Diagnosis.objects.filter(patient_name = name).first():
            messages.info(request, 'Patient already diagnized')
            return redirect('/diagnosis')
        else:
            messages.success(request, 'Patient record created.')
            user = Diagnosis.objects.create(patient_name =name,test_name=user_test,diagnosis=diagnose)
            # Redirect to a success page.
            return redirect('/diagnosis')
    else:
        return render('/diagnosis')

def treatment(request):
    med_data = Medicine.objects.all()
    number = med_data.count()
    return render(request, 'users/pharmacy.html', {'number':number,'med_data':med_data})

def prescribe(request):
    if request.POST:
        user_name = request.POST['Patient_Name']
        meds = request.POST['medicine']
        drug_stock = request.POST['stock']
        if Medicine.objects.filter(prescribed_to = user_name).first():
            messages.info(request, 'Prescription record already exists')
            return redirect('/treatment')
        else:
            messages.success(request, 'Prescription record created.')
            prescribed = Medicine.objects.create(prescribed_to=user_name,drug_name=meds,stock=drug_stock)
            drug_data = Medicine.objects.all()
            # Redirect to a success page.
            return redirect('/treatment')
    else:
        return render('/treatment')

def add_patient(request):
    if request.POST:
        user_name = request.POST['Patient_Name']
        ailment = request.POST['ailment']
        diagnosis = request.POST['diagnosis']
        if Patient.objects.filter(full_name = user_name).first():
            messages.info(request, 'Patient record already exists')
            return redirect('/patients')
        else:
            messages.success(request, 'Patient record created.')
            user = Patient.objects.create(full_name =user_name,diagnosis=diagnosis,symptoms=ailment)
            p_data = Patient.objects.all()
            # Redirect to a success page.
            return redirect('/patients')
    else:
        return redirect('/patients')

def patient(request):
    p_data = Patient.objects.all()
    p_number = p_data.count()
    # Redirect to a success page.
    return render(request, 'users/patients.html',{'p_data':p_data,'p_number':p_number})


def delete_patient(request):
    p_name = request.POST['Patient_Name']
    patient = Patient.objects.get(full_name=p_name)
    patient.delete()
    messages.success(request, 'Patient record deleted.')
    return redirect('/patients')

def update_patient(request):
    user_name = request.POST['Patient_Name']
    p_id = request.POST['Patient_ID']
    ailment = request.POST['ailment']
    diagnosis = request.POST['diagnosis']
    user = Patient.objects.get(id=p_id)
    user.full_name = user_name
    user.diagnosis=diagnosis
    user.symptoms=ailment
    user.save()
    messages.success(request, 'Patient record updated.')
    return redirect('/patients')


