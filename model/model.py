def init_class(clz):
    model = read_model()
    def setattr_function(self, name, value):
        

def read_model():
    import json
    with open('./model.json', 'r') as model:
        return json.load(model)