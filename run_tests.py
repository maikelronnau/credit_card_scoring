#!/usr/bin/python

import requests


def test_predict():
    from multiprocessing import Process
    import time

    process = Process(target=start_server)
    process.start()

    # Giving a few seconds to have the server start
    time.sleep(10)

    data = {"id": "8db4206f-8878-174d-7a23-dd2c4f4ef5a0", "score_3": 480.0, "score_4": 105.2, "score_5": 0.8514, "score_6": 94.2, "income": 500000}

    r = requests.post("http://localhost:8080/predict", json=data)

    response = str(r.text)

    print("RESPONSE: {}".format(response))

    if response == "{'id': u'8db4206f-8878-174d-7a23-dd2c4f4ef5a0', 'prediction': 0.1495}":
        print "PASS: Predict endpoint ok"
        process.terminate()
        exit(0)
    else:
        print "FAIL: Predict endpoint ok"
        process.terminate()
        exit(1)


def start_server():
    import os
    os.system("python run.py")


####
# To be removed
def development_test():
    data = {"id": "8db4206f-8878-174d-7a23-dd2c4f4ef5a0", "score_3": 480.0, "score_4": 105.2, "score_5": 0.8514, "score_6": 94.2, "income": 500000}

    r = requests.post("http://localhost:8091/predict", json=data)

    print r.text


if __name__ == "__main__":
    # test_predict()
    development_test()
