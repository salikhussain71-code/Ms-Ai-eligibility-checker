# exceptions.py
# Custom exception for invalid scores
# CS50P Week 3 - Exceptions

class InvalidScoreError(Exception):
    """Raised when CGPA or IELTS score is out of valid range."""
    pass