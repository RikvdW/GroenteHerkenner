import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.neighbors.nearest_centroid import NearestCentroid


class Teach:
    """docstring for Teach."""
    X = [   [0, 0, 0, 584, 1304, 0, 0, 0, 0, 584, 1304, 0, 8402, 7401, 8552, 10331, 8466, 0, 7529],
            [0, 0, 574, 1546, 1248, 0, 0, 0, 574, 1546, 1248, 0, 13521, 14828, 11963, 8516, 7633, 0, 1933],
            [0, 883, 588, 449, 356, 0, 0, 883, 588, 449, 356, 0, 2362, 2618, 4585, 3963, 3233, 0, 2737],
            [0, 1435, 1944, 1505, 1164, 0, 0, 1435, 1944, 1505, 1164, 0, 4593, 15108, 13479, 10188, 7812, 0, 4832],
            [0, 871, 1043, 804, 619, 0, 0, 871, 1043, 804, 619, 0, 7878, 5793, 4785, 3301, 2773, 0, 2472]
        ]

    def __init__(self):
        super(Teach, self).__init__()
        self.training=self.X
        self.labels=np.array(["wortel", "prei", "radijs", "broccoli", "auburgine"])
        self.teach()

    def teach(self):
        X = self.training

        y = self.labels

        self.clf =  NearestCentroid()
        self.clf.fit(X, y)
        print(self.clf.get_params())
        print(self.clf.score(X,y))
    def Predict(self, n):
        print(self.clf.predict([n]))
        #print(self.clf.predict_log_proba([n]))






#tch.Predict([0, 227, 542, 551, 449, 0, 0, 227, 542, 551, 449, 0, 24489, 14252, 10620, 7030, 6626, 0, 3961])
