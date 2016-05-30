#!/usr/bin/env python

import context
import sys, logging
from docxperiments.pathutils import mkpath
from zipfile import ZipFile

STAGE_DIR = 'stages'
STAGE_NAME = '0-original'
DOCX_NAME = 'natural.docx'
DESTINATION_DIR = 'ugly'

log_format = '%(name)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger('undx')
logger.info("Hello")


def _natural_docx_path(stage_name):
    path = mkpath(STAGE_DIR, stage_name, DOCX_NAME)
    return path

def _ugly_path(stage_name):
    path = mkpath(STAGE_DIR, stage_name, DESTINATION_DIR)
    return path

def analyze(stage_path):
    natural_docx_path = _natural_docx_path(stage_path)
    logger.info("Making ZipFile from '{}'".format(natural_docx_path))
    natural_archive = ZipFile(natural_docx_path)
    destination_path = _ugly_path(stage_path)
    logger.info("Extracting ZipFile to '{}'".format(destination_path))
    natural_archive.extractall(destination_path)

def main():
    args = sys.argv
    stage_path = args[1]
    logger.info("Using '{}' for stage path".format(stage_path))
    logger.info("Analyzing '{}'".format(stage_path))
    analyze(stage_path)

if __name__ == '__main__':
    main()
