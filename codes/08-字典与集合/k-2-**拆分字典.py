base_config = {"host": "localhost", "port": 8080}
extra_config = {"port": 9000, "debug": True}

full_config = {**base_config, **extra_config}
print(full_config)
