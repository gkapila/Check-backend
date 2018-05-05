from . import *

DB_COMMIT_ERROR_MESSAGE = 'Failure to complete DB transaction'


### COMMIT ###

def commit_models(model_lst):
  for m in model_lst:
    db.session.add(m)
  try:
    db.session.commit()
    return model_lst
  except Exception as e:
    db.session.rollback()
    raise Exception(e)

def commit_model(m):
  return commit_models([m])[0]


### DELETE ###

def delete_models(model_lst):
  try:
    for m in model_lst:
      db.session.delete(m)
  except Exception:
    raise Exception('Deletion of models failed')
  try:
    db.session.commit()
    return model_lst
  except Exception:
    db.session.rollback()
    raise Exception(DB_COMMIT_ERROR_MESSAGE)

def delete_model(m):
  return delete_models([m])[0]

