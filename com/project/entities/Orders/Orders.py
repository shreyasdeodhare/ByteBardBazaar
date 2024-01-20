class Orders:
    def __init__(self,oid,cid,orderdate,payid):
        self._oid=oid
        self._cid=cid
        self._orderdate=orderdate
        self._payid=payid
    @property
    def oid(self):
        return self._oid
    @oid.setter
    def oid(self,value):
        self._oid=value
    @property
    def cid(self):
        return self._cid
    @cid.setter
    def cid(self,value):
        self._cid=value
    @property
    def orderdate(self):
        return self._orderdate
    @orderdate.setter
    def orderdate(self,value):
        self._orderdate=value
    @property
    def payid(self):
        return self._payid
    @payid.setter
    def payid(self,value):
        self._payid=value
    def to_dict(self):
        return{
            'oid':self.oid,
            'cid':self.cid,
            'orderdate':self.orderdate,
            'payid':self.payid
        }
    @classmethod
    def from_dict(cls,data):
      return cls(**data)

    def __reper__(self):
        return f"Orders(oid={self.oid},cid={self.cid},orderdate={self.orderdate},payid={self.payid})"
