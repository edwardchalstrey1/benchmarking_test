FROM python:3

RUN apt-get update
RUN pip3 install numpy
RUN pip3 install scipy
RUN pip3 install scikit-learn

COPY classifier.py /classifier.py
COPY display_classifier_results.py /display_classifier_results.py

CMD python3 display_classifier_results.py
