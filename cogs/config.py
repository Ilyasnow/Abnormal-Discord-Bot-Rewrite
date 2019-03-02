import configparser
from collections import deque
import io

class ConfigFileIO:
    """Base class for file read/write
    """
    
    def __init__(self, filename):
        """Open/create file
        """
        self.filename = filename
        try:
            io.open(self.filename, 'r', encoding='utf16')
        except FileNotFoundError:
            f = io.open(self.filename, 'w', encoding='utf16')
        self.config = configparser.ConfigParser(allow_no_value=True)

    def write(self, section, key, value):
        """Write value in file
        """
        f = io.open(self.filename, 'r', encoding='utf16')
        self.config.read_file(f)
        f.close()
        if section in config:
            config[section][key] = str(value)
        else:
            config[section] = {key:str(value)}
        f = io.open(self.filename, 'w', encoding='utf16')
        self.config.write(f)
        f.close()

    def read(self, section, key):
        """Read value of key in section. Return value or None if failed.
        """
        f = io.open(self.filename, 'r', encoding='utf16')
        self.config.read_file(f)
        f.close()
        if section in config:
            if key in config[section]:
                return config[section][key]
        return ''

class NamesConfig(ConfigFileIO):
    """Class for managing nicks/names for `names command
    """
    
    def __init__(self, filename):
        super().__init__(self, filename)
        
    def write_name(uid, name):
        """Format names and write to memory file
        """
        f = io.open(self.filename, 'r', encoding='utf16')
        self.config.read_file(f)
        f.close()
        record = deque(self.read('Names', uid).split('\n'))
        if list(record) == ['']:
            record.clear()
        record.append(name)
        if len(record) > 20:
            record.popleft()
        self.write('Names', uid, '\n'.join(record))

    def write_nick(uid, nick):
        """Format nick and write to memory file
        """
        f = io.open(self.filename, 'r', encoding='utf16')
        self.config.read_file(f)
        f.close()
        record = deque(self.read('Nicks', uid).split('\n'))
        if list(record) == ['']:
            record.clear()
        record.append(nick)
        if len(record) > 20:
            record.popleft()
        self.write('Nicks', uid, '\n'.join(record))
