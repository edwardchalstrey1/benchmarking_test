from sklearn import datasets, svm, metrics
import time

digits = datasets.load_digits()

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

expected = digits.target[n_samples // 2:]

classifier = svm.SVC(gamma='scale')

start = time.time()
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])
end = time.time()
training_time = end - start

start = time.time()
predicted = classifier.predict(data[n_samples // 2:])
end = time.time()
classifier_time = end - start

report = metrics.classification_report(expected, predicted, output_dict=True)

performance = report['micro avg']['f1-score']

def results():

    return({"Training time (s)": training_time, "Prediction time (s)": classifier_time,
    "Performance (micro avg f1 score)": report['micro avg']['f1-score']})
