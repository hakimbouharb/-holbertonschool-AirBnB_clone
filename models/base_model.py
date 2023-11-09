#!usr/bin/python3
"""Write a class BaseModel that defines all 
common attributes/methods for other classes:"""

import uuid
from datetime import datetime



class baseModel:
    """this is class BaseModel"""
    
    def __init__(self):
        """constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    
    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return "".format(
            self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """updates the public instance attribute 
        updated_at with the current datetime"""

        self.updated_at = date_time.now()


    def to_dict(self):
        """eturns a dictionary containing all keys/values of
          __dict__ of the instance:"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
        







        
