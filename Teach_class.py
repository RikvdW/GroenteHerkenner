import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.kernel_approximation import RBFSampler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
import pickle


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
        InputL = open('labels.pkl', 'rb')
        one = pickle.load(InputL)
        y=[]
        Input = open('data.pkl', 'rb')
        X = pickle.load(Input)
        for i in one:
            if i == 1:
                y.append("prei")
            elif i == 2:
                y.append("aubergine")
            elif i == 3:
                y.append("radijs")
            elif i == 4:
                y.append("wortel")
            elif i == 5:
                y.append("broccoli")

        self.MNB =  MultinomialNB()
        self.NC =  NearestCentroid()
        self.SVC = svm.SVC()
        self.Nur = MLPClassifier(solver='adam', alpha=1e-5,hidden_layer_sizes=(1000, 500), random_state=1000,learning_rate='adaptive',warm_start=True,max_iter=1)
        self.SGDC = SGDClassifier(loss="log", penalty="elasticnet",random_state=100,max_iter=10)
        self.RF = RandomForestClassifier(n_estimators=1000)
        self.bagging = BaggingClassifier(KNeighborsClassifier(),max_samples=0.5, max_features=0.5)

        self.bagging.fit(X,y)
        self.RF.fit(X, y)
        self.SGDC.fit(X, y)
        self.MNB.fit(X, y)
        self.NC.fit(X, y)
        self.SVC.fit(X, y)
        self.Nur.fit(X,y)

    def Predict(self, n):
        print("bagging" + str(self.bagging.predict([n])))
        print(self.bagging.predict_proba([n]))
        print("random forest" + str(self.RF.predict([n])))
        print(self.RF.predict_proba([n]))
        print("SGDC" + str(self.SGDC.predict([n])))
        print(self.SGDC.predict_proba([n]))
        print("Nerual" + str(self.Nur.predict([n])))
        print(self.Nur.predict_proba([n]))
        print("MultinomialNB" + str(self.MNB.predict([n])))
        print(self.MNB.predict_proba([n]))
        print("Meriest centroid"+ str(self.NC.predict([n])))
        print(self.NC.predict_proba([n]))
        print("Support vector machine (SVC)" + str(self.SVC.predict([n])))
        print(self.MNB.predict_log_proba([n]))






#tch.Predict([0, 227, 542, 551, 449, 0, 0, 227, 542, 551, 449, 0, 24489, 14252, 10620, 7030, 6626, 0, 3961])
