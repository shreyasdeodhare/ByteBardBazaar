class OrderDetails:
    def __init__(self,odid,oid,payid,pid,quantity):
        self._odid=odid
        self._oid=oid
        self._payid=payid
        self._pid = pid
        self._quantity=quantity


    @property
    def odid(self):
        return self._odid
    @odid.setter
    def odid(self,value):
        self._odid=value
    @property
    def oid(self):
        return self._oid
    @oid.setter
    def oid(self,value):
        self._oid=value

    @property
    def payid(self):
        return self._payid

    @payid.setter
    def payid(self, value):
        self._payid = value
    @property
    def pid(self):
        return self._pid
    @pid.setter
    def pid(self,value):
        self._pid=value
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self,value):
        self._quantity=value


    def  to_dict(self):
        return {
            'odid':self.odid,
            'oid':self.oid,
            'payid':self.payid,
            'pid': self.pid,
            'quantity':self.quantity,



        }
    @classmethod
    def from_dict(cls,data):
        return cls(**data)
    def __reper__(self):
        return f"OrderDetails(odid={self.odid}, oid={self.oid},payid={self.payid},pid={self.pid},quantity={self.quantity} )"

