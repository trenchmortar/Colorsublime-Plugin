import os
import shutil

from . import settings


def _ensure_folder_exists(abs_path):
    if not os.path.exists(abs_path):
        os.makedirs(abs_path)


def install_theme(theme):
    install_dir = settings.get_install_path()
    _ensure_folder_exists(install_dir)
    install_path = install_dir + '/' + theme.file_name

    shutil.copy(theme.file_path, install_path, follow_symlinks=True)

    return install_path


def get_theme_path(file_name):
    _ensure_folder_exists(settings.get_themes_abs())
    themes_dir = settings.get_themes_abs()
    p = os.path.join(themes_dir, file_name)
    if os.path.exists(p):
        return settings.get_themes_rel() + '/' + file_name
    return None
