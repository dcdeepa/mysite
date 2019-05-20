
from django.urls import path
from django.contrib import admin

from . import views

app_name = 'polls'

admin.site.site_header="MY VOTE"
admin.site.site_title="myvote"
admin.site.index_title="VOTING"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
