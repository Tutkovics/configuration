import yaml
import logging

def readConfig(configFile):
    logging.info('Read configuartion from: ' + str(configFile))
    with open(configFile) as file:
        conf = yaml.full_load(file)
    logging.debug(conf)
    return conf

def main():
    # configure logger
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    # read configuration
    conf = readConfig("./script_config.yaml")
    # install apps
    installApps(conf["applications"])
  
  
main()
