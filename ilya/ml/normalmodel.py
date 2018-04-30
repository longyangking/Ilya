import sklearn
from sklearn.neural_network import MLPRegressor, MLPClassifier

class NeuralNetworkModel:
    def __init__(self,
        hidden_layer_sizes=(100, ), 
        activation='relu', 
        solver='adam', 
        alpha=1e-4,
        learning_rate='adaptive', 
        learning_rate_init=0.001, 
        max_iter=200,  
        tol=0.0001, 
        verbose=False, 
        momentum=0.9,
        validation_fraction=0.1
    ):
        self.hidden_layer_sizes = hidden_layer_sizes
        self.activation = activation
        self.solver = solver
        self.alpha = alpha
        self.learning_rate = learning_rate
        self.learning_rate_init = learning_rate_init
        self.max_iter = max_iter
        self.tol = tol
        self.verbose = verbose
        self.momentum = momentum
        self.validation_fraction = validation_fraction

        self.model = None
        
    def init(self):
        self.model = MLPRegressor(
            hidden_layer_sizes=self.hidden_layer_sizes, 
            activation=self.activation, 
            solver=self.solver, 
            alpha=self.alpha,
            learning_rate=self.learning_rate, 
            learning_rate_init=self.learning_rate_init, 
            max_iter=self.max_iter,  
            tol=self.tol, 
            verbose=self.verbose, 
            momentum=self.momentum,
            validation_fraction=self.validation_fraction)

    def train(self, X, y):
        self.model.fit(X, y)

    def update(self, X, y):
        self.model.partial_fit(X, y)

    def predict(self, X)
        return self.model.predict(X)

    def evaluate(self, X, y)
        return self.model.score(X, y)