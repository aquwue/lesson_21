from classes import Shop, Store, Request


if __name__ == '__main__':
    store = Store()
    print("Всего на складе: ")
    list_1 = store.get_items()
    for i, v in list_1.items():
        print(v, i)
    str_1 = input()
    request = Request(str_1)
    print(f"Курьер забирает {request.amount} {request.product} из {request.from_}")
    print(f"Курьер везет {request.amount} {request.product} со {request.to} в {request.to}")
    print(f"Курьер доставил {request.amount} {request.product} в {request.to}")
    shop = Shop()
    shop.add(request.product, request.amount)
    store.remove(request.product, request.amount)
    print("В склад хранится: ")
    list_1 = store.get_items()
    for i, v in list_1.items():
        print(v, i)
    print("\nВ магазин хранится: ")
    list_2 = shop.get_items()
    for i, v in list_2.items():
        print(v, i)

