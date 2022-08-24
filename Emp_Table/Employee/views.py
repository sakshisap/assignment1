from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework import status

#from django.contrib import messages

from .serializers import EmployeeSerializer
from .models import Employee
from django.shortcuts import get_object_or_404


class EmployeeViews(APIView): #here we use apiview class to represent views.
    
    def post(self, request): # POST request handeler
        '''
        this function is used to insert data into the database
        '''
        serializer = EmployeeSerializer(data=request.data)# here create object from request.data
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data)
        else:
            return Response( serializer.errors)

    def get(self, request, id=None):# GET request handeler function
        '''Get function is use to dispaly records according to id,name,age,desg and all records also.'''
        parameter_dict =request.query_params
        
        # filter for search by 'name'
        if 'name' in parameter_dict.keys():
            
            
            filtering_data = parameter_dict['name']
            all_Employee_obj = Employee.objects.filter(Emp_name=filtering_data)
            serializer = EmployeeSerializer(all_Employee_obj, many=True)
            return Response(serializer.data)
        
        
        elif 'age' in parameter_dict.keys():#filter for search by 'age'
           
            
            filtering_data = parameter_dict['age']
            all_Employee_obj = Employee.objects.filter(Age=filtering_data)
            serializer = EmployeeSerializer(all_Employee_obj, many=True)
            return Response(serializer.data)
        
        #filter for search by 'designation'
        elif 'desg' in parameter_dict.keys():
            filtering_data = parameter_dict['desg']
            all_Employee_obj = Employee.objects.filter(Desg=filtering_data)
            serializer = EmployeeSerializer(all_Employee_obj, many=True)
            return Response(serializer.data)
        
        #use foe search by id 
        elif id: 
            try:
                item = Employee.objects.get(id=id)
                serializer = EmployeeSerializer(item)
                return Response(serializer.data)
            except Employee.DoesNotExist:
                return Response("Employee Does not exist") 
                    
        # display all records            
        items = Employee.objects.all()       
        serializer = EmployeeSerializer(items, many=True)
        return Response( serializer.data)
    
    
   
     #put request handler
    def put(self, request, id=None):  
        '''this function is used to modify resorce and update data according to id. 
           if id does note exist then it will create new record..'''
        data=request.data 
        id = data['id']
        
        try:
            item = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Employee.DoesNotExist:
            serializer = EmployeeSerializer(data=request.data)# here create object from request.data
            if serializer.is_valid():
                serializer.save()
            return Response({"Employee Does Not Exist.. created new record." :serializer.data})
            #return Response("Employee Does not exist")   

    #patch request handler
    def patch(self,request, id=None): 
        '''this function is used to modify resorce with partial data and update it according to id.'''
        
        try:
            item = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response( serializer.data)
        except Employee.DoesNotExist:
            return Response("Employee Does Not Exist")
            
        
    #delete request handler function
    def delete(self, request, id=None):
        '''this function is use to delete record according to given id.. '''
        
        item = get_object_or_404(Employee, id=id)
        item.delete()
        return Response("Item Deleted")
    
   
        
        
    
    
    
        