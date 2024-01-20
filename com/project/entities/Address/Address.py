# aid,cid,city,country,state,street,zipcode
class Address:
    def __init__(self,aid,cid,city,country,state,street,zipcode):
        self._aid=aid
        self._cid=cid
        self._street=street
        self._city=city
        self._state=state
        self._zipcode=zipcode
        self._country=country
    @property
    def aid(self):
        return self._aid
    @aid.setter
    def aid(self,value):
        self._aid=value
    @property
    def cid(self):
        return self._cid
    @cid.setter
    def cid(self,value):
        self._cid=value
    @property
    def street(self):
        return self._street
    @street.setter
    def street(self,value):
        self._street=value
    @property
    def city(self):
        return self._city
    @city.setter
    def city(self,value):
        self._city=value
    @property
    def state(self):
        return self._state
    @state.setter
    def state(self,value):
        self._state=value
    @property
    def zipcode(self):
        return self._zipcode
    @zipcode.setter
    def zipcode(self,value):
        self._zipcode=value
    @property
    def country(self):
        return self._country
    @country.setter
    def country(self,value):
        self._zipcode=value
    def to_dict(self):
        return {

            "aid":self.aid,
            "cid":self.cid,
            "city":self.city,
            "state":self.state,
            "zipcode":self.zipcode,
            "country":self.country
        }
    @classmethod
    def from_dict(cls,data):
        return cls(**data)

    def __reper__(self):
        return f"Address(aid={self.aid} ,cid={self.cid},city={self.city},country={self.country},state={self.state},street={self.street},zipcode={self.zipcode})"


