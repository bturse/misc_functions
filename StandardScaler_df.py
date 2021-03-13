class StandardScaler_df(BaseEstimator, ClassifierMixin, TransformerMixin):
    """
    simple adaptation of sklearn.preprocessing.StandardScalar meant to work
    with dataframes.

    The standard score of a sample x is calculated as: 
        z = (x - u) / s
    where u is the mean of the training samples, and s is the standard
    deviation of the training samples.
    
    applies scaling only to columns specified in to_scale
    """
    def __init__(self, to_scale=None):
        self.to_scale = to_scale
        mean_ = None
        var_ = None
    def fit(self, X, y=None):
        self.mean_ = np.mean(X[self.to_scale])
        self.var_ = np.std(X[self.to_scale])
        return self
    def transform(self, X):
        X_ = X.copy()
        X_[self.to_scale] = (X_[self.to_scale] - self.mean_) / self.var_
        return X_
