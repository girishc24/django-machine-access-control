from rest_framework import serializers
from .models import  Machine, Axis


class AxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Axis
        fields = '__all__'


class MachineSerializer(serializers.ModelSerializer):
    axes = AxisSerializer(many=True, read_only=True)

    class Meta:
        model = Machine
        fields = '__all__'
    
    def to_representation(self, instance):
        user = self.context['request'].user
        data = super().to_representation(instance)

        if user.groups.filter(name__in=['Manager', 'Supervisor']).exists():
            data.pop('tool_in_use', None)  
        elif user.groups.filter(name='Operator').exists():
            return {'tool_in_use': data.get('tool_in_use')}  

        return data

