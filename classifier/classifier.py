from sklearn import datasets, svm, metrics
import time

def results():

    digits = datasets.load_digits()

    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))

    expected = digits.target[n_samples // 2:]

    C = 1.0  # SVM regularization parameter
    models = [svm.SVC(kernel='linear', C=C),
          svm.LinearSVC(C=C),
          svm.SVC(kernel='rbf', gamma=0.7, C=C),
          svm.SVC(kernel='poly', degree=3, C=C)]

    ### Version 1.0 ###

    # classifier = models[0]

    ### Version 1.1 ###

    classifier = models[1]

    ### Version 1.2 ###

    # classifier = models[2]

    ### Version 1.3 ###

    # classifier = models[3]

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

    return([metrics.classification_report(expected, predicted), {"Training time (s)": training_time, "Prediction time (s)": classifier_time,
    "Performance (micro avg f1 score)": report['micro avg']['f1-score']}])
