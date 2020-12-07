from setuptools import setup
# import os

# driver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver')

# driver_path = './chromedriver'  # path of your chromedriver

APP = ['yosuniiiii_insta_GUI.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation' : True,
}

setup(
    app=APP,
    # data_file=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)