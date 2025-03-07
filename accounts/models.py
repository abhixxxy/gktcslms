from django.db import models
from django.contrib.auth.models import AbstractUser

# ✅ Custom User Model
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("trainer", "Trainer"),
        ("student", "Student"),
    ]

    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="student")
    profile_picture = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_users_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_users_permissions",
        blank=True,
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    def get_full_name(self):
        """Returns the full name of the user."""
        return f"{self.first_name} {self.last_name}".strip()

    def get_role_display(self):
        """Returns the role name in a user-friendly format."""
        return dict(self.ROLE_CHOICES).get(self.role, "Unknown")

    # ✅ Role-based helper methods
    def is_admin(self):
        return self.role == "admin"

    def is_trainer(self):
        return self.role == "trainer"

    def is_student(self):
        return self.role == "student"


# ✅ Course Model (Fixed Name Error)
class Course(models.Model):
    CATEGORY_CHOICES = [
        ("programming", "Programming"),
        ("data_science", "Data Science"),
        ("design", "Design"),
        ("marketing", "Marketing"),
        ("business", "Business"),
    ]

    title = models.CharField(max_length=255)  # ✅ Corrected field name (was `name`)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    duration = models.CharField(max_length=100, help_text="Duration (e.g., '4 weeks')")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="programming")
    created_at = models.DateTimeField(auto_now_add=True)
    trainer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "trainer"},
        related_name="courses",
    )

    def __str__(self):
        return f"{self.title} - {self.get_category_display()}"

    def get_category_display(self):
        """Returns the category name in a user-friendly format."""
        return dict(self.CATEGORY_CHOICES).get(self.category, "Unknown")
