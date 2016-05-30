from docxperiments import operator
import logging

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename="run.log", level=logging.INFO, format=log_format, filemode="w")

logging.info("Creating Operator")
op = operator.Operator()
logging.info("Running all experiments with Operator")
op.run_all()

