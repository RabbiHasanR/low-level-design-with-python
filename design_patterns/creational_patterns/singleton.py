
# 1. Eager Initialization Singleton
# Example: Database Configuration Manager
# In this example, the DatabaseConfigManager is a singleton that manages database configuration settings. The instance is created eagerly when the class is loaded.

class DatabaseConfigManager:
    
    _instance = None
    
    def __init__(self) -> None:
        if DatabaseConfigManager._instance is not None:
            raise Exception("This class is singleton")
        self.config = self._load_config()
        
    
    def _load_config(self):
        return {"host": "localhost", "port": 5432, "user": "admin", "password": "secret"}
    
    def get_config(self):
        return self.config
    
    
    @staticmethod
    def get_instance():
        return DatabaseConfigManager._instance
    
# Eagerly initialize the singleton instance
DatabaseConfigManager._instance = DatabaseConfigManager()

# usage
db_config_manager = DatabaseConfigManager.get_instance()
print(db_config_manager.get_config())  # Output: {'host': 'localhost', 'port': 5432, 'user': 'admin', 'password': 'secret'}



# 2. Lazy Initialization Singleton
# Example: Logger
# In this example, the Logger is a singleton that logs messages to a file. The instance is created only when it is needed for the first time (lazy initialization).

class Logger:
    _instance = None
    
    def __init__(self) -> None:
        if Logger._instance is not None:
            raise Exception("This class is a singleton!")
        self.log_file = self._open_log_file()
        
    def _open_log_file(self):
        return open('logfile.txt', 'a')
    
    def log(self, message):
        self.log_file.write(message + "\n")
        
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Logger()
        return cls._instance
    

#usage
logger = Logger.get_instance()
logger.log("This is a log message") # Logs the message to the file




# 3. Thread-Safe Singleton
# Example: AppConfig
# In this example, AppConfig is a thread-safe singleton that stores application configuration settings. 
# The instance is lazily initialized in a thread-safe manner using a lock to ensure that only one instance is created, even when accessed by multiple threads. 

import threading

class AppConfig:
    _instance = None
    _lock = threading.Lock()
    
    def __init__(self) -> None:
        if AppConfig._instance is not None:
            raise Exception("This class is a singleton")
        self.settings = self._load_settings()
        
    
    def _load_settings(self):
        return {"theme": "dark", "language": "en", "version": "1.0"}
    
    def get_settings(self, key):
        return self.settings.get(key, None)
    
    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = AppConfig()
        return cls._instance
    
    

# usage
def access_settings():
    app_config = AppConfig.get_instance()
    print(app_config.get_settings('theme')) # output: dark
    print(app_config)
    


# Simulate concurrent access in a multithreaded environment
thread1 = threading.Thread(target=access_settings)
thread2 = threading.Thread(target=access_settings)

thread1.start()
thread2.start()

thread1.join()
thread2.join()