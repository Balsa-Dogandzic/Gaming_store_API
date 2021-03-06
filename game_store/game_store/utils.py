"""Module for custom exception handling"""
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    """Custom exception handler class"""
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status'] = response.status_code
        response.data['success'] = False

    return response
