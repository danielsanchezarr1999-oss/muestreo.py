"""
MÓDULO: sistema_academico.py
PROPÓSITO: Demostrar conceptos avanzados de POO (Clases, Atributos, Constructores, 
           Métodos, Instanciación y Agregación de Objetos) mediante un sistema interactivo.
AUTOR: Jesús Daniel Sánchez Arredondo
"""

# =====================================================================
# 1. CLASE: Estudiante (Entidad Individual)
# =====================================================================
class Estudiante:
    """
    Clase que define la estructura y el comportamiento individual de un Estudiante.
    """

    # CONSTRUCTOR: Inicializa los atributos del estudiante
    def __init__(self, matricula: str, nombre: str, carrera: str):
        self.matricula = matricula        # Atributo de tipo Texto (String)
        self.nombre = nombre              # Atributo de tipo Texto (String)
        self.carrera = carrera            # Atributo de tipo Texto (String)
        self.calificaciones = []          # Atributo de tipo Lista (Colección de datos)

    # MÉTODO 1: Agregar una calificación con validación de rango
    def agregar_calificacion(self, nota: float):
        if 0 <= nota <= 100:
            self.calificaciones.append(nota)
            print(f"    [✓] Nota {nota} añadida a {self.nombre}.")
        else:
            print(f"    [X] Error: La nota {nota} no es válida (Debe ser de 0 a 100).")

    # MÉTODO 2: Calcular el promedio dinámico
    def calcular_promedio(self) -> float:
        if not self.calificaciones:
            return 0.0  # Validación para evitar error crítico de división entre cero
        return float(sum(self.calificaciones) / len(self.calificaciones))

    # MÉTODO 3: Obtener el estatus académico
    def obtener_estatus(self) -> str:
        return "APROBADO" if self.calcular_promedio() >= 70 else "REPROBADO"


# =====================================================================
# 2. CLASE: Grupo (Concepto de Agregación de Objetos)
# =====================================================================
class Grupo:
    """
    Clase que administra una colección de objetos de tipo 'Estudiante'.
    Demuestra cómo los objetos pueden interactuar entre sí.
    """

    # CONSTRUCTOR: Inicializa el grupo con un nombre/código
    def __init__(self, nombre_grupo: str):
        self.nombre_grupo = nombre_grupo  # Atributo identificador del grupo
        self.lista_estudiantes = []       # Lista que guardará OBJETOS de la clase Estudiante

    # MÉTODO 1: Agregar un objeto Estudiante al grupo
    def inscribir_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
        print(f"[OK] Estudiante '{estudiante.nombre}' inscrito en el grupo {self.nombre_grupo}.")

    # MÉTODO 2: Buscar un estudiante por su matrícula
    def buscar_estudiante(self, matricula: str) -> Estudiante:
        for est in self.lista_estudiantes:
            if est.matricula == matricula:
                return est  # Retorna el objeto completo si lo encuentra
        return None  # Retorna Nada si no existe

    # MÉTODO 3: Mostrar el reporte general del grupo (Iteración y formato)
    def generar_reporte_general(self):
        print("\n" + "═" * 65)
        print(f" 📊 REPORTE GENERAL DEL GRUPO: {self.nombre_grupo} ")
        print("═" * 65)
        print(f"{'Matrícula':<12} | {'Nombre':<20} | {'Promedio':<10} | {'Estatus':<10}")
        print("-" * 65)
        
        if not self.lista_estudiantes:
            print(" El grupo no tiene estudiantes inscritos actualmente.")
        else:
            for est in self.lista_estudiantes:
                prom = est.calcular_promedio()
                estatus = est.obtener_estatus()
                # Uso de formato de texto alineado para una vista limpia en consola
                print(f"{est.matricula:<12} | {est.nombre:<20} | {prom:<10.2f} | {estatus:<10}")
        print("═" * 65 + "\n")


# =====================================================================
# 3. PROGRAMA PRINCIPAL CON MENÚ INTERACTIVO
# =====================================================================
if __name__ == "__main__":
    # Creamos un grupo contenedor de manera inicial
    mi_grupo = Grupo("SOFTWARE-101")

    # Datos iniciales precargados para que la app no inicie vacía en tu demostración
    alumno_demo = Estudiante("202601", "Daniel Sánchez", "Sistemas")
    alumno_demo.agregar_calificacion(95)
    alumno_demo.agregar_calificacion(98)
    mi_grupo.inscribir_estudiante(alumno_demo)

    while True:
        print("┌────────────────────────────────────────────────────────┐")
        print("│       SISTEMA GESTOR ACADÉMICO (CONTROL POO)          │")
        print("├────────────────────────────────────────────────────────┤")
        print("│ 1. Inscribir nuevo estudiante                          │")
        print("│ 2. Registrar calificación a un estudiante              │")
        print("│ 3. Ver reporte general del grupo                       │")
        print("│ 4. Salir de la aplicación                              │")
        print("└────────────────────────────────────────────────────────┘")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            print("\n--- REGISTRO DE NUEVO ESTUDIANTE ---")
            mat = input("Ingrese la matrícula: ")
            nom = input("Ingrese el nombre completo: ")
            car = input("Ingrese la carrera: ")
            
            # Instanciación dinámica basada en la entrada del usuario
            nuevo_alumno = Estudiante(mat, nom, car)
            mi_grupo.inscribir_estudiante(nuevo_alumno)
            print()

        elif opcion == "2":
            print("\n--- REGISTRO DE CALIFICACIONES ---")
            mat = input("Ingrese la matrícula del estudiante: ")
            estudiante_encontrado = mi_grupo.buscar_estudiante(mat)
            
            if estudiante_encontrado:
                try:
                    nota = float(input(f"Ingrese la nota para {estudiante_encontrado.nombre}: "))
                    estudiante_encontrado.agregar_calificacion(nota)
                except ValueError:
                    print("[X] Error: Debe ingresar un valor numérico válido.")
            else:
                print("[X] Error: No se encontró ningún estudiante con esa matrícula.")
            print()

        elif opcion == "3":
            # Llamada al método que procesa toda la colección de objetos
            mi_grupo.generar_reporte_general()

        elif opcion == "4":
            print("\n¡Gracias por utilizar el Sistema Académico POO! Finalizando programa...")
            break
        else:
            print("\n[X] Opción inválida. Intente de nuevo.\n")
        