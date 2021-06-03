from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='app2'

urlpatterns = [
#    path('', views.index, name='index'),
    path('',views.searching, name='searching'),
    # path('/download/',views.file_download, name='file_download'),
    # path('', views.UploadList.as_view(), name='upload_list'),
    # path('download/<int:pk>/', views.download, name='download')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)