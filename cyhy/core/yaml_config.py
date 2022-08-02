import sys
import yaml
import logging

# import IPython; IPython.embed() #<<< BREAKPOINT >>>


class YamlConfig:

    SUPPORTED_VERSIONS = ["1"]

    VERSION = "version"
    DEFAULT = "default"
    CORE = "core"
    MONGO = "mongo"
    REDIS = "redis"

    def __init__(self, config_filename=None):
        if not isinstance(config_filename, basestring):
            raise ValueError("Configuration filename must be a string.")
        self.logger = logging.getLogger(__name__)
        self.config_filename = config_filename
        self.config = self.__load_config()

    def get(self, key=None):
        try:
            if not isinstance(key, basestring):
                raise ValueError("Key must be a string.")
            return self.config[key]
        except ValueError as e:
            self.logger.exception(e)
            raise

    def get_service(self, service=None, section=None):
        try:
            if not isinstance(service, basestring):
                raise ValueError("Service must be a string.")

            if section is None:
                section = YamlConfig.DEFAULT
            elif not isinstance(section, basestring):
                raise ValueError("Section must be a string.")
            elif section not in self.config[service]:
                raise KeyError(f'Section "{section}" not found in service {service}')
            return self.config[service][section]
        except (KeyError, ValueError) as e:
            self.logger.exception(e)
            raise

    def __load_config(self):
        try:
            self.logger.info(
                "Loading configuration from {!s}".format(self.config_filename)
            )
            with open(self.config_filename, "r") as stream:
                # The loader must now be explicitly specified to avoid
                # a warning message.  See here for more details:
                # https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
                config = yaml.load(stream, Loader=yaml.FullLoader)

                if YamlConfig.VERSION not in config:
                    raise KeyError(
                        'Required configuration field "version" missing. '
                        "Please check your configuration file."
                    )
                elif config[YamlConfig.VERSION] not in YamlConfig.SUPPORTED_VERSIONS:
                    raise ValueError(
                        f"Configuration version {config[YamlConfig.VERSION]} not supported.\n  Please use one of the following versions: {YamlConfig.SUPPORTED_VERSIONS}."
                    )

                return config
        except (IOError, KeyError) as e:
            self.logger.exception(e)
            raise
        except ValueError as e:
            self.logger.exception(e)
            raise
        except yaml.YAMLError as e:
            self.logger.exception(e)
            raise
