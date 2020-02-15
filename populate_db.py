from database_setup import  User, Category, Item, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///item_catalog.db',connect_args={'check_same_thread': False})

Session = sessionmaker(bind=engine)

session = Session()

first_user = User(name = "Ravi", email = "ravi.kolanpaka@gmail.com", picture = "https://png.pngtree.com/png-clipart/20190516/original/pngtree-users-vector-icon-png-image_3725294.jpg")

session.add(first_user)
session.commit()

first_category = Category(name = "Soccer", user = first_user)
session.add(first_category)
session.commit()

first_item = Item(name = "Jersey", description = "Its a Jersey for football", category = first_category, user = first_user )
session.add(first_item)
session.commit()


second_item = Item(name = "Soccer Cleats", description = "Its Soccer Cleats!!!", category = first_category, user = first_user )
session.add(second_item)
session.commit()

second_category = Category(name = "Snowboarding", user = first_user)
session.add(second_category)
session.commit()

first_item_snowboarding =   Item(name = "Goggles", description = "Its goggles for snowboarding!!!", category = second_category, user = first_user )
session.add(first_item_snowboarding)
session.commit()

second_item_snowboarding =   Item(name = "Snowboard", description = "Its snowboard for snowboarding!!!", category = second_category, user = first_user )
session.add(second_item_snowboarding)
session.commit()