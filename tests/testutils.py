# coding: utf-8

import unittest, sys, traceback, os
from functools import wraps
from unittest import TextTestResult
PKG_DIR = os.path.dirname(os.path.realpath(__file__))

__unittest = True

def heading2(text):
    style = '~'
    return "\n{}\n{}\n".format(text, style * len(text))
        

class DiffTest(unittest.TestCase):
    def check(self, target, result):
        joined_result = ''.join([unicode(i) for i in result])

        if target != joined_result:
            msg="{}\n{}\n{}\n{}".format(
                heading2('Expected Diff'),
                target.encode('utf-8'), 
                heading2('Actual Diff'),
                joined_result.encode('utf-8')
                )
            raise self.failureException(msg)    

def failfast(method):
    @wraps(method)
    def inner(self, *args, **kw):
        if getattr(self, 'failfast', False):
            self.stop()
        return method(self, *args, **kw)
    return inner

class CustomResult(TextTestResult):
    separator2 = "{}{}".format(40 * '-', '> DONE' )

    @failfast
    def superAddFailure(self, test, err):
        """Called when an error has occurred. 'err' is a tuple of values as
        returned by sys.exc_info()."""
        self.failures.append((test, self.format_error_message(err, test)))
        self._mirrorOutput = True

    def addFailure(self, test, err):
        self.superAddFailure(test, err)
        if self.showAll:
            self.stream.writeln("FAIL")
        elif self.dots:
            self.stream.write('F')
            self.stream.flush()

    @failfast
    def superAddError(self, test, err):
        """Called when an error has occurred. 'err' is a tuple of values as
        returned by sys.exc_info().
        """
        self.errors.append((test, self.format_error_message(err, test)))
        self._mirrorOutput = True

    def addError(self, test, err):
        self.superAddError(test, err)
        if self.showAll:
            self.stream.writeln("ERROR")
        elif self.dots:
            self.stream.write('E')
            self.stream.flush()

    def heading1(self, text):
        return "{}\n{}".format(text, '-' * len(text))

    def format_error_message(self, err, test):
        ex_type, msg, tb = err
        while tb and self._is_relevant_tb_level(tb):
            tb = tb.tb_next
        self.msg = msg
        self.ex_type = ex_type.__name__
        self.fex = self.format_ex(ex_type, msg)
        self.ftb = self.format_tb(tb)
        return "\n{}\n\n{}\n".format(self.fex, self.ftb)

    def _is_relevant_tb_level(self, tb):
        return '__unittest' in tb.tb_frame.f_globals

    def format_ex(self, ex_type, msg):
        return "{}\n{}".format(self.heading1(ex_type.__name__), msg)

    def format_tb(self, tb):
        ftb = traceback.extract_tb(tb)
        ftb_lines = []
        ftb_lines.append(self.heading1("Traceback"))
        for no, l in enumerate(ftb):
            filename, lineno, funcname, text = l
            rel_path = os.path.relpath(filename, PKG_DIR)
            summary = "{}. {}\n   - {} : {}\n   - {}".format(no+1, rel_path, funcname, lineno, text)
            ftb_lines.append(summary)
        return "\n".join(ftb_lines)

    def printErrors(self):
        if self.dots or self.showAll:
            self.stream.writeln()
        self.stream.writeln()
        self.printErrorList('ERROR', self.errors)
        self.printErrorList('FAIL', self.failures)

    def printErrorList(self, flavour, errors):
        for test, err in errors:
            title = "{}: {}".format(flavour, self.getDescription(test))
            self.stream.writeln(title)
            self.stream.writeln('=' * len(title))
            self.stream.writeln("%s" % err)