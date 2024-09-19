from src.lista_tarea import Tarea, GestorTarea
import pytest

def test_identificador_de_tarea():
    tarea = Tarea(1, "Hacer la cama")

    assert tarea.identificador_tarea(1) == True
    assert tarea.identificador_tarea(2) == False

def test_descripcion_de_tarea():
    tarea = Tarea(1, "Hacer la cama")

    assert tarea.descripcion_tarea("Hacer la cama") == True
    assert tarea.descripcion_tarea("Ir al supermercado") == False

def test_agregar_tarea():
    gestor = GestorTarea()
    gestor.agregar_tarea(1, "Hacer la cama")
    gestor.agregar_tarea(2, "Comprar comida")

    tareas = gestor.listar_tareas()

    assert len(tareas) == 2
    assert tareas[0].obtener_id() == 1
    assert tareas[0].obtener_descripcion() == "Hacer la cama"
    assert tareas[1].obtener_id() == 2
    assert tareas[1].obtener_descripcion() == "Comprar comida"

def test_eliminar_tarea():
    gestor = GestorTarea()
    gestor.agregar_tarea(1, "Hacer la cama")
    gestor.agregar_tarea(2, "Comprar comida")

    gestor.eliminar_tarea(1)
    tareas = gestor.listar_tareas()

def test_comprobar_que_existan_las_demas_tareas_que_no_fueron_eliminadas():
    gestor = GestorTarea()
    gestor.agregar_tarea(1, "Hacer la cama")
    gestor.agregar_tarea(2, "Comprar comida")

    gestor.eliminar_tarea(1)
    tareas = gestor.listar_tareas()

    assert len(tareas) == 1
    assert tareas[0].obtener_id() == 2
    assert tareas[0].obtener_descripcion() == "Comprar comida"

def test_intentar_eliminar_una_tarea_que_no_existe():
    gestor = GestorTarea()
    gestor.agregar_tarea(1, "Hacer la cama")

    gestor.eliminar_tarea(3)
    tareas = gestor.listar_tareas()
    assert len(tareas) == 1

def test_marcar_tarea_completada():
    gestor = GestorTarea()
    gestor.agregar_tarea(1, "Hacer la cama")

    gestor.marcar_tarea_completada(1)
    tareas = gestor.listar_tareas()

    assert tareas[0].esta_completada() is True

def test_comprobar_que_una_tarea_inexistente_no_afecte_el_estado():
    gestor = GestorTarea()
    gestor.agregar_tarea(1, "Hacer la cama")

    gestor.marcar_tarea_completada(1)
    tareas = gestor.listar_tareas()

    gestor.marcar_tarea_completada(2)
    assert tareas[0].esta_completada() is True






