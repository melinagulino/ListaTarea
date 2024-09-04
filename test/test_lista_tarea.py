from src.lista_tarea import Tarea
import pytest

def test_agregar_tarea():
    tarea = Tarea()
    assert tarea.agregar_una_tarea("Hacer la cama") == True
    assert tarea.agregar_una_tarea("Cocinar") == True


def test_completar_tarea():
    tarea = Tarea()

    assert tarea.completar_tarea("Hacer la cama") == True
    assert tarea.completar_tarea("cocinar") == True


def test_eliminar_tarea():
    tarea = Tarea()
    tarea.agregar_una_tarea("Hacer la cama")
    assert tarea.eliminar_tarea("Hacer la cama") == True




