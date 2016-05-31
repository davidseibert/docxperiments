#!/usr/bin/env python

# stdlib
import sys, logging, os
from zipfile import ZipFile

# config import path
sys.path.append('/Users/david/dev/docxperiments')

# local modules
from docxperiments.pathutils import mkpath, ls, mkrel

# set up logger
log_format = 'undx: %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger(__name__)


def _setup_archive(stage_path):
    synthetic_docx_path = mkpath(stage_path, 'synthetic.docx')
    logger.info("Synthetic docx: '{}'".format(synthetic_docx_path))
    synthetic_archive = ZipFile(synthetic_docx_path, 'w')
    return synthetic_archive

def _get_source_file_paths(stage_path):
    source_dir_path = mkpath(stage_path, 'decomposed')
    logger.info("Source Dir: '{}'".format(source_dir_path))
    source_file_paths = ls(source_dir_path)
    logger.info("Found {} Source Files".format(len(source_file_paths)))
    logger.info("Found {} Source Files: '{}'".format(len(source_file_paths), [mkrel(path, source_dir_path) for path in source_file_paths]))
    return source_file_paths

def _write_files_to_archive(stage_path, source_file_paths, archive):
    source_dir_path = mkpath(stage_path, 'decomposed')
    for path in source_file_paths:
        relpath = mkrel(path, source_dir_path)
        logger.info("Writing '{}' to archive".format(relpath))
        archive.write(path, relpath)
    archive.close()
    logger.info("Archive closed")
    archived_file_names = [member.filename for member in archive.infolist()]
    logger.info("Archive has these files: {}".format(archived_file_names))

def synthesize(stage_path):
    archive = _setup_archive(stage_path)
    source_file_paths = _get_source_file_paths(stage_path)
    _write_files_to_archive(stage_path, source_file_paths, archive)


def main():
    args = sys.argv
    if len(args) == 1:
        stage_path = os.path.realpath(".")
    else:
        stage_path = os.path.realpath(args[1])
    logger.info("Using '{}' for stage path".format(stage_path))
    logger.info("Synthesizing '{}'".format(stage_path))
    synthesize(stage_path)

if __name__ == '__main__':
    main()
