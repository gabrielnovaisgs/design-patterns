
class Configuration:
    instance: "Configuration | None" = None
    configs: dict[str, str]
    def __init__(self):
        self.configs = {}
        print(f'instance created!')


    @classmethod
    def get_instance(cls) -> "Configuration":
        
        if(not cls.instance):
            cls.instance = Configuration()
        return cls.instance

    
    def save_configuration(self, configs: dict[str, str]):
        self.configs = configs
        print("configurations saved!")
    
    def show_configs(self):
        print(f'System configurations: {[f'{config}: {self.configs[config]}' for config in self.configs]}')


obj1 = Configuration.get_instance()
obj2 = Configuration.get_instance()

obj1.save_configuration({
    "dark": 'true',
    'zoom': "5x"
})

obj2.show_configs()
