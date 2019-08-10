
from flask.ext.sqlalchemy import SQLAlchemy

from ... import dbQoR


# - - - Models - - -
class Project(dbQoR.Model):
    __tablename__ = 'projects'
    id = dbQoR.Column(dbQoR.Integer(), primary_key=True)
    projectName = dbQoR.Column(dbQoR.String(40))
    designs = dbQoR.relationship('Design',backref='projects',lazy='dynamic')

    def __init__(self, name):
        self.projectName = name
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.projectName)

class Design(dbQoR.Model):
    __tablename__ = 'designs'
    id = dbQoR.Column(dbQoR.Integer(), primary_key=True)
    project_id = dbQoR.Column(dbQoR.Integer(), dbQoR.ForeignKey('projects.id))
    designName = dbQoR.Column(dbQoR.String(40))
    ownerName  = dbQoR.Column(dbQoR.String(40))
    blocks = dbQoR.relationship('Block',backref='designs',lazy='dynamic')

    def __init__(self, designName, ownerName):
        self.designName = designName
        self.ownerName  = ownerName
    def __repr__(self):
        return '%s(%r)(%r)' % (self.__class__.__name__, self.designName,
        self.ownerName)

class Block(dbQoR.Model):
    __tablename__ = 'blocks'
    id = dbQoR.Column(dbQoR.Integer(), primary_key=True)
    design_id = dbQoR.Column(dbQoR.Integer(), dbQoR.ForeignKey('designs.id))
    blockName = dbQoR.Column(dbQoR.String(40))
    ownerName  = dbQoR.Column(dbQoR.String(40))

    def __init__(self, blockName, ownerName):
        self.blockName  = blockName
        self.ownerName  = ownerName
    def __repr__(self):
        return '%s(%r)(%r)' % (self.__class__.__name__, self.blockName,
        self.ownerName)
