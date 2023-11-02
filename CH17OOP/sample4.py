"""
Computer class
    Laptop
    Tablet
    Smartphone
"""
class Processor:
    pass
class Intel:
    pass
class M1:
    pass
class M2:
    pass
class AMD:
    pass

class Computer:
    processor_type = Processor
    def __init__(self, memory, storage, os):
        self.memory = memory
        self.storage = storage
        self.os = os
        
    def boot(self):
        print(f"Starting {self.__class__.__name__}...")
        print(f"Running {self.processor_type.__name__}...")
class Laptop(Computer):
    Processor_type = Intel
    def __init__(self, memory, storage, os, name):
        super().__init__(memory, storage, os)
        self.name = name
        
    def boot(self):
        print(f"running {self.processor_type.__name__}  processor on {self.name}")
    
    
class Tablet(Computer):
    Processor_type = M1
    def __init__(self, memory, storage, os, name):
        super().__init__(memory, storage, os)
        self.name = name
        
    def boot(self):
        print(f"running {self.processor_type.__name__}  processor on {self.name}")
        
        
class Smartphone(Computer):
    processor_type = M2

    def __init__(self, memory, storage, os, name):
        super().__init__(memory, storage, os)
        self.name = name
        
    def boot(self):
        print(f"running {self.processor_type.__name__}  processor on {self.name}")
        
computer = Computer(memory=32, storage=128, os="windows")
computer.boot()

macBook = Laptop(memory=32, storage=128, os="MacOS", name="Macbook Pro")
macBook.boot()

iPad = Tablet(memory=4, storage=64, os="IOS", name="Ipad")
iPad.boot()

iPhone = Smartphone(memory=3, storage=64, os="IOS", name="iPhone")
iPhone.boot()

print(isinstance(iPhone, Smartphone))
print(isinstance(iPad, Smartphone))
print(issubclass(Smartphone, Computer))


