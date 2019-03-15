import configparser
from collections import deque
import io

#Module for working with config-like files

#module attributes
attributes = {"Name":"config",
              "Type":"lib",
              "Description":"File I/O module"}

class ConfigFileIO:
    """Base class for file read/write."""
    
    def __init__(self, filename):
        """Open/create file."""
        
        self.filename = filename
        self.config = configparser.ConfigParser(allow_no_value=True)
        try:
            io.open(self.filename, 'r', encoding='utf16')
        except FileNotFoundError:
            f = io.open(self.filename, 'w', encoding='utf16')

    def write(self, section, key, value):
        """Write value in file"""
        
        f = io.open(self.filename, 'r', encoding='utf16')
        self.config.read_file(f)
        f.close()
        if section in self.config:
            self.config[section][key] = str(value)
        else:
            self.config[section] = {key:str(value)}
        f = io.open(self.filename, 'w', encoding='utf16')
        self.config.write(f)
        f.close()

    def read(self, section, key):
        """Read value of key in section. Return value or None if failed."""
        
        f = io.open(self.filename, 'r', encoding='utf16')
        self.config.read_file(f)
        f.close()
        if section in self.config:
            if key in self.config[section]:
                return self.config[section][key]
        return None

    def init_setup(self):
        """Create missing CONFIG entries"""
        f = io.open(self.filename, 'r', encoding='utf16')
        self.config.read_file(f)
        f.close()
        if 'CONFIG' in self.config:
            if 'token' not in self.config['CONFIG']:
                self.config['CONFIG']['token'] = ''
            if 'bot' not in self.config['CONFIG']:
                self.config['CONFIG']['bot'] = 'True'
        else:
            self.config['CONFIG'] = {'token': 'put_token_here',
                                     'bot': 'True'}
        f = io.open(self.filename, 'w', encoding='utf16')
        self.config.write(f)
        f.close()

class NamesConfig(ConfigFileIO):
    """Class for managing nicks/names for `names command."""
    
    def __init__(self, filename):
        super().__init__(filename)
        
    def write_name(self, uid, name):
        """Format names and write to memory file."""
        
        record = deque(self.read('Names', uid).split('\n'))
        if list(record) == ['']:
            record.clear()
        record.append(name)
        if len(record) > 20:
            record.popleft()
        self.write('Names', uid, '\n'.join(record))

    def write_nick(self, uid, nick):
        """Format nick and write to memory file."""
        
        record = deque(self.read('Nicks', uid).split('\n'))
        if list(record) == ['']:
            record.clear()
        record.append(nick)
        if len(record) > 20:
            record.popleft()
        self.write('Nicks', uid, '\n'.join(record))

class SettingsConfig(ConfigFileIO):
    """Class for managing settings like channel IDs and whatnot."""

    def __init__(self, filename):
        super().__init__(filename)

    def read_setting(self, key):
        """Read [SETTINGS][key] and format into list. Return list."""
        record = list(self.read('SETTINGS',key).split('|'))
        if record == ['']:
            record.clear()
        return record
