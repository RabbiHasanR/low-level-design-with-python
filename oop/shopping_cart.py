from typing import Any


class Item:
    
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    
    
    def __repr__(self) -> str:
        return f"Item(name='{self.name}', price='{self.price}')"
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Item):
            return self.name == value.name and self.price == value.price
        return False



class ShoppingCart:
    
    __slots__=['items', 'item_quantities']
    
    def __init__(self) -> None:
        self.items = []
        self.item_quantities = {}
    
    def __repr__(self) -> str:
        return f"ShoppingCart(items={self.items})"
    
    def __str__(self) -> str:
        return f"ShoppingCart with {len(self.items)} items."
    
    def __len__(self) -> int:
        return len(self.items)
    
    def __getitem__(self, item_name) -> int:
        return self.item_quantities.get(item_name, 0)
    
    def __setitem__(self, item_name, quantity):
        if quantity > 0:
            self.item_quantities[item_name] = quantity
        else:
            if item_name in self.item_quantities:
                del self.item_quantities[item_name]
    
    def __contains__(self, item):
        return item.name in self.item_quantities
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return sum(item.price * self.item_quantities[item.name] for item in self.items)
    
    