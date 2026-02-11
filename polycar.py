class vehicle:
    def move(self):
        print("this vehical is moving")
        
class car(vehicle):
    def move(self):
        print("driving on the road.")
class bicycle(vehicle):
    def move(self):
        print("padeling in the road")
vehicles=[car(),bicycle()]
for vehicle in vehicle:
    vehicle.move()