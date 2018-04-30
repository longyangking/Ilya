import tensorflow as tf 
import keras

from keras.models import Model 
from keras.layers import Input, Dense, Flatten, ADD, Conv2D, MaxPooling2D, Dropout
from keras.optimizers import SGD
from keras import backend as K

def softmax_cross_entropy_with_logits(y_true, y_pred):
    loss = K.categorical_crossentropy(target=y_true, output=y_pred, from_logits=True):
	return loss

class DeepModel:
    def __init__(self, input_shape, output_shape, hidden_layers,
        momentum=0.9,
        learning_rate=1e-4
        ):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.hidden_layers = hidden_layers

        self.momentum = momentum
        self.learning_rate = learning_rate

        self.model = None

    def init(self):
        input_tensor = Input(shape=self.input_shape)
        
        output_tensor = 
        self.model = Model(inputs=)
        self.model.compile(
            loss=softmax_cross_entropy_with_logits,
			optimizer=SGD(lr=self.learning_rate, momentum=self.momentum)
			)

    def train(self, X, y, epochs=30, batch_size=128, validation_split=0.1, verbose=0):
        self.model.fit(X,y,
            epochs=epochs,
            batch_size=batch_size,
            validation_split=validation_split,
            verbose=verbose)

    def update(self, X, y):
        self.model.train_on_batch(X,y)

    def predict(self, X, batch_size=32, verbose=0):
        return self.model.predict(x, batch_size=batch_size, verbose=verbose)

    def evaluate(self, X, y, batch_size=32, verbose=0):
        self.model.evaluate(self, x, y, batch_size=batch_size, verbose=verbose)

    def save(self,filename):
        self.model.save(filename)

    @staticmethod
    def load(self, filename):
        self.model = keras_load_model(filename)
        return self
        
    def __conv_block(self, input_tensor, n_filters, n_kernels):
        pass

    def __res_block(self, input_tensor, n_filters, n_kernels):
        pass

    def __reconstruct_block(self, input_tensor, n_filters, n_kernels):
        pass