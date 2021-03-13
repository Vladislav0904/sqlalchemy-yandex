from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.speciality = 'research engineer'
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user1 = User()
    user1.name = "Curt"
    user1.surname = "Cobain"
    user1.age = 27
    user1.speciality = 'doctor'
    user1.address = "forest_lawn"
    user1.email = "cobain_curt@mars.org"
    user2 = User()
    user2.name = "Elon"
    user2.surname = "Musk"
    user2.age = 21
    user2.speciality = 'Space X engineer'
    user2.address = "module_mars"
    user2.email = "elon_musk@spacex.org"
    user3 = User()
    user3.name = "Marshall"
    user3.surname = "Mathers"
    user3.age = 49
    user3.speciality = 'professional battle rapper'
    user3.address = "module_3"
    user3.email = "beard_is_weirdf@shady.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()