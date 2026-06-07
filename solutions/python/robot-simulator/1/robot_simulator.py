# Globals for the directions
# Change the values as you see fit
EAST = (1, 0)
NORTH =  (0, 1)
WEST = (-1, 0)
SOUTH = (0,-1)


class Robot:
    
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos 
        self.coordinates = (self.x_pos, self.y_pos)


    def move(self, move_command:str):
        directions = [NORTH,EAST,SOUTH,WEST]
        for i in move_command:
            match i:
                case "L":
                    # turn left
                    self.direction = directions[directions.index(self.direction)-1]
                
                case "R":
                    # turn right
                    self.direction = directions[(directions.index(self.direction)+1)%4]
                    
                case "A":
                    # advance
                    self.coordinates = (self.coordinates[0]+self.direction[0], self.coordinates[1]+self.direction[1])
            
                    
                    