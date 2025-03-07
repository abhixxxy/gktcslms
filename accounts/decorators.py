from django.core.exceptions import PermissionDenied
from functools import wraps

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "admin":
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view

def trainer_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "trainer":
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view

def student_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "student":
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view
