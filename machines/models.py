from django.db import models



class Machine(models.Model):
    machine_id = models.CharField(max_length=255, unique=True)
    machine_name = models.CharField(max_length=255)
    tool_capacity = models.IntegerField()
    tool_offset = models.FloatField()
    feedrate = models.IntegerField()
    tool_in_use = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.machine_name} ({self.machine_id})"

class Axis(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name="axes")
    axis_name = models.CharField(max_length=1)  
    max_acceleration = models.FloatField()
    max_velocity = models.FloatField()
    actual_position = models.FloatField()
    target_position = models.FloatField()
    distance_to_go = models.FloatField()
    homed = models.BooleanField(default=False)
    acceleration = models.FloatField()
    velocity = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.axis_name} Axis of {self.machine.machine_name}"
