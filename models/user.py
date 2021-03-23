import json
from pydantic import BaseModel


class User(BaseModel):

    def __init__(self, name: str, id: str):
        super.__init__(self, name, id)

    def to_json(self):
        return json.dumps(
            {'user_id': self._id, 'name': self._name}
        )