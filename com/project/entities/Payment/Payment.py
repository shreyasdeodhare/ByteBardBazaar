class Payment:
    def __init__(self,payid,pdate,amount,paymethod,oid):
        self._payid = payid
        self._pdate= pdate
        self._amount = amount
        self._paymethod =paymethod
        self._oid = oid

    @property
    def payid(self):
        return self._payid

    @payid.setter
    def payid(self, value):
        self._payid = value

    @property
    def pdate(self):
        return self._pdate
    @pdate.setter
    def pdate(self,value):
        self._pdate=value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def paymethod(self):
        return self._paymethod

    @paymethod.setter
    def paymethod(self, value):
        self._paymethod = value

    @property
    def oid(self):
        return self._oid

    @oid.setter
    def oid(self, value):
        self._oid = value
    def to_dict(self):
        return {

            "payid": self.payid,
            "pdate":self.pdate,
            "amount":self.amount,
            "paymehtod":self.paymethod,
            "oid":self.oid

        }
    @classmethod
    def from_dict(cls,data):
        return cls(**data)

    def __repr__(self):
        return f"Payment(payid={self.payid} ,pdate={self.pdate},amount={self.amount},paymethod={self.paymethod},oid={self.oid})"
