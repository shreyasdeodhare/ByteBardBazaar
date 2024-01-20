class Status:
    def __init__(self,status_id,status_name,odid):
        self._status_id=status_id
        self._status_name=status_name
        self._odid = odid
    @property
    def status_id(self):
        return self._status_id
    @status_id.setter
    def status_id(self,value):
        self._status_id=value
    @property
    def status_name(self):
        return self._status_name
    @status_name.setter
    def status_name(self,value):
        self._status_name=value
    @property
    def odid(self):
        return self._odid
    @odid.setter
    def odid(self,value):
        self._odid=value
    def to_dict(self):
        return{
            'status_id':self.status_id,
            'status_name':self.status_name,
            'odid':self.odid
        }
    @classmethod
    def from_dict(cls,data):
        return cls(**data)

    def __repr__(self):
        return f"Status(status_id={self.status_id} ,status_name={self.status_name},odid={self.odid})"

