import configparser

DEFAULT = "/Serialization/"
path = "test.ini"

# Created and save a configuration file
config = configparser.ConfigParser()
config['DEFAULT'] = {'IP' : '127.0.0.1',
                     'PORT': '93',
                     'Weight' : 'C:\Projects\TTVisionAI\DLPythonScript/best_dataset2.pt'}
config['testing.org'] = {}
config['testing.org']['User'] = 'Hadi'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['AI'] = 'smart'     # mutates the parser
topsecret['success'] = 'no'  # same here
topsecret['ForwardX11'] = 'no'
config['DEFAULT']['default_message'] = 'Hey! help me!!'   # create
config['DEFAULT']['pathFile'] = 'C:\Projects\TTVisionAI\DLPythonScript'   # create

#create a new ini file
with open('Serialization/example.ini', 'w') as configfile:
    config.write(configfile)
    
config.read('test.ini')
print(config['DEFAULT']['pathFile'])
# print(config['DEFAULT']['test.ini'])     # -> "/path/name/"
# config['DEFAULT']['path'] = '/var/shared/'    # update
# config['DEFAULT']['default_message'] = 'Hey! help me!!'   # create

# with open('FILE.INI', 'w') as configfile:    # save
#     config.write(configfile)
    
# Config parser
# class MyParser(configparser.ConfigParser.ConfigParser):
    
#     def as_dict(self):
#         d = dict(self.sections)
#         for k in d:
#             d[k] = dict(self.defaults, **d[k])
#             d[k].pop(')