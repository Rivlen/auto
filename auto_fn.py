def init_auto(brand, max_speed):
    return {
        "brand": brand,
        "speed": 0,
        "max_speed": max_speed,
        "engine": False
    }


bmw = init_auto("bmw", 310)
fiat = init_auto("fiat", 160)


def start_engine(auto):
    if not auto['engine']:
        auto['engine'] = True
        print('Silnik odpalony')
    else:
        print('Silnik był już odpalony')


def stop_engine(auto):
    if auto['speed'] == 0:
        auto['engine'] = False
        print("Silnik zgaszony")
    else:
        print('Zatrzymaj auto wpierw')


def speed_up(auto, amount):
    if auto['engine']:
        auto['speed'] = min(auto['speed'] + amount, auto['max_speed'])
        print(f"Jedziesz z prędkością {auto['speed']}")
    else:
        print("Odpal silnik")


def slow_down(auto, amount):
    auto['speed'] = max(auto['speed'] - amount, 0)
    print(f"Jedziesz z prędkością {auto['speed']}")


speed_up(bmw, 100)
start_engine(bmw)
speed_up(bmw, 100)
speed_up(bmw, 100)
speed_up(bmw, 200)
stop_engine(bmw)
slow_down(bmw, 150)
slow_down(bmw, 150)
slow_down(bmw, 150)
stop_engine(bmw)
