# coding: utf-8

from . import PACKAGE_DIR, PROJECT_DIR, DATA_DIR
import os
from extract import extract_docx
import dirdiff, filediff
from prettify import prettify_xml

class Experiment (object):
    def __init__(self, left_name, right_name):
        self.left_name = left_name
        self.right_name = right_name
        self.exp_name = "{}_{}".format(left_name, right_name)

    def extract_left(self):
        extract_docx(self.docx_paths[0], self.ugly_dir_paths[0])

    def extract_right(self):
        extract_docx(self.docx_paths[1], self.ugly_dir_paths[1])

    def prettify_left(self):
        self._mkdir(self.pretty_dir_paths[0])
        for ugly_path, pretty_path in zip(self.ugly_file_paths[0], self.pretty_file_paths[0]):
            try:
                pretty_str = prettify_xml(ugly_path)
            except IOError:
                self._mkdir(pretty_path)
            else:
                with open(pretty_path, 'w') as f:
                    f.write(pretty_str.encode('utf-8'))

    def prettify_right(self):
        self._mkdir(self.pretty_dir_paths[1])
        for ugly_path, pretty_path in zip(self.ugly_file_paths[1], self.pretty_file_paths[1]):
            try:
                pretty_str = prettify_xml(ugly_path)
            except IOError:
                self._mkdir(pretty_path)
            else:
                with open(pretty_path, 'w') as f:
                    f.write(pretty_str.encode('utf-8'))

    def _mkdir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

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
    def pretty_dir_paths(self):
        try:
            return self._pretty_dir_paths
        except AttributeError:
            self._pretty_dir_paths = self._configure_pretty_dir_paths()
            return self._pretty_dir_paths

    def _configure_pretty_dir_paths(self):
        return (
            self._pretty_dir_path(self.left_name),
            self._pretty_dir_path(self.right_name),
        )

    def _pretty_dir_path(self, name):
        return self._path(self._data_path(name), 'pretty')

    @property
    def changed_files(self):
        common_files = dirdiff.get_common(*self.pretty_dir_paths)
        changes = []
        for f in common_files:
            left = self._path(self.pretty_dir_paths[0], f)
            right = self._path(self.pretty_dir_paths[1], f)
            if not os.path.isdir(left) and not os.path.isdir(right):
                _context_diff = filediff.get_context_diff(left, right)
                if _context_diff:
                    changes.append(f)
        return changes

    def write_diff_reports(self):
        for f in self.changed_files:
            left = self._path(self.pretty_dir_paths[0], f)
            right = self._path(self.pretty_dir_paths[1], f)
            diffs = filediff.get_diff_battery(left, right)
            for difftext, difftype in zip(diffs, ['context', 'n', 'unified']):
                self._write_diff_report(difftext, f, difftype)

    def _write_diff_report(self, difftext, filename, difftype):
        diffname = "{}/{}".format(filename, difftype)
        diffname = diffname.replace("/", "__")
        diffname = diffname.replace(".", "_")
        diffname = "{}_diff.xml".format(diffname)
        self._mkdir(self.exp_dir_path)
        with open(self._path(self.exp_dir_path, diffname), 'w') as f:
            f.write(difftext)



    @property
    def ugly_file_paths(self):
        return (
            dirdiff.walk_dir(self.ugly_dir_paths[0]),
            dirdiff.walk_dir(self.ugly_dir_paths[1]),
        )

    @property
    def pretty_file_paths(self):
        return (
            self._configure_pretty_file_paths_left(self.ugly_file_paths[0]),
            self._configure_pretty_file_paths_right(self.ugly_file_paths[1]),
            )

    def _configure_pretty_file_paths_left(self, ugly_paths):
        return [self._transpose_to_pretty_dir_left(path) for path in ugly_paths]

    def _transpose_to_pretty_dir_left(self, path):
        ugly_dir_path = self.ugly_dir_paths[0]
        pretty_dir_path = self.pretty_dir_paths[0]
        file_rel_path = os.path.relpath(path, ugly_dir_path)
        return self._path(pretty_dir_path, file_rel_path)

    def _configure_pretty_file_paths_right(self, ugly_paths):
        return [self._transpose_to_pretty_dir_right(path) for path in ugly_paths]

    def _transpose_to_pretty_dir_right(self, path):
        ugly_dir_path = self.ugly_dir_paths[1]
        pretty_dir_path = self.pretty_dir_paths[1]
        file_rel_path = os.path.relpath(path, ugly_dir_path)
        return self._path(pretty_dir_path, file_rel_path)
