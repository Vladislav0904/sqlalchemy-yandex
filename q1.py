db = input()
global_init(db)
db_sess = create_session()
user = db_sess.query(User).filter(User.address == 'module_1').all()
for i in user:
    print(i)
