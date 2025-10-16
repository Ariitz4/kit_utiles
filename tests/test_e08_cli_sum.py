import pytest
from src.cli import main

def test_main_with_numbers(capsys):
    main(["prog", "1,2,3"])
    salida = capsys.readouterr().out.strip()
    assert salida == "6.0"

def test_main_no_numbers(capsys):
    main(["prog"])
    salida = capsys.readouterr().out.strip()
    assert salida == "0"