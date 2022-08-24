from .views import EmployeeViews


from django.urls import path



urlpatterns = [
    
    
    path('', EmployeeViews.as_view()), 
    path('<int:id>', EmployeeViews.as_view())
]