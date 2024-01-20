class Product:
    def __init__(self, p_id, p_name, p_available_stock, p_sell_stock, p_price_per_item, p_is_available,p_category_id):
        self._p_id = p_id
        self._p_name = p_name
        # self._p_category = p_category
        self._p_available_stock = p_available_stock
        self._p_sell_stock = p_sell_stock
        self._p_price_per_item = p_price_per_item
        self._p_is_available = p_is_available
        self._p_category_id= p_category_id

    @property
    def p_id(self):
        return self._p_id

    @p_id.setter
    def p_id(self, value):
        self._p_id = value

    @property
    def p_name(self):
        return self._p_name

    @p_name.setter
    def p_name(self, value):
        self._p_name = value





    @property
    def p_available_stock(self):
        return self._p_available_stock

    @p_available_stock.setter
    def p_available_stock(self, value):
        self._p_available_stock = value

    @property
    def p_sell_stock(self):
        return self._p_sell_stock

    @p_sell_stock.setter
    def p_sell_stock(self, value):
        self._p_sell_stock = value

    @property
    def p_price_per_item(self):
        return self._p_price_per_item

    @p_price_per_item.setter
    def p_price_per_item(self, value):
        self._p_price_per_item = value

    @property
    def p_is_available(self):
        return self._p_is_available

    @p_is_available.setter
    def p_is_available(self, value):
        self._p_is_available = value
    @property
    def p_category_id(self):
        return  self._p_category_id
    @p_category_id.setter
    def p_category_id(self,value):
        self._p_category_id=value
    def to_dict(self):
        return{
            'p_id':self.p_id,
            'p_name':self.p_name,
            # 'p_category':self.p_category,
            'p_available_stock':self.p_available_stock,
            'p_sell_stock':self.p_sell_stock,
            'p_price_per_item':self.p_price_per_item,
            'p_is_available':self.p_is_available,
            'p_category_id':self.p_category_id
        }
    @classmethod
    def from_dict(cls,data):
        return cls(**data)

    def __repr__(self):
        return f"Product(p_id={self.p_id}, p_name={self.p_name},  " \
               f"p_available_stock={self.p_available_stock}, p_sell_stock={self.p_sell_stock}, " \
               f"p_price_per_item={self.p_price_per_item}, p_is_available={self.p_is_available} ,"\
                f"p_category_id={self.p_category_id})"
