class NotFoundError(Exception):
    """Exception raised when a required resource is not found."""
    
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"NotFoundError: {self.message}"