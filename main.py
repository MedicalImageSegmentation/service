import glob
import importlib
import os

import uvicorn

from config.config import settings
from core import app
from core.app import App

service_file = glob.glob('services/*.py')

if __name__ == '__main__':
    app.instance = App()

    for file in service_file:
        module_name = file[:-3].replace(os.sep, '.')
        module = importlib.import_module(module_name)

    uvicorn.run(app=app.instance.http,
                host="0.0.0.0",
                port=8000,
                )
