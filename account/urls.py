from django.urls import path
from . import views


urlpatterns = [
    path('account-page1', views.AccountPage1, name="AccountPage1"),
    # path('account-page2', views.AccountPage2, name="AccountPage2"),
    path('', views.AccountPage2, name="AccountPage2"),
]
