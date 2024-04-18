import psycopg2 as pg2                                   #Package used to connect to PostgreSQL DB

from config import load_config                          

def connect(config):                                    
    """ Connect to the PostgreSQL database server """
    try:
        with pg2.connect(**config) as conn:             # connecting to the PostgreSQL server
            print('Connected to the PostgreSQL server.')
            return conn
    except (pg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_config()
    connect(config)