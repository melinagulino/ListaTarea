from src.tarea import  GestorTarea

def test_agregar_tarea():
    gestor = GestorTarea()
    gestor.agregar_tarea(1, "Hacer la cama")

    assert len(gestor.listar_tareas()) == 1
    assert gestor.listar_tareas()[0].comprobar_id(1)
    assert gestor.listar_tareas()[0].comprobar_descripcion("Hacer la cama")
    assert not gestor.listar_tareas()[0].esta_completada()

def test_agregar_multiples_tarea():
    gestor = GestorTarea()
    gestor.agregar_tarea(1, "Hacer la cama")
    gestor.agregar_tarea(2, "Comprar comida")

    tareas = gestor.listar_tareas()

    assert len(tareas) == 2
    assert tareas[0].comprobar_id(1)
    assert tareas[0].comprobar_descripcion("Hacer la cama")
    assert tareas[1].comprobar_id(2)
    assert tareas[1].comprobar_descripcion("Comprar comida")

def test_eliminar_tarea():
    gestor = GestorTarea()
    gestor.agregar_tarea(1, "Hacer la cama")

    gestor.eliminar_tarea(1)

    assert len(gestor.listar_tareas()) == 0

def test_marcar_tarea_completada():
    gestor = GestorTarea()
    gestor.agregar_tarea(1, "Hacer la cama")

    gestor.marcar_tarea_completada(1)

    assert  gestor.listar_tareas()[0].esta_completada() is True








