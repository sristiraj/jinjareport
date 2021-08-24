from __future__ import print_function
from jinja2 import Environment, FileSystemLoader
import pdfkit
import pandas as pd
import numpy as np
import os


TEMPLATE_FOLDER = (os.getcwd()+"/resources/templates/").replace("/", os.path.sep)
TEMPLATE_FILE = "qareport.html"
DATA_FILE = "data.xlsx"

os.environ['path'] = os.environ.get("path")+";"+(os.getcwd()+"/wkhtmltox/bin")

env = Environment(loader=FileSystemLoader(searchpath="./resources/templates"))
template = env.get_template(TEMPLATE_FILE)
# qa_report_template = env.get_template(TEMPLATE_FOLDER+"qareport.html")

df = pd.read_excel(DATA_FILE)

qa_report = df[['table_name','status']].groupby(["table_name","status"]).count()
print(qa_report)

template_vars = {"title" : "Sales Funnel Report - National",
                 "national_pivot_table": qa_report.to_html()}

html_out = template.render(template_vars)               
pdfkit.from_string(html_out,'report.pdf')