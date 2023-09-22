import importlib
import socket
import threading
import json
import os
import importlib.util

class ModuleUpdater:
    def __init__(self, module_directory=None):
        if module_directory:
            self.module_directory = module_directory
            self.modules = self.load_modules_from_directory()
        else:
            self.modules = {
                'main': 'main.py',
                'ues': 'ues.py',
                'world': 'world.py',
                'gameplay_mechanics': 'GameplayMechanicsModule.py',
                'ui': 'ui.py',
                'graphics': 'graphics.py'
                'multiplayer.py'
            }

    def load_modules_from_directory(self):
        modules = {}
        for filename in os.listdir(self.module_directory):
            if filename.endswith('.py'):
                module_name = filename[:-3]
                modules[module_name] = os.path.join(self.module_directory, filename)
        return modules

    def update_module(self, module_name, update_function, *args, **kwargs):
        if module_name in self.modules:
            module_path = self.modules[module_name]
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        
        # Get the function object from the module
            func = getattr(module, update_function, None)
        
            if func and callable(func):
            # Call the update function
                func(*args, **kwargs)
            
            # Save the updated module
                self.save_module(module_name, module)
            
            # Reload the module to apply changes
                importlib.reload(module)
            else:
                print(f"Function {update_function} not found in module {module_name}.")
        else:
            print(f"Module {module_name} not found.")



    def save_module(self, module_name, module):
        module_code = """
        # Your updated code here
        """
        with open(self.modules[module_name], 'w') as f:
            f.write(module_code)

    def update_graphics(self, *args, **kwargs):
        self.update_module('graphics', 'generate_world', *args, **kwargs)

if __name__ == "__main__":
    module_directory = "D:\Prototype\Modules"  # Replace with your actual module directory
    module_updater = ModuleUpdater(module_directory)

    while True:
        print("Available modules:", list(module_updater.modules.keys()))
        module_name = input("Enter the module name to update: ")
        update_function = input("Enter the update function to call: ")

        if module_name in module_updater.modules:
            module_updater.update_module(module_name, update_function)
            print(f"{module_name} has been updated.")
        else:
            print("Invalid module name.")
