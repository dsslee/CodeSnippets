import numpy as np
from keras.models import Sequential
from keras.layers import Dense


# ===== Easy Method: procedural programming =====
# PREPARE DATA
train_images = np.ones((700,5))  #row,col ->5 feature
train_labels = np.zeros((700,1))
print(train_images)

# BUILD MODEL

# ---instantiate model
model = Sequential()

# ---add model
model.add(Dense(32, activation='relu', input_shape=(5,)))
model.add(Dense(16, activation='relu'))

# ---ouput model
model.add(Dense(1, activation='softmax'))

# ---compile
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])


# TRAIN MODEL
model.fit(train_images, train_labesl, epochs=10, batch=128)


# ===== INTERMEDIATE METHOD USING CLASS =====
# PREPARE DATA
shape = 5
def makeTrain():
    train_images = np.ones((700,shape))
    train_labels = np.zeros((700,1))
    return train_images, train_labels

# BUILD MODEL
def buildModel():
    model = models.Sequential()
    model.add(layers.Dense(32, activation='relu', input_shape=(shape,)))
    model.add(layers.Dense(10, activation='softmax'))

    model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['acc'])
    return model

def fit(model):
    model.fit(train_images, train_labels, epochs=10, batch=128)
    
    
if __name__ == "__main__":
    train_images, train_labels = makeTrain()
    model_1 = buildModel()
    model_2 = buildModel()
        fit(model)


# ===== INTERMEDIATE II: Object oriented programming =====
# BUILD MODEL
class myModel:
    def __init__(self):
        self.shape = 5
        self.model = self.buildModel()
        
    def prepData(self):
        _train_images = np.ones((700, self.shape))
        _train_labels = np.zeros((700,1))
        return _train_images, _train_labels
    
    def buildModel(self):
        _model = Sequential()
        _model.add(Dense(32, activation='relu', input_shape=(self.shape,)))
        _model.add(Dense(16, activation='relu'))
        _model.add(Dense(1, activation='softmax'))
        
        _model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
        return _model
    
    def fitModel(self,train_images, train_labels):
        self.model.fit(train_images, train_labels, epochs=10, batch=128)

if __name__ == "__main__":
    my_model = inheritanceModel()
    my_model.shape = 745
    train_images, train_labels = my_model.makeTrain()
    
    my_model.fit()


# ===== ADVANCED METHOD: USING EXCEPT =====
# BUILD MODEL
class myModel:
    def __init__(self):
        self.shape = 5
        self.model = self.buildModel()
        
    def prepData(self):
        _train_images = np.ones((700, self.shape))
        _train_labels = np.zeros((700,1))
        return _train_images, _train_labels
    
    def buildModel(self):
        _model = Sequential()
        _model.add(Dense(32, activation='relu', input_shape=(self.shape,)))
        _model.add(Dense(16, activation='relu'))
        _model.add(Dense(1, activation='softmax'))
        
        _model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
        return _model
    
    def fitModel(self,train_images, train_labels):
        assert train_images.ndim == 2, "not 2 dimension
        
        if train_images.dtype is not np.float:
            raise TypeError
        
        try:
            self.model.fit(train_images, train_labels, epochs=10, batch=128)
        except Error:
            traceback.print_exc()
            pass
        
if __name__ == "__main__":
    my_model = myModel()
    my_model.shape = 745
    train_images, train_labels = my_model.makeTrain()
    
    #my_model.fit(train_images, train_labels)
    print('except py file')
                                