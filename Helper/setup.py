from distutils.core import setup
import py2exe
 
setup(
    console=['C:\Users\TigerApps\Desktop\SongDirectorySetter\Wrapper_8.py'],
    options = {
        'py2exe': {
            'packages': ['id3reader']
        }
    }
)
