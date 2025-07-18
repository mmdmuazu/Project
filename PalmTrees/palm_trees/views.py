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
from django.templatetags.static import static
try:
    with open("./users.json", "r") as db:
        users = load(db)
except Exception:
    with open("./users.json","w") as db:
        users = {}

print(users)
def send_verification(email, request):
    token = generate_token(email)
    link = request.build_absolute_uri(f'/verify/{token}/')

    image_url = request.build_absolute_uri(static('images/palm.png'))
    print(image_url)

    subject = "Verify Your Email – PALM TREES OIL & AGRO"
    from_email = settings.EMAIL_HOST_USER  
    to_email = [email]

    # Context for HTML template
    context = {
        'verification_link': link,
        'image_url': image_url,
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
    print(email,users)
    if email:
        try:
            for info in users.values():
                if info['email'] == email:
                    user = Register(fullName=info['fullName'], email=info['email'], password=info['password'], verified=True)
                    user.save()
                    del users[info['email']]
                    return HttpResponse(f"Email {email} verified successfully!")

            # user = Register.objects.get(email=email)
            # user.verified = True  # Add this field to your model if not already
            # user.save()
        except Exception:
            return HttpResponse("User not found.")
    return HttpResponse("Invalid or expired verification link.")


# ✅ Check if email already exists
def check(email):
    return Register.objects.filter(email=email).exists()


# ✅ Home page
def index(request):
    # products = Product.objects.all()
    products = [
    {
        'id': 1,
        'name': 'Palm Oil',
        'image': 'images/palm-oil.jpg',
        'price': 8000,
        'discount': 25,
    },
    {
        'id': 2,
        'name': 'Groundnut Oil',
        'image': 'images/groundnut-oil.jpg',
        'price': 7500,
        'discount': 20,
    },
    {
        'id': 3,
        'name': 'Agro Produce',
        'image': 'images/agro.jpg',
        'price': 10000,
        'discount': 15,
    },
    {
        'id': 4,
        'name': 'Produce',
        'image': 'images/agro.jpg',
        'price': 10000,
        'discount': 100,
    },
]
    return render(request, 'app.html', {'products': products})

def cart(request):
    # Dummy cart data for testing
    cart_items = [
        {
            'id': 1,
            'name': 'Palm Oil',
            'image': 'images/palm-oil.jpg',
            'price': 8000,
            'quantity': 2,
        },
        {
            'id': 2,
            'name': 'Groundnut Oil',
            'image': 'images/groundnut-oil.jpg',
            'price': 7500,
            'quantity': 1,
        },
    ]
    return render(request, 'cart.html', {'cart_items': cart_items})
# ✅ Register new user
def register(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        full_name = data.get('fullName')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirmPassword')

        if check(email):
            if email in users.values():
                del users[email]
            return JsonResponse({"success":False,"email":"email already exists"})

        if password != confirm_password:
            return JsonResponse({"success":False,"confirmPassword": "Password mismatch!"})


        users[email] = {"fullName":full_name,"email":email,"password":password}
        with open('./users.json' ,'w') as db:
            dump(users,db)
            db.close()
        send_verification(email, request)
        return JsonResponse({"success":True,"message": "Registration successful! Check your email to verify."})

        # Save user to database (initially unverified)

    return render(request, 'signup.html')


# ✅ Login page (dummy call to test email)
def login(request):
    if request.method == "POST":
        # data = json.loads(request.body.decode('utf-8'))
        data = request.body.decode("utf-8")
        # username = data('username')
        print((data))
        return JsonResponse({"good":'username'})
    return render(request, 'signin.html')

def products(request):
    return render(request,"products.html")

def get_products(request):
    products = {}
    if request.method == "GET":
        return JsonResponse({"products":"products"})
    else:
        return "post request not allowed"
