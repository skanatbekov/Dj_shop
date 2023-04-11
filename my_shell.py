from shop.models import *

item = Item.objects.create(name="Nike shoes", price=100)
item = Item.objects.create(name="Nike wmn shoes", price=100)
item = Item.objects.create(name="Nike cap", price=25)
item = Item.objects.create(name="Nike wmn cap", price=25)
item = Item.objects.create(name="Nike socks", price=10)
item = Item.objects.create(name="Nike wmn socks", price=10)
item = Item.objects.create(name="Nike shorts", price=20)
item = Item.objects.create(name="Nike wmn shorts", price=20)
item = Item.objects.create(name="Nike t-shirt", price=20)
item = Item.objects.create(name="Nike wmn t-shirt", price=20)

items = Item.objects.all()
items

purchase = Purchase.objects.create(item_id=4, name="Max", age="34")
purchase = Purchase.objects.create(item_id=6, name="David", age="14")
purchase = Purchase.objects.create(item_id=2, name="Olivia", age="50")
purchase = Purchase.objects.create(item_id=1, name="Alex", age="20")
purchase = Purchase.objects.create(item_id=4, name="Anna", age="19")
purchase = Purchase.objects.create(item_id=7, name="Noah", age="33")
purchase = Purchase.objects.create(item_id=5, name="Kate", age="28")
purchase = Purchase.objects.create(item_id=5, name="Mark", age="60")
purchase = Purchase.objects.create(item_id=3, name="Claire", age="44")
purchase = Purchase.objects.create(item_id=8, name="Michael", age="18")
purchase = Purchase.objects.create(item_id=9, name="Jack", age="31")
purchase = Purchase.objects.create(item_id=4, name="Brad", age="56")
purchase = Purchase.objects.create(item_id=3, name="Rose", age="47")
purchase = Purchase.objects.create(item_id=7, name="Julie", age="52")
purchase = Purchase.objects.create(item_id=5, name="Jordan", age="68")
purchase = Purchase.objects.create(item_id=2, name="Jury", age="18")
purchase = Purchase.objects.create(item_id=1, name="Don", age="26")
purchase = Purchase.objects.create(item_id=9, name="Mel", age="40")
purchase = Purchase.objects.create(item_id=10, name="Angelina", age="32")

purchases = Purchase.objects.all()
purchases





