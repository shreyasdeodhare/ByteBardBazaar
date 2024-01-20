class Category:
    def __init__(self,categoryid,category_name):
        self._categroyid=categoryid
        self._category_name=category_name
    @property
    def categoryid(self):
        return self._categroyid
    @categoryid.setter
    def categoryid(self,value):
        self._categroyid=value
    @property
    def category_name(self):
        return self._category_name
    @category_name.setter
    def category_name(self,value):
        self.category_name=value
    def to_dict(self):
        return{
            'categoryid':self.categoryid,
            'categoryname':self.category_name
        }
    @classmethod
    def from_dict(cls,data):
        return cls(**data)
    def __reper__(self):
        return f"Category(category_id={self.categoryid} ,name={self._category_name})"