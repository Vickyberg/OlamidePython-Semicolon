customers = [
    {
        "name": "Omotola Fashola",
        "acct_num": "001",
        "age": 24,
        "balance": 10_000,
        "type": "savings",
        "gender": "female",
        "is_married": False
    },
    {
        "name": "Idiot Z eddy",
        "acct_num": "010",
        "age": 32,
        "balance": 1_005,
        "type": "current",
        "gender": "male",
        "is_married": True
    },
    {
        "name": "Ololade Boyo",
        "acct_num": "031",
        "age": 18,
        "balance": 34_000,
        "type": "savings",
        "gender": "female",
        "is_married": False
    },
    {
        "name": "Dorcas Charles",
        "acct_num": "011",
        "age": 22,
        "balance": 12_000,
        "type": "savings",
        "gender": "female",
        "is_married": False
    },
    {
        "name": "Emmanuel Obsession",
        "acct_num": "092",
        "age": 76,
        "balance": 1_000_000,
        "type": "current",
        "gender": "male",
        "is_married": True
    },
    {
        "name": "Eden Ace",
        "acct_num": "021",
        "age": 27,
        "balance": 2_000,
        "type": "savings",
        "gender": "female",
        "is_married": True
    },
    {
        "name": "Odogwu Buga",
        "acct_num": "022",
        "age": 32,
        "balance": 13_000,
        "type": "current",
        "gender": "male",
        "is_married": True
    }

]
names = [customer["name"] for customer in customers]
avg_age = sum(customer["age"] for customer in customers) / len(customers)
savings_acct_holders = [dict(name=c["name"], balance=c["balance"]) for c in customers if c["type"] == "savings"]
print("NAMES OF CUSTOMERS")
print(names)
print("AVERAGE")
print("Average age of all the customers: ", avg_age)
print("CUSTOMERS WITH SAVINGS ACCOUNT")
print(savings_acct_holders)


def get_balance(dict_: dict) -> int:
    return dict_["balance"]


customers.sort(key=get_balance, reverse=True)
print()
print(customers)
