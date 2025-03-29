from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AdminLogin
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AdminLogin

def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if an admin with the given email and password exists
        if AdminLogin.objects.filter(email=email, password=password).exists():
            return redirect('admin_index')  # Redirect to admin index if login is successful
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "admin_login.html")  # Always show the login page

def admin_index(request):
    return render(request, "admin_index.html")

def admin_logout(request):
    messages.success(request, "Logged out successfully.")
    return redirect('admin_login')


from django.shortcuts import render, redirect
from .models import Category
from django.contrib import messages

def add_category(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description", "")

        if not name:
            messages.error(request, "Category name is required.")
        else:
            Category.objects.create(name=name, description=description)
            messages.success(request, "Category added successfully!")
            return redirect("add_category")  # Change as needed

    return render(request, "add_category.html")



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, "category_list.html", {"categories": categories})

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description", "")

        if not name:
            messages.error(request, "Category name is required.")
        else:
            category.name = name
            category.description = description
            category.save()
            messages.success(request, "Category updated successfully!")
            return redirect("category_list")

    return render(request, "edit_category.html", {"category": category})

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    messages.success(request, "Category deleted successfully!")
    return redirect("category_list")




from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.core.exceptions import ValidationError

from django.shortcuts import render, redirect, get_object_or_404
from .models import Officer, Category

def add_officer(request):
    if request.method == 'POST':
        fullname = request.POST['Fullname']
        email = request.POST['Email']
        password = request.POST['Password']
        phone = request.POST['Phone']
        gender = request.POST['Gender']
        category_id = request.POST['category']
        officer_id = request.POST['officer_id']
        id_card = request.FILES.get('id_card')
        profile = request.FILES.get('profile')

        category = get_object_or_404(Category, id=category_id)  # Fetch Category

        new_officer = Officer(
            Fullname=fullname,
            Email=email,
            Password=password,
            Phone=phone,
            Gender=gender,
            category=category,  # Assign ForeignKey
            officer_id=officer_id,
            id_card=id_card,
            profile=profile
        )

        new_officer.save()
        return redirect('list_officers')

    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'add_officer.html', {'categories': categories})




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from adminapp.models import Officer

# List Officers View
def list_officers(request):
    officers = Officer.objects.all()
    return render(request, 'list_officers.html', {'officers': officers})

# Edit Officer Password
def edit_officer(request, officer_id):
    officer_instance = get_object_or_404(Officer, id=officer_id)
    
    if request.method == 'POST':
        # Only updating the password
        new_password = request.POST.get('password')
        if new_password:
            officer_instance.Password = new_password
            officer_instance.save()
            messages.success(request, 'Password updated successfully!')
            return redirect('list_officers')
    
    return render(request, 'edit_officer.html', {'officer': officer_instance})

# Delete Officer
def delete_officer(request, officer_id):
    officer_instance = get_object_or_404(Officer, id=officer_id)
    officer_instance.delete()
    messages.success(request, 'Officer deleted successfully!')
    return redirect('list_officers')


from django.shortcuts import render
from userapp.models import userreg  # Import the user model

def list_users(request):
    users = userreg.objects.all()  # Fetch all users
    return render(request, 'list_users.html', {'users': users})


from django.shortcuts import render
from userapp.models import Complaints
from django.shortcuts import render, get_object_or_404, redirect
from .models import Officer

def admin_complaints_view(request):
    complaints = Complaints.objects.all()
    officers = Officer.objects.all()
    return render(request, 'admin_complaints_list.html', {'complaints': complaints, 'officers': officers})


def assign_officer(request, complaint_id):
    if request.method == "POST":
        complaint = get_object_or_404(Complaints, id=complaint_id)
        officer_id = request.POST.get("officer_id")
        if officer_id:
            officer = get_object_or_404(Officer, id=officer_id)
            complaint.assigned_officer = officer
            complaint.save()
        return render(request,'admin_complaints_list.html')


from django.shortcuts import render
from userapp.models import Complaints

def assigned_complaints_view(request):
    complaints = Complaints.objects.exclude(assigned_officer__isnull=True)  # Fetch only assigned complaints
    return render(request, 'assigned_complaints.html', {'complaints': complaints})



from django.shortcuts import render
from userapp.models import Feedback

def admin_feedback_list(request):
    """View to display all feedbacks for the admin"""
    feedbacks = Feedback.objects.all()
    return render(request, 'admin_feedback_list.html', {'feedbacks': feedbacks})

