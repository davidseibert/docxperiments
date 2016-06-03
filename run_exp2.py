import logging

from docxperiments import experiment
from docxperiments.analysis import operator

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename="run.log", level=logging.INFO, format=log_format, filemode="w")

logging.info("Creating Operator")
op = operator.Operator()

logging.info("Creating Experiment")
exp2 = experiment.Experiment('1-singlepara', '2-secondpara')

logging.info("Running {}".format(exp2))
op.run(exp2)
