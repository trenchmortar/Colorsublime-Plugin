import os
import shutil
import json
from zipfile import ZipFile
from tempfile import SpooledTemporaryFile

from . import logger
log = logger.get(__name__)


def _ensure_folder_exists(abs_path):
    try:
        os.makedirs(abs_path)
    except os.error:
        # Directory already exists.
        pass


def extract(archive_bytes, extract_path):
    log.debug('Extracting archive to ' + extract_path)
    _ensure_folder_exists(extract_path)
    with SpooledTemporaryFile() as temp:
        temp.write(archive_bytes)
        data = ZipFile(temp, mode='r')
        data.extractall(extract_path)
        data.close()


def read_json(path):
    try:  # Python 3
        with open(path, encoding='utf-8') as data:
            return json.loads(data.read())
    except TypeError:  # Python 2
        import codecs
        f = codecs.open(path, encoding='utf-8')
        data = json.loads(f.read())
        f.close()
        return data



def copy(from_path, to_path):
    shutil.copy(from_path, to_path)
