class Tower:
    def __init__(self, name):
        self.name = name
        self.discList = []
    
    def placeDisc(self, disc, supressPrint: bool):
        if (len(self.discList) == 0):
            self.discList.append(disc)
            return
        if (self.discList[-1] < disc):
            if (not supressPrint):
                print("Can't place bigger disc on smaller disc!")
            return
        self.discList.append(disc)
    
    def takeDisc(self, supressPrint: bool):
        if (len(self.discList) == 0):
            if (not supressPrint):
                print("No discs on this tower")
            return
        return self.discList.pop()