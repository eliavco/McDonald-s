from django.urls import path,re_path
from home_page.views import McHomeView,McListView,McDetailView,McGallery,McCreateView,McUpdateView,McDeleteView

app_name = 'home'

urlpatterns = [
    path('',McHomeView.as_view(),name="home"),
    path('list/',McListView.as_view(),name="list"),
    path('gallery/',McGallery.as_view(),name="gallery"),
    path('create/',McCreateView.as_view(),name="create"),
    re_path(r'^update/(?P<pk>\d+)/$',McUpdateView.as_view(),name="update"),
    re_path(r'^list/(?P<pk>\d+)/$',McDetailView.as_view(),name="detail_list"),
    re_path(r'^(?P<pk>\d+)/$',McDetailView.as_view(),name="details"),
    re_path(r'^delete/(?P<pk>\d+)/$',McDeleteView.as_view(),name="delete"),
]
