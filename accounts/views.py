from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from .forms import CustomUserCreationForm, CustomUserUpdateForm, CustomPasswordChangeForm, CourseForm
from .decorators import admin_required, trainer_required, student_required
from courses.models import Course  # Ensure correct import

def index(request):
    return HttpResponse("Welcome to the Accounts App!")

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "accounts/register.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.role = form.cleaned_data["role"]

            # Handle Profile Picture Upload
            user.profile_picture = request.FILES.get("profile_picture")

            user.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect_dashboard(user)
        
        return render(request, "accounts/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect_dashboard(user)
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "accounts/login.html")

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")

@login_required
def profile_update(request):
    user = request.user  # Get logged-in user instance

    if request.method == "POST":
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=user)

        # Preserve existing profile picture if not updated
        form.instance.profile_picture = request.FILES.get("profile_picture", user.profile_picture)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile")  # Redirect to profile page
    else:
        form = CustomUserUpdateForm(instance=user)
    
    return render(request, "accounts/profile_update.html", {"form": form})

@login_required
def change_password(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been updated successfully!")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, "accounts/change_password.html", {"form": form})

@login_required
@admin_required
def admin_dashboard(request):
    return render(request, "accounts/admin_dashboard.html")

@login_required
@trainer_required
def trainer_dashboard(request):
    return render(request, "accounts/trainer_dashboard.html")

@login_required
@student_required
def student_dashboard(request):
    return render(request, "accounts/student_dashboard.html")

def redirect_dashboard(user):
    """Redirect user to the appropriate dashboard based on their role."""
    if user.role == "admin":
        return redirect("admin_dashboard")
    elif user.role == "trainer":
        return redirect("trainer_dashboard")
    return redirect("student_dashboard")

# ✅ Improved Add Course View (Using Forms)
@login_required
@admin_required
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.trainer = request.user  # Assign the logged-in admin/trainer
            course.save()
            messages.success(request, "Course added successfully!")
            return redirect("admin_dashboard")
    else:
        form = CourseForm()

    return render(request, "accounts/add_course.html", {"form": form})
