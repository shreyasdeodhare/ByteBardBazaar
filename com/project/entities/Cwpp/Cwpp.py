class Cwpp:
    def __init__(self,cname,p_name,purchase_count):
        self._cname=cname
        self._p_name=p_name
        self._purchase_count=purchase_count
    @property
    def cname(self):
        return self._cname
    @cname.setter
    def cname(self,value):
        self._cname=value
    @property
    def p_name(self):
        return self._p_name
    @p_name.setter
    def p_name(self,value):
       self._p_name=value
    @property
    def purchase_count(self):
        return self._purchase_count
    @purchase_count.setter
    def purchase_count(self,value):
        self._purchase_count = value
    def to_dict(self):
        return{
          'cname' : self.cname,
          'p_name':self.p_name,
          'purchase_count':self.purchase_count
        }
    @classmethod
    def from_dict(cls,data):
        return cls(**data)
    def __reper__(self):
        return f"Dwpp(cname={self.cname} ,name={self.p_name},purchase_count={self.purchase_count})"