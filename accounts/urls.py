from django.urls import path
from .views import (
    index, RegisterView, user_login, user_logout, profile_update,
    change_password, admin_dashboard, trainer_dashboard, student_dashboard, add_course
)

urlpatterns = [
    path("", index, name="index"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/update/", profile_update, name="profile"),
    path("change-password/", change_password, name="change_password"),
    path("admin/dashboard/", admin_dashboard, name="admin_dashboard"),
    path("trainer/dashboard/", trainer_dashboard, name="trainer_dashboard"),
    path("student/dashboard/", student_dashboard, name="student_dashboard"),
    path("add-course/", add_course, name="add_course"),  # ✅ Ensure this exists
]
    