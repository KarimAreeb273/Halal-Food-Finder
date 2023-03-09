from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User, Location, Restaurant, IftarTable

from helpers import (create_restaurant_table, create_location_table, create_menu_table)

from db.seed import make_restaurant

engine = create_engine('sqlite:///iftar.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    # print('Welcome to the Iftar Food Finder')

    # print('These are the possible options for Cities:')
    # locations = session.query(Location)
    # create_location_table(locations)

    # print("Enter your name and city to search for restaurants:")
    name = input("Name: ")
    # city = input("City: ")
    user = User(full_name=name)
    session.add(user)
    session.commit()
    
    state = input("Enter the state your city is in: ")

    # print ("Here are the restaurants in your city:")
    # restaurants = session.query(Restaurant)
    # create_restaurant_table(restaurants)

    # restaurant_choice = input("Choose a restaurant: ")
    # print("Okay here is the menu for that restaurant: ")
    
    # create_menu_table(restaurants)

    iftar_time = session.query(IftarTable).filter_by(state=state).first()
    print(f"Your iftar time is: {iftar_time}")
    

    # restaurants = make_restaurant()
    # print(f"Here are the restaurants in your city: ")
    # for restaurant in restaurants:
    #     print(restaurant.name)

