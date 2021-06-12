from django.conf.urls import url
import boards.views
urlpatterns = [
    path('',views.home, name='board' )
    
]