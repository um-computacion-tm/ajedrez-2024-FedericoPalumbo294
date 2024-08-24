class Piece:
    
    def __init__(self, color):
        self.color = color    

    # Implementar la lógica de movimiento     
    def move(self, start_pos, end_pos):         
        raise NotImplementedError("This method should be overridden by subclasses")