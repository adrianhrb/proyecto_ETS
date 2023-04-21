USERS = {}
DRIVERS = {}
SCUDERIAS = {}
USERS_TEAMS = {}
# STANDING = dict(sorted(STANDING.items(), key=lambda d: d[1], reverse=True))
DRIVERS_STANDING = {}
SCUDERIAS_STANDING = {}
USER_RANKINGS = {}
RACE_CALENDAR = {}


def define_driver_standing():
    for driver in DRIVERS:
        DRIVERS_STANDING[driver] = DRIVERS[driver]["points"]
    return "Definida clasificacion de pilotos"


def define_scuderias_standing():
    for scuderia in SCUDERIAS:
        SCUDERIAS_STANDING[scuderia] = SCUDERIAS[scuderia]["points"]


def add_driver_points(driver_number: int, points: int):
    driver_number.add_points(points)
    DRIVERS_STANDING[driver_number] += points
    driver_scuderia = driver_number.scuderia
    driver_scuderia.points += points
    for user_team in USERS_TEAMS:
        for driver in USERS_TEAMS[user_team]["drivers"]:
            if driver == driver_number:
                USERS_TEAMS[user_team]["points"] += points


class User:
    def __init__(
        self, id: int, name: str, lastname: str, email: str, password: str, budget: int
    ):
        """Ademas de ser el constructor, la creacion de un nuevo objeto cumple la funcion de
        creacion de una cuenta en la aplicacion"""
        if id not in USERS:
            self.id = id
        else:
            self.id = list(USERS.keys()[-1]) + 1
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.budget = budget
        self.log_status = False
        USERS[id] = {"name": name, "lastname": lastname, "password": password}

    def to_check_user_login(method):
        def wrapper(self, *args, **kwargs):
            if self.log_status == True:
                return method(self, *args, **kwargs)
            return print("El usuario no esta loggeado y no se puede realizar la accion")

        return wrapper

    def login(self, id: int, password: str):
        if id in USERS:
            if password == USERS[id]["password"]:
                self.log_status = True
                return print("Ha iniciado sesion correctamente")
            else:
                return print("La password para el identificador indicado no coincide")
        return print("El identificador indicado no existe")

    def logout(self):
        self.log_status == False
        return print("Se ha cerrado la sesion correctamente")

    @to_check_user_login
    def remove_user(self):
        del USERS[self.id]
        return print("Se ha eliminado correctamente el usuario")

    @to_check_user_login
    def mod_user(self, option: str, value_to_change):
        if isinstance(value_to_change, str):
            match option.upper():
                case "N":
                    self.name = value_to_change
                    USERS[self.id]["name"] = value_to_change
                case "L":
                    self.lastname = value_to_change
                    USERS[self.id]["lastname"] = value_to_change
                case "E":
                    self.email = value_to_change
                    USERS[self.id]["email"] = value_to_change
                case "P":
                    self.password = value_to_change
                    USERS[self.id]["password"] = value_to_change
                    self.logout()
                case _:
                    return print("La opcion indicada no es valida")
        return print("El valor a cambiar debe ser de tipo texto(str)")

    def create_team(
        self,
        team_number: int,
        team_name: str,
        drivers_to_add: list,
        scuderias_to_add: list,
    ):
        if len(drivers_to_add) > 5:
            drivers_to_add = drivers_to_add[:5]
        if len(scuderias_to_add) > 2:
            scuderias_to_add = scuderias_to_add[:2]

        # Modificar la clase de user team para tratar pilotos individuales y que la clase User sea la que compruebe el presupuesto
        for driver in drivers_to_add:
            driver_cost = driver.market_price
            after_addition_budget = self.budget - driver_cost
            if after_addition_budget > 0:
                UserTeam(
                    team_number, self.id, team_name, drivers_to_add, scuderias_to_add
                )
                self.budget = after_addition_budget
            else:
                return print(
                    "No hay dinero suficiente para realizar el fichaje solicitado"
                )


class Driver:
    def __init__(
        self,
        number: int,
        name: str,
        lastname: str,
        country: str,
        scuderia: str,
        market_price: int,
    ):
        self.number = number
        self.name = name
        self.lastname = lastname
        self.country = country
        self.scuderia = scuderia
        self.market_price = market_price
        self.points = 0
        DRIVERS[number] = {
            "name": name,
            "lastname": lastname,
            "country": country,
            "scuderia": scuderia,
            "points": 0,
        }

    def add_points(self, earned_points: int):
        self.points += earned_points
        DRIVERS[self.number]["points"] += earned_points

    def change_scuderia(self, new_scuderia: str, replaced_driver_car: int):
        self.scuderia = new_scuderia
        DRIVERS[self.number]["scuderia"] = new_scuderia

    def change_number(self, new_number: int):
        if new_number not in DRIVERS:
            DRIVERS[self.number] = new_number
            self.number = new_number
        return print("El numero ya esta ocupado por otro piloto")

    def retire_driver(self):
        del DRIVERS[self.number]

    def modify_market_price(self, new_market_price):
        self.market_price = new_market_price


