class Ship:
    ''' Blueprint for the ship objects '''
    def __init__(self, size):
        self.size = size
        self.rotation = "hori"
        self.position_x = 0
        self.position_y = 0
        self.cords = []

    def ship_cords(self):
        for i in range(self.size):
            #Adds coordinates of the ship to cords list
            if self.rotation == 'hori':
                self.cords.append((self.position_y,self.position_x+i))
            else:
                self.cords.append((self.position_y+i,self.position_x))
    
    def __del__(self):
        del self
        