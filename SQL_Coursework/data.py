import pandas as pd
import random
import faker

customer_csv = pd.read_csv("datasets/customer.csv")
name = pd.read_csv("datasets/NationalNames.csv")
address = pd.read_csv("datasets/list_of_real_usa_addresses.csv")
brand = pd.read_csv("datasets/brand.csv")
product = pd.read_csv("datasets/BigBasketProducts.csv")


def get_address():
    while True:
        addressout = fake.address()
        if len(addressout) <= 44:
            return addressout


def get_u_name(numIn):
    str1 = str(name.iat[numIn % 1800000, 1])

    # print(str1)
    return str1


fake = faker.Faker()


def get_s_name(numIn):
    return brand.iat[numIn % 500, 0]


def get_p_url():
    return fake.lexify(text='https://????????????/???.png')


def get_s_category():
    return product.iat[random.randint(0, 2000), 2]


def get_p_name(numIn):
    str_out =  product.iat[numIn, 1]
    return str_out[0:44]


def get_p_category(numIn):
    return product.iat[numIn, 2]

def get_l_state():
    state = ["Collected","in transit","signed"]
    return state[random.randint(0,2)]

def get_l_time():
    return fake.date_time_this_decade()

def get_l_inc():
    index1 = random.randint(0,5)
    compane = ["UPS","Deutsche Post","FedEx","C. H. Robinson","XPO Logistics","J.B. Hunt"]
    return compane[index1]

