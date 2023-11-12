import datetime
from flask.json import JSONEncoder
import app

class CustomJSONEncoder(JSONEncoder):
  "Add support for serializing timedeltas"

  def default(o):
    if type(o) == datetime.timedelta:
      return str(o)
    if type(o) == datetime.datetime:
      return o.isoformat()
    return super().default(o)

app.json_encoder = CustomJSONEncoder  