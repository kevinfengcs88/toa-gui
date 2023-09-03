class Invocation:
    def __init__(self, name, description, raidlevel, category):
        self._name = name
        self._description = description
        self._raidlevel = raidlevel
        self._category = category

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_raidlevel(self):
        return self._raidlevel

    def get_category(self):
        return self._category

    def set_name(self, name):
        self._name = name

    def set_description(self, description):
        self._description = description

    def set_raidlevel(self, raidlevel):
        self._raidlevel = raidlevel

    def set_category(self, category):
        self._category = category

    def __str__(self):
        return f"Invocation(name='{self._name}', description='{self._description}', raidlevel={self._raidlevel}, category='{self._category}')"