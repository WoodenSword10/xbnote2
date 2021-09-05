from django.urls import path, re_path
from . import views

urlpatterns = [
    path('center', views.index_view),
    path('delete/<int:note_id>', views.delete_view),
    path('download_csv', views.download_csv_view),
    path('download_page',views.download_page_view),
]