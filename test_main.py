from main import do_smth, dont_do_it


def test_dont_do_it():
    assert dont_do_it() == "oh shit nooooooo"


def test_do_smth():
    assert do_smth(3) == 9
