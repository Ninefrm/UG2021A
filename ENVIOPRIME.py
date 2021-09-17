class warehouse:
    def __init__(self, name, destiny, distance, subscription):
        self.name = name
        self.destiny = destiny
        self.distance = distance
        self.subscription = subscription

def fromTo(warehousesA, init, destinyO, subscription, route):
    init = init+subscription[0]
    destiny = destinyO+subscription[0]
    fwarehouse = warehousesA[init]
    route = route + ' ' + init
    if fwarehouse.destiny+subscription[0] == destiny:
        return print(route)
    else:
        fromTo(warehousesA, fwarehouse.destiny, destinyO, subscription, route)

warehouses = {
    'TJN': warehouse('TJ', 'MXL', 100, 'NORMAL'),
    'MXLN': warehouse('MXL', 'HMO', 300, 'NORMAL'),
    'HMON': warehouse('HMO', 'CUL', 400, 'NORMAL'),
    'CULN': warehouse('CUL', 'MZT', 100, 'NORMAL'),
    'MZTN': warehouse('MZT', 'PVR', 100, 'NORMAL'),
    'PVRN': warehouse('PVR', 'GDL', 100, 'NORMAL'),
    'GDLN': warehouse('GDL', 'AGU', 100, 'NORMAL'),
    'AGUN': warehouse('AGU', 'BJX', 50, 'NORMAL'),
    'TJP': warehouse('TJ', 'BJX', 2500, 'PREMIUM'),
    'TJS': warehouse('TJ', 'MXL', 100, 'STANDARD'),
    'MXLS': warehouse('MXL', 'BJX', 1795, 'STANDARD'),
}

# print(warehouses['TJN'].name)

fromTo(warehouses, 'TJ', 'BJX', 'STANDARD', '')