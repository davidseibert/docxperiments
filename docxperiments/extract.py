# coding: utf-8

from zipfile import ZipFile

def extract_docx(docx_path, destination_dir_path):
    docx_file = ZipFile(docx_path)
    docx_file.extractall(destination_dir_path)
