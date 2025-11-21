

from jedi_utils import (
    jedis,
    ordenar_por_nombre,
    ordenar_por_especie,
    mostrar_informacion,
    mostrar_padawans,
    mostrar_jedi_por_especie,
    listar_jedi_por_inicial,
    mostrar_jedi_con_multiples_colores_sable,
    indicar_jedi_por_color_sable,
    indicar_padawans_de_maestros,
)

def main():
    print("--- Actividad Jedi ---")

    print("\n--- a. Listado ordenado ---")
    jedis_por_nombre = ordenar_por_nombre(jedis)
    jedis_por_especie = ordenar_por_especie(jedis)
    print("\nOrdenado por nombre:")
    for jedi in jedis_por_nombre:
        print(f"  - {jedi['nombre']}")
    print("\nOrdenado por especie:")
    for jedi in jedis_por_especie:
        print(f"  - {jedi['nombre']} ({jedi['especie']})")

    print("\n--- b. Información detallada ---")
    mostrar_informacion(jedis, ["Ahsoka Tano", "Kit Fisto"])

    print("\n--- c. Padawans de Yoda y Luke Skywalker ---")
    mostrar_padawans(jedis, ["Yoda", "Luke Skywalker"])

    print("\n--- d. Jedi de especie Humana y Twi'lek ---")
    mostrar_jedi_por_especie(jedis, ["Humano", "Twi'lek"])

    print("\n--- e. Jedi que comienzan con A ---")
    listar_jedi_por_inicial(jedis, "A")

    print("\n--- f. Jedi con sables de más de un color ---")
    mostrar_jedi_con_multiples_colores_sable(jedis)

    print("\n--- g. Jedi con sable amarillo o violeta ---")
    indicar_jedi_por_color_sable(jedis, ["amarillo", "violeta"])

    print("\n--- h. Padawans de Qui-Gon Jinn y Mace Windu ---")
    indicar_padawans_de_maestros(jedis, ["Qui-Gon Jinn", "Mace Windu"])


if __name__ == "__main__":
    main()