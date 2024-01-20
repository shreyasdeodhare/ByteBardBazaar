class Customer:
    def __init__(self,cid,cname,c_email,c_number):
        self._cid=cid
        self._cname=cname
        self._c_email=c_email
        self._c_number = c_number
    @property
    def cid(self):
        return self._cid
    @cid.setter
    def cid(self,value):
        self._cid=value
    @property
    def cname(self):
        return self._cname
    @cname.setter
    def cname(self,value):
        self._cname=value


    @property
    def c_email(self):
        return self._c_email
    @c_email.setter
    def c_email(self,value):
        self._c_email=value

    @property
    def c_number(self):
        return self._c_number

    @c_number.setter
    def c_number(self, value):
        self._c_number = value
    def to_dict(self):
        return {
            'cid': self.cid,
            'cname':self.cname,
            'c_email': self.c_email,
            'c_number': str(self.c_number),

        }
    @classmethod
    def from_dict(cls,data):
        def from_dict(cls,data):
            return cls(**data)
    def __reper__(self):
        return f"Customer(cid={self.cid} ,cname={self.cname} ,c_email={self.c_email},c_number={self.c_number})"






