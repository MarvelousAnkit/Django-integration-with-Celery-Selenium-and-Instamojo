from django.shortcuts import render,HttpResponse,redirect
from .models import data
import nexmo
from nexmo import Client
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
from selenium.webdriver.common.keys import Keys
from instamojo_wrapper import Instamojo





from selenium import webdriver
import time


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from .apps import PrintfConfig,browser
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.by import By
from .tasks import test,done






from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Snippet
api = Instamojo(api_key="test_3848b0c0aa36cf0194b5e994374", auth_token="test_5785a0456d445e982e9567d42a4" , endpoint='https://test.instamojo.com/api/1.1/' )

def about(request):
    return HttpResponse('about page')
def snippet_detail(request, slug):
    snippet = get_object_or_404(Snippet, slug=slug)
    return HttpResponse(f'the detailview for slug of {slug}')

# Create your views here.
@csrf_exempt
def home(request):
    
    
    

    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    

    
    if request.method == "POST":
       
        fdocs = request.FILES['file']
        filename = fdocs.name
        
        global fname;    
        fname = request.POST.get('name')
        fphone = request.POST.get('phone')
        fcopy = int(request.POST.get('copy'))
        flimit = int(request.POST.get('limit'))
        fadd = request.POST.get('add')
        fmode = int(request.POST.get('mode'))
        total = int(fcopy*flimit*fmode)*100
        total1 = int(fcopy*flimit*fmode + 10)
        global details;
        details = f'Full Name: {fname} ------  phone : {fphone}  ------- No of Copy : {fcopy} ------ Print Till Page No : {flimit} ------- address : {fadd} ----- Mode : {fmode} ---- Total Money : {total1}'

        

        # document = data.objects.create(Files1=fdocs)
        # document.save()
        
        # client = Client(key='d98caeeb', secret='Lt8nkZAlllpia7tJ') not needed
        # rAZORPAY WORL START
        # client  = razorpay.Client(auth=("rzp_test_XLgbcJqxxm1chb","enVUzcMaE2VbsaBFsNGCSQxs"))
        # payment = client.order.create({'amount':total, 'currency' :'INR' , 'payment_capture' :'1'}) 
        # print(payment)
        # RAZOURPAY WORK END


        response = api.payment_request_create(
                    amount=total1,
                    buyer_name = fname,
                    purpose='Printing',
                    send_email=True,
                    email='blog.ankitsinghD@gmail.com',
                    phone=fphone ,
                    redirect_url="https://printf.in/success/"

                    )
        print(response)



        # coffee = data()
        # coffee.save()
        coffee = data(Name=fname, Phone=fphone, Copies=fcopy, Page_Limit=flimit, Address=fadd, delivery=fmode,Files1=fdocs,Payment_id =response['payment_request']['id'])
        coffee.save()
        global file_path;
        file_path = os.path.join(settings.MEDIA_ROOT, filename)
        print(file_path,filename)
        with open(file_path, 'wb+') as destination:
            for chunk in fdocs.chunks():
                destination.write(chunk)
        test.delay(file_path,details)
        


        return render(request , "pay.html" , {'payment_url': response['payment_request']['longurl'] , 'name' : fname, 'phone' : fphone ,'total': total1,})
    return render (request, 'index.html')
@csrf_exempt
def text(request):
    if request.method=="POST":
        texts = request.POST.get('texta')
        return redirect(f'https://apis.xditya.me/write?text={texts}')

def success(request):
    print("hiijscjdjcjdnvcdfjv dfjkmc sdxck dsvn hfdv fdjnvijdsncisjdvnijfdvnidfj")
    try:
        
            # a=request.POST
            # order_id = ""
            # for key,val in a.items():
            #     if key == "razorpay_order_id":
            #         order_id=val
            #         break
        payment_request_id = request.GET.get('payment_request_id')
        # data1 = data.objects.get(Payment_id = payment_request_id)

        # data1.Paid = True   
    
        print("hiiiiiii")
        # data1.save()
        print("1")
        user = data.objects.filter(Payment_id=payment_request_id).first()
        # print("2")
        user.Paid= True
        user.save()
        print(fname)
        global message1;
        message1 = f'The payment of {fname} Has been Recieved Successfully.'
        done.delay(message1)
        
        
        print("3")
    except Exception as e:
        print(e)
    return render (request , "success.html")
    
            

                                       
                                      
        
    

        
        



        


 
def terms(request):
    return render (request,'pp.html')       
def privacy(request):
    return render (request,'tc.html')       
def disc(request):
    return render (request,'disc.html')       
def cancel(request):
    return render (request,'cr.html')       
def shipping(request):
    return render (request,'sp.html')       
def contact(request):
    return render (request,'contact.html')       
def facebook(request):
    return redirect("https://www.facebook.com/profile.php?id=100090358433386")   
def twitter(request):
    return redirect("https://twitter.com/connect_printf")  
def linkedin(request):
    return redirect("https://www.linkedin.com/in/print-f-792a9525a/") 
def instagram(request):
    return redirect("https://www.instagram.com/connect_printf/")
def riya(request):
    return redirect("https://www.instagram.com/_.rhea_22._/")
def anuska(request):
    return redirect("https://www.instagram.com/anushkaa_singh14/")
def kunal(request):
    return redirect("https://www.instagram.com/kunalbhardwaj81/")
def priyanshu(request):
    return redirect("https://www.instagram.com/priyanshu_pratap_siingh/")


