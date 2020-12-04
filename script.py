import yaml
import logging
import os

def readConfig(configFile):
    logging.info('Read configuartion from: ' + str(configFile))
    with open(configFile) as file:
        conf = yaml.full_load(file)
    logging.debug(conf)
    return conf

def installApps(pacman, apps):
    if pacman == 'apt':
        os.system("sudo apt-get update")
        command = "sudo apt-get install {app} {flags}"
        for app in apps:
            logging.info('Install app: ' + str(app))
            os.system(command.format(app=app,flags="-y"))
        os.system("sudo apt-get autoremove")
    else:
        logging.error("Not supported packet manager")
    

def main():
    # configure logger
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    # read configuration
    conf = readConfig("./script_config.yaml")
    # install apps
    installApps(conf["packetmanager"], conf["applications"])
  
  
main()
