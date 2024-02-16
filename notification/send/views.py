from django.shortcuts import render, redirect
from .models import UserSubmission, AnimalReport, UploadFile
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings
from . import machine
import re




def send_mail_to_admin(user_name, report):
    
    message_body = f'Form filled by {user_name}--- and the description provided was {report.description}'
    message = EmailMessage(
        subject='New Animal Report Submitted',
        body=message_body,
        from_email=settings.EMAIL_HOST_USER,
        to=['syedzubair4unib@gmail.com','rugvedkulk2003@gmail.com','koustavbiswas04@gmail.com','kishlaysharma80@gmail.com']
    )
    message.send()


def user_page(request):
    send = 0
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        submission_data = request.POST.get('submission_data')
        submission = UserSubmission.objects.create(user_name=user_name, submission_data=submission_data)
        submission.save()

        try:
            send_mail_to_admin(user_name, submission_data)
            send = 1  
        except Exception as e:
            print(e)  

    return render(request, 'user_page.html', {'send': send})


def admin_page(request):
    animal_reports = AnimalReport.objects.all()
    
    return render(request, 'admin.html', {'animal_reports': animal_reports})

def land(request):

    
    return render(request, 'LandingPage.html',{
        'offerBanner1': '/static/LandingImages/offerBanner1.jpg',
        'offerBanner2':'/static/LandingImages/offerBanner2.jpg',
        'offerBanner3':'/static/LandingImages/offerBanner3.jpg',
        'ctaBg':'/static/LandingImages/ctaBg.jpg',
        'footerBg':'/static/LandingImages/footerBg.jpg',
        'heroBanner':'/static/LandingImages/heroBanner.jpg'

    })

def landing(request):
    return render(request, 'LandingPage.html',{
        'offerBanner1': '/static/LandingImages/offerBanner1.jpg',
        'offerBanner2':'/static/LandingImages/offerBanner2.jpg',
        'offerBanner3':'/static/LandingImages/offerBanner3.jpg',
        'ctaBg':'/static/LandingImages/ctaBg.jpg',
        'footerBg':'/static/LandingImages/footerBg.jpg',
        'heroBanner':'/static/LandingImages/heroBanner.jpg'

    })



def redirectToUser(request):
    return render(request, 'user_page.html')

def redirectToLogin(request):
    return render(request, 'LoginPage.html')

def redirectToAdmin(request):
    submissions = UserSubmission.objects.all()



def Login(request):
    if request.method == 'POST':
        usn = request.POST['username']
        passw = request.POST['password']

        User = auth.authenticate(username=usn, password=passw)
        if User is not None:
            auth.login(request, User)
            
            
            return render(request,'LandingPage.html',{
                'username':usn,
                'offerBanner1': '/static/LandingImages/offerBanner1.jpg',
                'offerBanner2':'/static/LandingImages/offerBanner2.jpg',
                'offerBanner3':'/static/LandingImages/offerBanner3.jpg',
                'ctaBg':'/static/LandingImages/ctaBg.jpg',
                'footerBg':'/static/LandingImages/footerBg.jpg',
                'heroBanner':'/static/LandingImages/heroBanner.jpg'

            })
        else:
            messages.error(request, 'Invalid Credentials. Please check.')
    
    return render(request, 'LoginPage.html',{
                'username':usn,
                'offerBanner1': '/static/LandingImages/offerBanner1.jpg',
                'offerBanner2':'/static/LandingImages/offerBanner2.jpg',
                'offerBanner3':'/static/LandingImages/offerBanner3.jpg',
                'ctaBg':'/static/LandingImages/ctaBg.jpg',
                'footerBg':'/static/LandingImages/footerBg.jpg',
                'heroBanner':'/static/LandingImages/heroBanner.jpg'

            })


