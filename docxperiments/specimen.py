# coding: utf-8

from pathutils import mkpath, data_abs, ls, mkrel, mkdir, specimens_abs
from prettify import prettify_xml
from zipfile import ZipFile


class Specimen(object):
    """
    Locate and manage specimen file paths and operations.
    """
    def __init__(self, name):
        """
        Create a new specimen set based around a given name.

        :param name: name used to locate the .docx file
                    and name related experiments.
        :type name: string

        """
        self.name = name

    def extract(self):
        """
        Extract this specimen's docx file
        into a directory called 'ugly' in the same directory.

        """
        archive = ZipFile(self.docx)
        archive.extractall(self.ugly)

    def prettify(self):
        """
        Reformat the XML files in this specimen's 'ugly' directory
        and write them into the neighboring 'pretty' directory.

        """
        mkdir(self.pretty)
        for ugly, pretty in zip(self.uglies, self.pretties):
            try:
                pretty_str = prettify_xml(ugly)
            except IOError:
                mkdir(pretty)
            else:
                with open(pretty, 'w') as f:
                    f.write(pretty_str.encode('utf-8'))

    @property
    def path(self):
        """
        The directory holding this specimen's docx file,
        ugly XML directory, and pretty XML directory.

        :return: directory path
        :rtype: string
        """
        return specimens_abs(self.name)
    @property
    def docx(self):
        """
        The path to this specimen's docx file.

        :return: docx file path
        :rtype: string
        """
        return mkpath(self.path, self.name+'.docx')
    @property
    def ugly(self):
        """
        The path to this specimen's ugly XML directory.

        :return: directory path
        :rtype: string
        """
        return mkpath(self.path, 'ugly')
    @property
    def pretty(self):
        """
        The path to this specimen's pretty XML directory.

        :return: directory path
        :rtype: string
        """
        return mkpath(self.path, 'pretty')
    @property
    def uglies(self):
        """
        The paths to this specimen's various ugly files.

        :return: ugly file paths
        :rtype: list
        """
        return ls(self.ugly)
    @property
    def pretties(self):
        """
        The paths to this specimen's various pretty files.

        :return: pretty file paths
        :rtype: list
        """
        return [self._transpose(path) for path in self.uglies]

    def _transpose(self, path):
        """
        Generate an equivalent `pretty` path for the given `ugly` file path.

        :param path: the ugly path to transpose to a pretty path
        :type path: string

        :return: pretty path
        :rtype: string
        """
        return mkpath(self.pretty, mkrel(path, self.ugly))
