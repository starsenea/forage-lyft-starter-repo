from abc import ABC, abstractmethod

class Battery(Car):
  def __init__(self, last_service_date, current_date):
      self.last_service_date = last_service_date
      self.current_date = current_date
  def battery_needs_service(self):
        pass  
  

