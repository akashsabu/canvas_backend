from django.urls import path
from .views import CanvasDataUpload, user_canvas_data_list

urlpatterns = [
    path('upload/', CanvasDataUpload, name='jsonfile-upload'),
    path('user_canvas_data/', user_canvas_data_list, name='user_canvas_data'),
]
