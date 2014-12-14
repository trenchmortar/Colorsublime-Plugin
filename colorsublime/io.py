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
        with ZipFile(temp, mode='r') as data:
            data.extractall(extract_path)


def read_json(path):
    with open(path, encoding='utf-8') as data:
        return json.loads(data.read())


def copy(from_path, to_path):
    shutil.copy(from_path, to_path)
