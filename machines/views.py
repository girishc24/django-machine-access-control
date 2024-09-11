from django.shortcuts import render
from django.http import HttpResponse
from .permissions import IsSuperAdmin, IsManager, IsSupervisor, IsOperator
from .models import Machine, Axis
from .serializers import MachineSerializer, AxisSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

def members(request):
    return HttpResponse('Welcome to Ethereal Machines')

class MachineViewSet(APIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def get_permissions(self):
        user = self.request.user

        if user.groups.filter(name='Superadmin').exists():
            return [IsSuperAdmin()]
        if user.groups.filter(name='Manager').exists():
            return [IsManager()]
        if user.groups.filter(name='Supervisor').exists():
            return [IsSupervisor()]
        if user.groups.filter(name='Operator').exists():
            return [IsOperator()]
        return [IsAuthenticated()]