class Scuderia:
    def __init__(
        self,
        name: str,
        country: str,
        engine_manufacturer: str,
        drivers: dict,
    ):
        self.name = name
        self.country = country
        self.engine_manufacturer = engine_manufacturer
        self.drivers = drivers
        self.points = 0
        SCUDERIAS[name] = {1: drivers[0], 2: drivers[1], "points": self.points}

    def change_drivers_lineup(self):
        SCUDERIAS[self.name][1], SCUDERIAS[self.name][2] = (
            SCUDERIAS[self.name][2],
            SCUDERIAS[self.name][1],
        )
        self.drivers[0], self.drivers[1] = self.drivers[1], self.drivers[0]
        return print("Se han intercambiado los coches de los pilotos")

    def fire_driver(self, driver_number: int):
        if SCUDERIAS[self.name][1] == driver_number:
            del SCUDERIAS[self.name][1]
            return print("Se ha despedido correctamente al piloto con el coche 1")
        elif SCUDERIAS[self.name][2] == driver_number:
            del SCUDERIAS[self.name][2]
            return print("Se ha despedido correctamente al piloto con el coche 2")
        else:
            return print("El piloto indicado no esta en la escuderia")

    def hire_driver(self, assigned_car: int, driver_number: int):
        if driver_number in DRIVERS:
            self.drivers.append(driver_number)
            SCUDERIAS[self.name][assigned_car] = driver_number
            return print("Se ha contratado correctamente al piloto")
        return "El piloto indicado no esta registrado y no se puede contratar"


class UserTeam:
    def __init__(
        self,
        number_of_team: int,
        user_id: int,
        team_name: str,
        drivers: list,
        scuderias: list,
    ):
        self.team_id = float(f"{user_id}.{number_of_team}")
        self.user_id = user_id
        self.team_name = team_name
        self.drivers = drivers
        self.scuderias = scuderias
        self.points = 0
        USERS_TEAMS[self.team_id] = {
            "user": user_id,
            "name": team_name,
            "drivers": drivers,
            "scuderias": scuderias,
            "points": 0,
        }

    def to_check_full_drivers(method):
        def wrapper(self, *args, **kwargs):
            if len(self.drivers) < 5:
                return method(self, *args, **kwargs)
            return print("Ya tienes 5 pilotos")

        return wrapper

    def to_check_full_scuderia(method):
        def wrapper(self, *args, **kwargs):
            if len(self.scuderias) < 2:
                return method(self, *args, **kwargs)
            return print("Ya tienes 2 escuderias")

        return wrapper

    @to_check_full_drivers
    def add_driver(self, driver_number: str):
        self.drivers.append(driver_number)
        USERS_TEAMS[self.team_id]["drivers"].append(driver_number)
        return print("Piloto escogido con exito")

    @to_check_full_scuderia
    def add_scuderia(self, scuderia_name: str):
        self.scuderias.append(scuderia_name)
        USERS_TEAMS[self.team_id]["scuderias"].append(scuderia_name)
        return print("Piloto escogido con exito")

    def delete_driver(self, driver_to_delete: int):
        self.drivers.remove(driver_to_delete)
        USERS_TEAMS[self.team_id]["drivers"].remove(driver_to_delete)

    def delete_scuderia(self, scuderia_to_delete: str):
        self.scuderias.remove(scuderia_to_delete)
        USERS_TEAMS[self.team_id]["scuderias"].remove(scuderia_to_delete)


class Race:
    def __init__(self, race_id: int, race_name: str, country: str, race_format: str):
        self.race_id = race_id
        self.race_name = race_name
        self.country = country
        self.race_format = race_format
        RACE_CALENDAR[race_id] = {
            "name": race_name,
            "country": country,
            "format": race_format,
        }


""" User2 = User(2, "Alonso", "Perez", "alonso@gmail.com", "123ALonso")
User2.login(2, "123ALonso")
User2.mod_user("n", "Pepe")
print(USERS)
User1 = User(1, "Pepe", "Lopez", "pepelopez@gmail.com", "123PEpe")
User2 = User(2, "Alonso", "Perez", "alonso@gmail.com", "123ALonso")
User2.login(2, "123ALonso")
User2.remove_user()
print(User1.id)
print(User1.name)
print(User1.lastname)
print(User1.email)
print(User1.password)
User1.login(3, "12322PEpe")
User1.remove_user(1, "123PEpe")
print(USERS)
 """
