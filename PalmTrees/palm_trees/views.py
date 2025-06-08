from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import Product
from palm_trees.models import Register
from .utils import generate_token, verify_token
import json
from json import load,dump
try:
    with open("./users.db", "r") as db:
        users = load(db)
except Exception:
    with open("./users.db","w") as db:
        users = {}
def send_verification(email, request):
    token = generate_token(email)
    link = request.build_absolute_uri(f'/verify/{token}/')

    subject = "Verify Your Email – PALM TREES OIL & AGRO"
    from_email = settings.EMAIL_HOST_USER  # you can use a domain noreply email
    to_email = [email]

    # Context for HTML template
    context = {
        'verification_link': link,
        'company_name': "PALM TREES OIL & AGRO",
        'advert_text': "Welcome to Palm Trees – Get the purest palm oil direct from the source!",
    }

    # Load HTML and plain text content
    html_content = render_to_string('verify_email.html', context)
    text_content = f"Hi,\nClick the link to verify your email: {link}"

    msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return HttpResponse("Verification email sent.")
# # ✅ Token-based email verification
# def send_verification(email, request):
#     token = generate_token(email)
#     link = request.build_absolute_uri(f'/verify/{token}/')

#     send_mail(
#         subject='Verify your email',
#         message=f'Click this link to verify your email: {link}',
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[email],
#     )
#     return HttpResponse("Verification email sent.")


# ✅ Handle email verification
def verify_email(request, token):
    email = verify_token(token)
    if email:
        try:
            user = Register.objects.get(email=email)
            user.verified = True  # Add this field to your model if not already
            user.save()
            return HttpResponse(f"Email {email} verified successfully!")
        except Register.DoesNotExist:
            return HttpResponse("User not found.")
    return HttpResponse("Invalid or expired verification link.")


# ✅ Check if email already exists
def check(email):
    return Register.objects.filter(email=email).exists()


# ✅ Home page
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'product': products})


# ✅ Register new user
def register(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        full_name = data.get('fullName')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirmPassword')

        # if check(email):
        #     return JsonResponse({"success":False,"email": "User already exists"})

        if password != confirm_password:
            return JsonResponse({"success":False,"confirmPassword": "Password mismatch!"})


        user = Register(fullName=full_name, email=email, password=password, verified=False)
        user.save()
        
        send_verification(email, request)
        return JsonResponse({"success":True,"message": "Registration successful! Check your email to verify."})

        # Save user to database (initially unverified)

    return render(request, 'signup.html')


# ✅ Login page (dummy call to test email)
def login(request):
    return render(request, 'signin.html')
