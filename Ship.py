class Ship:
    ''' Blueprint for the ship objects '''
    def __init__(self, size):
        self.size = size
        self.rotation = "hori"
        self.position_x = 0
        self.position_y = 0