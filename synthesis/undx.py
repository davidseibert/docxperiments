#!/usr/bin/env python

# stdlib
import sys, logging, os
from zipfile import ZipFile

# config import path
sys.path.append('/Users/david/dev/docxperiments')

# local modules
from docxperiments.pathutils import mkpath, ls

# set up logger
log_format = 'undx: %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger(__name__)


def decompose(stage_path):
    natural_docx_path = mkpath(stage_path, 'natural.docx')
    destination_path = mkpath(stage_path, 'decomposed')

    logger.info("DOCX: '{}'".format(natural_docx_path))
    natural_archive = ZipFile(natural_docx_path)

    logger.info("Decomposed dir: '{}'".format(destination_path))
    natural_archive.extractall(destination_path)
    extracted_file_paths = ls(destination_path)
    logger.info("Extracted {} files".format(len(extracted_file_paths)))
    logger.debug("Extracted {} files: {}".format(len(extracted_file_paths), extracted_file_paths))

def main():
    args = sys.argv
    if len(args) == 1:
        stage_path = os.path.realpath(".")
    else:
        stage_path = os.path.realpath(args[1])
    logger.info("Using '{}' for stage path".format(stage_path))
    logger.info("Decomposing '{}'".format(stage_path))
    decompose(stage_path)

if __name__ == '__main__':
    main()
