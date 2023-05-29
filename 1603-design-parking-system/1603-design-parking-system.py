class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigcap = big
        self.mediumcamp = medium
        self.smallcap = small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bigcap:
                self.bigcap -= 1
                return True
            return False
        if carType == 2:
            if self.mediumcamp:
                self.mediumcamp -= 1
                return True
            return False
        if carType == 3:
            if self.smallcap:
                self.smallcap -= 1
                return True
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)