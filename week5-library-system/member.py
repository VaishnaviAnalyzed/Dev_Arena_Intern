class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def to_dict(self):
        return {'member_id': self.member_id, 'name': self.name}

    @classmethod
    def from_dict(cls, data):
        return cls(data['member_id'], data['name'])