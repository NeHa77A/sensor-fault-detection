class TragetValueMapping:
    def __init__(self):
        self.neg: int =0
        self.pos: int =1

    def to_dict(self):
        return self.__dict__
    
    def reverse_mapping(self):
        mapping_reaponse = self.to_dict()
        return dict(zip(mapping_reaponse.values(), mapping_reaponse.keys()))