from django.conf.urls import url
from User_App import views

app_name = 'User_App'

urlpatterns = [
    url(r'^register/',views.register,name='register')
]