def Register(request):
    
    if request.method == 'POST':
        usn = request.POST['username']
        email = request.POST['email']
        passw = request.POST['password']

        if not re.match(r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email): 
            messages.error(request, 'Invalid Credentials. Please check.')
            


       # Check if a user with the same username already exists
        if User.objects.filter(username=usn).exists():
            messages.error(request, 'Account already exists. Please login to your account.')
            return render(request, 'LoginPage.html')

        # If the user doesn't exist, create a new user
        user = User.objects.create_user(username=usn, password=passw, email=email)
        
        return render(request, 'LandingPage.html', {
                'username':usn,
                'offerBanner1': '/static/LandingImages/offerBanner1.jpg',
                'offerBanner2':'/static/LandingImages/offerBanner2.jpg',
                'offerBanner3':'/static/LandingImages/offerBanner3.jpg',
                'ctaBg':'/static/LandingImages/ctaBg.jpg',
                'footerBg':'/static/LandingImages/footerBg.jpg',
                'heroBanner':'/static/LandingImages/heroBanner.jpg'

            })
   
    # If the request method is not POST, render the registration page
    return render(request, 'LoginPage.html'),messages('Wrong Credentials')




#Ngo form page redirecting

def NgoLink(request):
    return render(request, 'NGO-Form.html')

#Ngo form handling
def SubmitNgoForm(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        photo = request.FILES.get('photo')
        location = request.POST.get('location', None)
        description = request.POST.get('description')
        animal_type = request.POST.get('animal_type')
        priority_type = request.POST.get('priority')

        # Save the data to the database
        report = AnimalReport.objects.create(
            user_name=user_name,
            phone_number=phone_number,
            photo=photo,
            location=location,
            description=description,
            animal_type=animal_type,
            priority_type=priority_type
        )
        report.save()

        send_mail_to_admin(user_name,report)


        
        return render(request, 'AfterLandingPage.html', {
                'offerBanner1': '/static/LandingImages/offerBanner1.jpg',
                'offerBanner2':'/static/LandingImages/offerBanner2.jpg',
                'offerBanner3':'/static/LandingImages/offerBanner3.jpg',
                'ctaBg':'/static/LandingImages/ctaBg.jpg',
                'footerBg':'/static/LandingImages/footerBg.jpg',
                'heroBanner':'/static/LandingImages/heroBanner.jpg' 
                })
    
    return render(request, 'NGO-Form.html')


#loading Ecommerce

def LoadEcommerce(request):
    return render(request, 'EcommercePage.html',{
        'pedigreeImage':'/static/EcommerceImages/pedigree.jpg',
        'P1image':'/static/EcommerceImages/p1.jpeg',
        'P2image':'/static/EcommerceImages/p2.jpeg',
        'P3image':'/static/EcommerceImages/p3.jpeg',
        'P4image':'/static/EcommerceImages/p4.jpeg',
        'Dog1Image':'/static/EcommerceImages/dog1.png',
        'KibblesNbits':'/static/EcommerceImages/kibblesnBits.jpeg',
        'Cat1Image':'/static/EcommerceImages/cat1.jpeg',
        'Cat2Image':'/static/EcommerceImages/cat2.jpeg',
        'Cat5Image':'/static/EcommerceImages/cat3.jpeg',
        'PetOffer':'/static/EcommerceImages/petOffer.png',
        'PetOffer1':'/static/EcommerceImages/petOffer1.png'
        
    })


#form of machine learning handling
def MachineLearn(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            new_file = UploadFile(file=uploaded_file)
            new_file.save()
            # Full path of the uploaded file
            full_file_path = new_file.file.path
            predictedValue = machine.predict_emotion(full_file_path)
            show_message=True

            # Here you can perform any additional processing with the uploaded file
            return render(request, 'ml_model.html',{'show_message':show_message,'answer':predictedValue})  # Redirect to a success page
    return render(request, 'ml_model.html')


    
#redirecting to Machine learning page
def redirectToMl(request):
    train_dir = 'D:/DjangoProjects/Emotions'
    machine.train_model(train_dir)

    return render(request,'ml_model.html')


def redirectToServices(request):
    return render(request, 'Services.html')



