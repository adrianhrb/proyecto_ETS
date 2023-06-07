USERS = {}
DRIVERS = {
    "Max Verstappen": 20_000_000,
    "Sergio Perez": 18_000_000,
    "Fernando Alonso": 15_000_000,
    "Lewis Hamilton": 12_000_000,
    "George Russell": 12_000_000,
    "Carlos Sainz": 12_000_000,
    "Charles Leclerc": 15_000_000,
    "Lance Stroll": 10_000_000,
    "Esteban Ocon": 7_000_000,
    "Pierre Gasly": 5_000_000,
    "Lando Norris": 10_000_000,
    "Nico Hulkenberg": 7_000_000,
    "Oscar Piastri": 10_000_000,
    "Valtteri Bottas": 10_000_000,
    "Yuki Tsunoda": 8_000_000,
    "Kevin Magnussen": 5_000_000,
    "Guanyu Zhou": 7_000_000,
    "Alexander Albon": 7_000_000,
    "Nyck de Vries": 5_000_000,
    "Logan Sargeant": 3_000_000,
}

CONSTRUCTORS = {
    "Red Bull": 15_000_000,
    "Mclaren": 5_000_000,
    "Aston Martin": 12_000_000,
    "Ferrari": 12_000_000,
    "Alpha Tauri": 5_000_000,
    "Alfa Romeo": 5_000_000,
    "Williams": 3_000_000,
    "Haas": 3_000_000,
    "Mercedes": 7_000_000,
    "Alpine": 7_000_000,
}

DRIVERS_RACE_RESULT = {
    "Fernando Alonso": 25,
    "Max Verstappen": 18,
    "Carlos Sainz": 15,
    "Lewis Hamilton": 13,
    "Lance Stroll": 10,
    "Charles Leclerc": 8,
    "Pierre Gasly": 6,
    "Esteban Ocon": 4,
    "Lando Norris": 2,
    "Oscar Piastri": 1,
}

CONSTRUCTORS_RACE_RESULT = {
    "Aston Martin": 35,
    "Red Bull": 18,
    "Mclaren": 3,
    "Ferrari": 23,
    "Alpha Tauri": 0,
    "Alfa Romeo": 0,
    "Williams": 0,
    "Haas": 0,
    "Mercedes": 13,
    "Alpine": 10,
}


class User:
    def __init__(
        self, id: int, username: str, password: str, budget: int = 50_000_000
    ) -> None:
        if id not in USERS.keys():
            self.id = id
        else:
            self.id = list(USERS.keys())[-1] + 1
        self.username = username
        self.password = password
        self.log_status = False
        self.budget = budget
        self.team = {"drivers": [], "constructors": []}
        self.points = 0
        USERS[self.id] = self

    def login(self, password: str):
        self.log_status = True if password == self.password else False

    def logout(self):
        self.log_status = False

    @staticmethod
    def to_check_login(method):
        def wrapper(self, *args, **kwargs):
            if self.log_status == False:
                raise LoginError(f"The user is not logged")
            return method(self, *args, **kwargs)

        return wrapper

    @to_check_login
    def buy_driver(self, driver: str):
        driver_cost = DRIVERS[driver] if driver in DRIVERS else -1
        if driver not in DRIVERS:
            return f"Driver {driver} is not racing in F1"
        if self.budget - driver_cost < 0:
            return f"Not enough budget to buy the driver"
        if len(self.team["drivers"]) >= 5:
            return f"Drivers lineup is full"
        if driver in self.team["drivers"]:
            return "Driver is already in your team"
        self.team["drivers"].append(driver)
        self.budget -= driver_cost
        return self.team["drivers"]

    @to_check_login
    def buy_constructor(self, constructor: str):
        constructor_cost = (
            CONSTRUCTORS[constructor] if constructor in CONSTRUCTORS else -1
        )
        if constructor not in CONSTRUCTORS:
            return f"Constructor {constructor} is not racing in F1"
        if self.budget - constructor_cost < 0:
            return f"Not enough budget to buy the driver"
        if len(self.team["constructors"]) >= 2:
            return f"Constructors lineup is full"
        if constructor in self.team["constructors"]:
            return "Driver is already in your team"
        self.team["constructors"].append(constructor)
        self.budget -= constructor_cost
        return self.team["constructors"]

    @to_check_login
    def sell(self, item: str):
        if item in self.team["drivers"]:
            self.team["drivers"].remove(item)
            self.budget += DRIVERS[item]
        if item in self.team["constructors"]:
            self.team["constructors"].remove(item)
            self.budget += CONSTRUCTORS[item]
        return f"{item} sold correctly"

    @to_check_login
    def mod_user_info(self, option: str, new_data: str):
        match option:
            case "U":
                self.username = new_data
            case "P":
                self.password = new_data
                self.log_status = False

    def update_points(self, drivers_race_result: dict, constructors_race_result: dict):
        for driver in self.team["drivers"]:
            if driver in drivers_race_result:
                self.points += drivers_race_result[driver]

        for constructor in self.team["constructors"]:
            if constructor in constructors_race_result:
                self.points += constructors_race_result[constructor]


class LoginError(Exception):
    pass


user1 = User(1, "pepe", "1234")
print(user1.budget)
user1.login("1234")
print(user1.buy_driver("Lance Stroll"))
print(user1.buy_driver("Charles Leclerc"))
print(user1.budget)
print(user1.buy_constructor("Aston Martin"))
print(user1.budget)
print(user1.team)
user1.sell("JKDFKJHSD")
print(user1.team)
print(user1.budget)
user2 = User(1, "pepe", "1234")
print(USERS[1].username)
user1.mod_user_info("U", "pepenuevonombre")
print(USERS[1].username)
user1.update_points(DRIVERS_RACE_RESULT, CONSTRUCTORS_RACE_RESULT)
print(user1.points)
