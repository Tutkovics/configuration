import yaml
import logging
import os

def pyInit():
    os.System("sudo pip3 install pyyaml")

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
            if os.system("apt-cache show {app}".format(app=app)) == 0:
                logging.info('Install app: ' + str(app))
                os.system(command.format(app=app,flags="-y"))
            else:
                logging.warning("App: {app} not found!".format(app=app))
        os.system("sudo apt-get autoremove")
    else:
        logging.error("Not supported packet manager")
    
def removeApps(pacman, apps):
    if pacman == 'apt':
        os.system("sudo apt-get update")
        command = "sudo apt-get remove {app} {flags}"
        for app in apps:
            if os.system("apt-cache show {app}".format(app=app)) == 0:
                logging.info('Remove app: ' + str(app))
                os.system(command.format(app=app,flags="-y"))
            else:
                logging.warning("App: {app} not found!".format(app=app))
        os.system("sudo apt-get autoremove")
    else:
        logging.error("Not supported packet manager")

def main():
    # configure logger
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    # init python environment
    pyInit()
    # read configuration
    conf = readConfig("./script_config.yaml")
    # install apps
    #installApps(conf["packetmanager"], conf["applications"])
    # remove apps
    removeApps(conf["packetmanager"], conf["applications"])
  
  
main()
