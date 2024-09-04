from src.lista_tarea import Tarea
import pytest

def test_agregar_tarea():
    tarea = Tarea()
    assert tarea.agregar_una_tarea("Hacer la cama") == True
    assert tarea.agregar_una_tarea("Cocinar") == True


def test_completar_tarea():
    tarea = Tarea()
    tarea.agregar_una_tarea("Hacer la cama")
    tarea.agregar_una_tarea("Cocinar")

    assert tarea.completar_tarea("Hacer la cama") == True
    assert tarea.completar_tarea("cocinar") == True


def test_eliminar_tarea():
    tarea = Tarea()
    tarea.agregar_una_tarea("Hacer la cama")
    assert tarea.eliminar_tarea("Hacer la cama") == True

def test_retornar_falso_si_es_tarea_repetida():
    tarea = Tarea()
    tarea.agregar_una_tarea("Limpiar la casa")
    assert tarea.agregar_una_tarea("Limpiar la casa") == False



