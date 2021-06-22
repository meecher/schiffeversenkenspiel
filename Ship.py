class Ship:
    ''' Blueprint for the ship objects '''
    def __init__(self, size):
        self.size = size
        self.rotation = "hori"
        self.position_x = 0
        self.position_y = 0
        self.cords = []

    def ship_cords():
        for i in size:
            if rotation == 'hori':
                cords.append((position_y,position_x+i))
            else:
                cords.append((position_y+i,position_x))