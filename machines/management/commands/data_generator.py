from django.core.management.base import BaseCommand
from machines.models import Machine, Axis
import random

class Command(BaseCommand):
    help = 'Generates random machine data for 20 machines with axes'

    def handle(self, *args, **kwargs):
        def create_machine(machine_id, machine_name, tool_capacity, tool_offset, feedrate, tool_in_use):
            machine = Machine.objects.create(
                machine_id=machine_id,
                machine_name=machine_name,
                tool_capacity=tool_capacity,
                tool_offset=tool_offset,
                feedrate=feedrate,
                tool_in_use=tool_in_use
            )
            return machine

        def create_axis(machine, axis_name, max_acceleration, max_velocity, actual_position, target_position):
            axis = Axis.objects.create(
                machine=machine,
                axis_name=axis_name,
                max_acceleration=max_acceleration,
                max_velocity=max_velocity,
                actual_position=actual_position,
                target_position=target_position,
                distance_to_go=abs(target_position - actual_position),
                homed=random.choice([True, False]),
                acceleration=random.uniform(0, 150),
                velocity=random.uniform(0, 80)
            )
            return axis

        def generate_random_values_for_20_machines():
            for i in range(1, 21):
                machine_id = f"EMXP{i}"
                machine_name = f"Machine-{i}"
                tool_capacity = 24
                tool_offset = random.uniform(5, 40)
                feedrate = random.randint(0, 20000)
                tool_in_use = random.randint(1, tool_capacity)

                machine = create_machine(machine_id, machine_name, tool_capacity, tool_offset, feedrate, tool_in_use)

                for axis_name in ['X', 'Y', 'Z', 'A', 'C']:
                    max_acceleration = 200
                    max_velocity = 60
                    actual_position = random.uniform(-190, 190)
                    target_position = random.uniform(-190, 191)

                    create_axis(machine, axis_name, max_acceleration, max_velocity, actual_position, target_position)

        generate_random_values_for_20_machines()
        self.stdout.write(self.style.SUCCESS('Successfully generated machine data for 20 machines'))
