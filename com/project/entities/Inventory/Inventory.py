class Inventory:
    def __init__(self,quantity,created_at,modified_at,deleted_at,inv_id,pid):

         self._quantity=quantity
         self._created_at=created_at
         self._modified_at=modified_at
         self._deleted_at=deleted_at
         self._inv_id=inv_id
         self._pid = pid

    @property
    def inv_id(self):
        return self._inv_id

    @inv_id.setter
    def inv_id(self, value):
        self._inv_id = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value

    @property
    def modified_at(self):
        return self._modified_at

    @modified_at.setter
    def modified_at(self, value):
        self._modified_at = value

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        self._created_at = value

    @property
    def deleted_at(self):
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, value):
        self._deleted_at = value

    def to_dict(self):
        return {
            'quantity':self.quantity,
            'created_at':self.created_at,
            'modified_at': self.modified_at,
            'deleted_at': self.deleted_at,
            'pid': self.pid,
            'inv_id': self.inv_id


        }

    @classmethod
    def from_dict(cls, data):

        return cls(**data)

    def __reper__(self):
        return f"Inventory(quantity:{self.quantity},created_at:{self.created_at},modified_at:{self.modified_at},deleted_at:{self.deleted_at},inv_id:{self.inv_id},pid:{self.pid})"

