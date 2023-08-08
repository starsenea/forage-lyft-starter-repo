from tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_sensor_data):
        self.tire_sensor_data = tire_sensor_data

    def needs_service(self):
        for tire in self.tire_sensor_data:
            if tire >= 0.9:
                return True
        return False
