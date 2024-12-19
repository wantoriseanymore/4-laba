class Car:
 color = None # цвет автомобиля
 fuel = None #количество топлива
 name = None #название автомобиля
 max_speed = None #максимальная скорость

 def go(self):
  # Команда ехать:
  pass
	
 def turn(self):
  # Команда поворачивать:
  pass

 def stop(self):
 # Команда остановиться:
  pass
myCar = Car()
myCar.color = 'red'  # красим в красный цвет
myCar.fuel = 50    # заливаем топливо
myCar.name = 'Belaz'
myCar.max_speed = '50 km/h'
myCar.go() 
myCar.turn() 
myCar.stop()
machine = [myCar.color, myCar.fuel, myCar.name, myCar.max_speed]
print(machine)