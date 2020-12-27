import bcrypt
import configparser


def gen_write(cfig, pth, ste, un2, pw2):
    pw3 = bcrypt.hashpw(pw2, bcrypt.gensalt())
    config.add_section(ste)
    cfig.set(str(ste), "Username", str(un2))
    cfig.set(str(ste), "Password", pw3.decode('utf8'))
    with open(pth, 'w') as config_file:
        cfig.write(config_file)


def check_pw(cfig2, ste2, pw2):
    db = dict(cfig2.items(ste2))
    print(db['password'])
    print(type(db['password']))
    if bcrypt.checkpw(pw2, db['password'].encode('utf8')):
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    config = configparser.ConfigParser()
    path = "test.ini"
    config.read(path)
    site = input("Enter site: ")
#    un = input("Enter username: ")
    pw = input("Enter password: ").encode('utf8')
#    gen_write(config, path, site, un, pw)
    check_pw(config, site, pw)
    print("Success!")
