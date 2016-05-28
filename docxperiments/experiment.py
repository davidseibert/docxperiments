# coding: utf-8

from . import PACKAGE_DIR, PROJECT_DIR, DATA_DIR
import os
import dirdiff

class Experiment (object):
    def __init__(self, left_name, right_name):
        self.left_name = left_name
        self.right_name = right_name
        self.exp_name = "{}_{}".format(left_name, right_name)

    @property
    def docx_paths(self):
        try:
            return self._docx_paths
        except AttributeError:
            self._docx_paths = self._configure_docx_paths()
            return self._docx_paths

    def _configure_docx_paths(self):
        return (
            self._docx_path(self.left_name),
            self._docx_path(self.right_name),
            )

    def _docx_path(self, name):
        return self._path(self._data_path(name), self._docx(name))

    def _docx(self, name):
        docx_name = "{}.docx".format(name)
        return docx_name

    def _data_path(self, name):
        return self._path(DATA_DIR, name)

    def _path(self, *args):
        return os.path.join(*args)

    @property
    def exp_dir_path(self):
        try:
            return self._exp_dir_path
        except AttributeError:
            self._exp_dir_path = self._configure_exp_dir_path()
            return self._exp_dir_path

    def _configure_exp_dir_path(self):
        return self._data_path(self.exp_name)

    @property
    def ugly_dir_paths(self):
        try:
            return self._ugly_dir_paths
        except AttributeError:
            self._ugly_dir_paths = self._configure_ugly_dir_paths()
            return self._ugly_dir_paths

    def _configure_ugly_dir_paths(self):
        return (
            self._ugly_dir_path(self.left_name),
            self._ugly_dir_path(self.right_name),
        )

    def _ugly_dir_path(self, name):
        return self._path(self._data_path(name), 'ugly')

    @property
    def ugly_file_paths(self):
        return (
            dirdiff.walk_dir(self.ugly_dir_paths[0]),
            dirdiff.walk_dir(self.ugly_dir_paths[1]),
        )

