from day5 import main


def test_main(capsys):
    main(1)
    captured = capsys.readouterr()
    assert captured.out[-8:] == "7692125\n"


def test_main2(capsys):
    main(5)
    captured = capsys.readouterr()
    assert captured.out == "14340395\n"
