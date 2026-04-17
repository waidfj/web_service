#DECLARATION: This snippet is AI-Generated
# To allow attribute-style access to dictionary keys
class MapDict(dict):
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(f"No such attribute: {item}")
