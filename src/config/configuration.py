import yaml


class Configuration:
    _CONFIG_FILE = "config.yaml"
    _config = {}

    def __init__(self):
        with open(self._CONFIG_FILE) as configuration:
            _config = yaml.safe_load(configuration)
            configuration.close()

    def get_batch_config(self):
        return self._config["batch"]

    def get_target_config(self):
        return self._config["target"]
