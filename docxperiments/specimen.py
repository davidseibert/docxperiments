# coding: utf-8

from pathutils import mkpath, data_abs, ls, mkrel, mkdir, specimens_abs, data_rel
from prettify import prettify_xml
from zipfile import ZipFile
import logging


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
        self.logger = logging.getLogger('SPEC: ' + self.name)
        self.path = specimens_abs(self.name)
        self.logger.debug("Path set to {}".format(self.path))
        self.docx = mkpath(self.path, self.name+'.docx')
        self.logger.debug("Docx set to {}".format(self.docx))
        self.ugly = mkpath(self.path, 'ugly')
        self.logger.debug("Ugly directory set to {}".format(self.ugly))
        self.pretty = mkpath(self.path, 'pretty')
        self.logger.debug("Pretty directory set to {}".format(self.pretty))
        self.uglies = ls(self.ugly)
        self.logger.debug("Ugly files set to {}".format(self.uglies))
        self.pretties = [self._transpose(path) for path in self.uglies]
        self.logger.debug("Pretty files set to {}".format(self.pretties))

    def __repr__(self):
        return "{}('{}')".format(self.__class__.__name__, self.name)

    def extract(self):
        """
        Extract this specimen's docx file
        into a directory called 'ugly' in the same directory.

        """
        self.logger.debug("Extracting '{}' to '{}'".format(data_rel(self.docx), data_rel(self.ugly)))
        archive = ZipFile(self.docx)
        archive.extractall(self.ugly)

    def prettify(self):
        """
        Reformat the XML files in this specimen's 'ugly' directory
        and write them into the neighboring 'pretty' directory.

        """
        self.logger.debug("Prettifying")
        mkdir(self.pretty)
        for ugly, pretty in zip(self.uglies, self.pretties):
            try:
                pretty_str = prettify_xml(ugly)
            except IOError:
                mkdir(pretty)
            else:
                with open(pretty, 'w') as f:
                    f.write(pretty_str.encode('utf-8'))

    def _transpose(self, path):
        """
        Generate an equivalent `pretty` path for the given `ugly` file path.

        :param path: the ugly path to transpose to a pretty path
        :type path: string

        :return: pretty path
        :rtype: string
        """
        new_path = mkpath(self.pretty, mkrel(path, self.ugly))
        self.logger.debug("Transposed {} to {}".format(path, new_path))
        return new_path
