from django.http import HttpResponse
from django.shortcuts import render
from main import mailjet


CSEMailadd = "anjalishahjhau12345@gmail.com"

# Create your views here.
def landingPage(request):
    return render(request,'index.html')
def courses(request):
    return render(request,'courses.html')
def about(request):
    return render(request,'about.html')
def admissionForm(request):
    return render(request,'form.html')
def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
         
        messageBody = f'''

            Some one trying  Contact u 
            Name : {fname} {lname}
            Email : {email}
            subject : {subject}
            Message : {message}
        '''
        print(messageBody)
        cursor = mailjet.sendMail(CSEMailadd,'CSE Contact form','Someone trying to contact ',  messageBody)

        return HttpResponse(f"{cursor}")
    else:
        return render(request,'contact.html')


def plans(request):
    return HttpResponse("planspage")
def patners(request):
    return HttpResponse("patnerspage")
  

def mailtest(self):
    cursor = mailjet.sendMail(CSEMailadd,'Got a mail','mera naam joker','Hello bro these is mailjet')

    return HttpResponse(f"{cursor}")
