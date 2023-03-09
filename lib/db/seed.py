from random import random, randint, choice 

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Location, Restaurant, IftarTable

engine = create_engine('sqlite:///iftar.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()


#make Users
# def make_users():
#     print("Deleting existing users...")
#     session.query(User).delete()
#     session.commit()

#     print("Making users...")
#     users = []
#     while True:
#         full_name = input("Enter your full name (or press q to quit): ")
#         if full_name == "q":
#             break
#         city = input("Enter your city: ")
#         state = input("Enter the state your city is in: ")
#         location = session.query(Location).filter_by(city=city, state=state).first()
#         if location is None:
#             print(f"Sorry, we couldn't find a location matching {city}, {state}")
#             continue
#         iftar_time = location.iftar_time
#         print(f"Your iftar time is: {iftar_time}")
#     session.add_all(users)
#     session.commit()
        
#make Location
def make_location():
    print("Deleting existing locations...")
    session.query(Location).delete()
    session.commit()

    print("Making locations...")
    # locations = [
    #     Location(city='Los Angeles', state='California', restaurant_locations = 1, iftar_time = 1),
    #     # Location(city='New York', state='New York', iftar_time='6:45 PM'),
    #     # Location(city='Houston', state='Texas', iftar_time='7:20 PM'),
    #     # Location(city='Chicago', state='Illinois', iftar_time='6:50 PM'),
    #     # Location(city='Miami', state='Florida', iftar_time='7:30 PM'),
    # ]

    locations = Location(city='Los Angeles', state='California', restaurant_locations = 1, iftar_time = 1)

    session.add(locations)
    session.commit()

    # return locations

#make Restaurant
def make_restaurant():
    print("Deleting existing restaurants...")
    session.query(Restaurant).delete()
    session.commit()

    print("Making Restaurant...")
    restaurants = [
        Restaurant(name='Halal Guys', city='Los Angeles', menu='gyro'),
        Restaurant(name='Pita Inn', city='Chicago', menu='shawarma'),
        Restaurant(name='Cava', city='New York', menu='bowl'),
        Restaurant(name='Zabak\'s Mediterranean Cafe', city='Houston', menu='platter'),
        Restaurant(name='Zaatar Mediterranean Cuisine', city='Miami', menu='hummus'),
        Restaurant(name='Rumi\'s Kitchen', city='Atlanta', menu='kebab'),
        Restaurant(name='Naya Express', city='New York', menu='pita'),
        Restaurant(name='Taste of Persia', city='New York', menu='joojeh'),
    ]
    
    session.add_all(restaurants)
    session.commit()

    return restaurants


#make IftarTable
def make_iftartable():
    print("Deleting existing iftar tables...")
    session.query(IftarTable).delete()
    session.commit()

    print("Making iftar tables...")
    iftar_tables = [
        IftarTable(state='California', iftar_time='7:10 PM'),
        IftarTable(state='New York', iftar_time='6:45 PM'),
        IftarTable(state='Texas', iftar_time='7:20 PM'),
        IftarTable(state='Illinois', iftar_time='6:50 PM'),
        IftarTable(state='Florida', iftar_time='7:30 PM'),
    ]
    
    session.add_all(iftar_tables)
    session.commit()

if __name__ == '__main__':
    # make_users()
    make_restaurant()
    make_location()
    make_iftartable()






