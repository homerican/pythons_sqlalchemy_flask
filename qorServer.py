# -*- coding: utf-8 -*-
from flask import Flask, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import FieldList
from wtforms import Form as NoCsrfForm
from wtforms.fields import StringField, FormField, SubmitField
from wtforms.validators import DataRequired

from models.qorMOdels import *

app = Flask(__name__)
app.config.from_pyfile('qorServer.cfg')
dbQoR = SQLAlchemy(app)
