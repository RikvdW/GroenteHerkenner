import numpy as np
from sklearn.naive_bayes import MultinomialNB


class Teach:
    """docstring for Teach."""
    def __init__(self,training,labels):
        super(Teach, self).__init__()
        self.training=training
        self.labels=labels
    def teach(self):
        X = self.training

        y = self.labels

        self.clf = MultinomialNB()
        self.clf.fit(X, y)
    def Predict(self, n):
        print(self.clf.predict(n))

X = [   [1,1,1,1],
        [0,1,0,0],
        [0,1,1,0],
        [0,1,0,1],
        [1,0,1,0],
        [0,0,0,0]
    ]


tch=Teach(X,np.array(["one", 2, 3, 4, 5, 6]))
tch.teach()
tch.Predict([[1,1,1,1],[0,1,0,0]])
