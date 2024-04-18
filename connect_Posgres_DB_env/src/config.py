
from configparser import ConfigParser

#reads database.ini
def load_config(filename='database.ini', section='postgresql'):

    parser = ConfigParser()               # Instantiate ConfigParser class to read database.ini
    parser.read(filename)                 # From the instatiated class we run the read method by passing the filename
    config = {}                           # confi is an empry dictionary or set

    if parser.has_section(section):       # test if section exists      
        params = parser.items(section)    # variable that holds the config
        for param in params:              # Loop through each line
            config[param[0]] = param[1]   #         
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config

#if __name__ == '__main__':
 #   config = load_config()
 #   print(config)