def test2():
    trainings = { "course1": {"title": "Python Training Course for Beginners",
                         "location": "Frankfurt",
                         "trainer": "Steve G. Snake"},
              "course2": {"title": "Intermediate Python Training",
                         "location": "Berlin",
                         "trainer": "Ella M. Charming"},
              "course3": {"title": "Python Text Processing Course",
                         "location": "Munchen",
                         "trainer": "Monica A. Snowdon"}
              }

    trainings2 = trainings.copy()

    trainings["course2"] = {"title": "Perl Seminar for Beginners",
                         "location": "Ulm",
                         "trainer": "James D. Morgan"}
    print(trainings2["course2"])
    print (trainings["course2"])


if __name__ == "__main__" :
        test2()