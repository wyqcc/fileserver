from django.urls import path, include

from files import views

urlpatterns = [
    path('upload', views.APIUploadHandler.as_view()),
    path('download/<str:img_name>', views.APIDownloadHandler.as_view()),
    path('filelist', views.ALIFinalist.as_view()),
    path('file', views.API_file.as_view()),
    path('root_url', views.Root_url.as_view()),
]
