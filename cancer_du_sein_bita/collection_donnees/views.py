
#import file
#-------------------------------------------------------------------------------
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth import login,authenticate,get_user
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

from django.shortcuts import render, redirect

from django.template.loader import render_to_string
from collection_donnees.models import *
from django.http import HttpResponse
from collection_donnees.forms import *

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from .tokens import account_activation_token
# ---------------------------------------------------------------------------------------------------------------


#first page ---------------------

def first_page(request):
    # login function

    if request.method == 'POST':
        form1= AuthenticationForm(data=request.POST)
        if form1.is_valid():
            user = form1.get_user()
            login(request, user)
            return redirect('profile',user.id)

        # signup function

        form = signupForm(request.POST or None)
        form2 = DoctorFrom(request.POST or None)
        if form.is_valid() and form2.is_valid():
            user2 = form.save()
            doctor = form2.save()
            #user2.is_staff = True
            user2.is_active = False

            user2.save()
            Doctor.objects.filter(pk=doctor.pk).update(user=user2)

            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user': user2,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user2.pk)),
                'token': account_activation_token.make_token(user2),
            })
            mail_subject = 'Activate your blog account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request,'confirmation_email.html')


    else:
        form1= AuthenticationForm(request.POST or None)
        form = signupForm(request.POST or None)
        form2 = DoctorFrom(request.POST or None)

    return render(request,'aidecan/index.html',locals())




#Email validation

def activate(request, uidb64, token,id):
    try:

        user = User.objects.get(pk=id)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None


    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.is_staff=True
        user.save()
        login(request, user)
        return redirect('profile', user.id)


    else:
        return HttpResponse('Activation link is invalid!')




#random lable view
@login_required()
def valid(request,id):

    user_id = id
    docs= Doctor.objects.filter(user_id=user_id)
    print(docs)
    doc = Doctor()
    for i in docs :
        doc=i
    mammo_id = request.POST.get('id_mamo',None)
    rate = request.POST.get('rate',None)
    comment = request.POST.get('comment',None)

    Diagnostic.objects.create(mammography_id=mammo_id,user_id=doc.id,rate=rate,comment=comment,date=timezone.now())
    data={
        'yes':'yes'
    }
    return JsonResponse(data)


@login_required()
def label_view(request,id):
    if request.user.id == id:
        id=id
        docs = Doctor.objects.filter(user_id=id)
        doc = Doctor()
        for i in docs:
            doc = i
        list=doc.get_teen_mammographys()
        return render(request, 'aidecan/random_labling.html', locals())
    else:
        return redirect(Error)

#add mammography view

@login_required()
def add_mammo_and_label_view(request,id):
    if request.user.id == id:
        # TODO::
        id=id
        return render(request, 'aidecan/add_label.html',locals())

    else:
        return redirect(Error)


#details label view

@login_required()
def show_label(request,id):
    if request.user.id == id:
        # TODO::

        return render(request, 'aidecan/show_label.html')

    else:
        return redirect(Error)
#profile view

@login_required()
def profile_view(request,id):
    if request.user.id == id:
        id=id
        docs=Doctor.objects.filter(user_id=id)
        doc=Doctor()
        for i in docs:
            doc=i

        if request.method=="POST" :
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            speciality = request.POST['speciality']
            establishment = request.POST['establishment']


            if request.FILES.get('img') is None:
                doc.specialty = speciality
                doc.establishment = establishment
            else:
                doc.specialty = speciality
                doc.establishment = establishment
                doc.photo = request.FILES.get("img")
            User.objects.filter(pk=id).update(first_name=first_name, last_name=last_name, email=email)
            doc.save()

        return render(request, 'aidecan/profile.html',locals())

    else:
        return redirect(Error)


@login_required()
def change_password(request,id):

    if request.user.id == id:
        #TODO::

        return render(request,'aidecan/change_password.html',locals())
    else:
        return redirect(Error)



#Error View
def Error(requeqt):
    return render(requeqt,'aidecan/NotLogedIn.html')