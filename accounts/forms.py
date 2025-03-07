from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser
from courses.models import Course  # Import Course model

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        help_text="Enter your first name",
        widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"})
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        help_text="Enter your last name",
        widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"})
    )

    phone = forms.CharField(
        max_length=15,
        required=False,
        help_text="Enter your phone number",
        widget=forms.TextInput(attrs={"placeholder": "Phone Number", "class": "form-control"})
    )

    email = forms.EmailField(
        required=True,
        help_text="Enter a valid email address",
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )

    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,
        required=True,
        help_text="Select your role",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    profile_picture = forms.ImageField(
        required=False,  
        help_text="Upload your profile picture",
        widget=forms.FileInput(attrs={"class": "form-control"})
    )

    address = forms.CharField(
        max_length=255,
        required=False,
        help_text="Enter your address",
        widget=forms.TextInput(attrs={"placeholder": "Address", "class": "form-control"})
    )

    bio = forms.CharField(
        required=False,
        help_text="Write something about yourself",
        widget=forms.Textarea(attrs={"placeholder": "Bio", "class": "form-control", "rows": 3})

    )

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "email", "phone", "role", "profile_picture", "address", "bio", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"placeholder": "Confirm Password", "class": "form-control"}),
        }


class CustomUserUpdateForm(UserChangeForm):
    password = None  # Hide password field in profile update

    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"})
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"})
    )

    phone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Phone Number", "class": "form-control"})
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )

    profile_picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"})
    )

    address = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Address", "class": "form-control"})
    )

    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "Bio", "class": "form-control", "rows": 3})


    )

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "email", "phone", "profile_picture", "address", "bio"]


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Old Password"})
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "New Password"})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm New Password"})
    )

    class Meta:
        model = CustomUser
        fields = ["old_password", "new_password1", "new_password2"]


# ✅ Form for adding courses
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "price", "duration", "category"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Course Name"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Course Description", "rows": 3}),
            "price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Course Price"}),
            "duration": forms.TextInput(attrs={"class": "form-control", "placeholder": "Course Duration"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }
