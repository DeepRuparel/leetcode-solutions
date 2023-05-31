class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        #self.checkout = {}
        self.average = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [t, stationName]
    

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (id in self.checkin):
            time = self.checkin[id][0]
            #print(time)
            departstation = self.checkin[id][1]
            timetaken = t - time
            if departstation+' '+stationName in self.average:
                self.average[departstation+' '+stationName].append(timetaken)
            else:
                self.average[departstation+' '+stationName] = [timetaken]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        #print(self.average)
        times = self.average[startStation+' '+endStation]
        #print(times)
        average = sum(times)/len(times)
        return average
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)