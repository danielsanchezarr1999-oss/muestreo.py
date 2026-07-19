# 1. CLASE BASE (SUPERCLASE)
class Persona:
    """
    Clase Base que define los atributos y métodos comunes para cualquier
    individuo dentro del sistema escolar, permitiendo la reutilización de código.
    """
    def __init__(self, matricula, nombre):
        self.matricula = matricula  # Atributo heredable
        self.nombre = nombre        # Atributo heredable

    def mostrar_informacion(self):
        """Método base para desplegar datos básicos."""
        return f"Matrícula: {self.matricula} | Nombre: {self.nombre}"


# 2. CLASE DERIVADA (SUBCLASE) - ESTUDIANTE REGULAR (LICENCIATURA)
class Estudiante(Persona):
    """
    Clase Derivada que hereda de Persona. Reutiliza 'matricula' y 'nombre'
    e incorpora lógica específica para alumnos de nivel licenciatura.
    """
    def __init__(self, matricula, nombre, carrera):
        # Invocación al constructor de la clase base mediante super()
        super().__init__(matricula, nombre)
        self.carrera = carrera  # Atributo exclusivo de la subclase
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        """Método exclusivo con validación estricta de rango."""
        if 0 <= calificacion <= 100:
            self.calificaciones.append(calificacion)
            print(f"\n[OK] Calificación {calificacion} agregada exitosamente a {self.nombre}.")
            return True
        else:
            print("\n[ERROR] La calificación debe estar estrictamente en el rango de 0 a 100.")
            return False

    def calcular_promedio(self):
        """Calcula el promedio previniendo errores lógicos de división entre cero."""
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

    # SOBRESCRITURA DE MÉTODO (Override)
    def mostrar_informacion(self):
        """Sobrescribe el método de Persona para adaptarlo al perfil de Estudiante."""
        datos_base = super().mostrar_informacion()  # Reutiliza el comportamiento del padre
        return f"{datos_base} | Nivel: Licenciatura | Carrera: {self.carrera} | Promedio: {self.calcular_promedio():.2f}"


# 3. NUEVA CLASE DERIVADA (SUBCLASE) - ESTUDIANTE DE POSGRADO
class EstudiantePosgrado(Persona):
    """
    Segunda clase derivada que extiende de Persona. Representa alumnos de alta especialidad.
    """
    def __init__(self, matricula, nombre, linea_investigacion):
        super().__init__(matricula, nombre)
        self.linea_investigacion = linea_investigacion  # Atributo exclusivo
        self.proyecto_tesis = "No asignado"

    def asignar_tesis(self, titulo_tesis):
        """Método exclusivo para la gestión de proyectos de posgrado."""
        if titulo_tesis.strip():
            self.proyecto_tesis = titulo_tesis
        else:
            self.proyecto_tesis = "Por definir"
        print(f"\n[OK] Tesis asignada a {self.nombre}: '{self.proyecto_tesis}'")

    # SOBRESCRITURA DE MÉTODO (Override)
    def mostrar_informacion(self):
        """Sobrescribe el método de Persona para mostrar campos de investigación."""
        datos_base = super().mostrar_informacion()
        return f"{datos_base} | Nivel: Posgrado | Investigación: {self.linea_investigacion} | Tesis: {self.proyecto_tesis}"


# 4. CLASE CONTENEDORA (AGREGACIÓN)
class Grupo:
    """
    Clase contenedora que aplica agregación. Almacena objetos de cualquier clase
    derivada de Persona e interactúa con ellos de manera polimórfica.
    """
    def __init__(self, nombre_grupo):
        self.nombre_grupo = nombre_grupo
        self.integrantes = []

    def agregar_integrante(self, persona):
        """Registra de manera dinámica cualquier subclase derivada de Persona."""
        self.integrantes.append(persona)
        print(f"\n[ÉXITO] {persona.nombre} ha sido inscrito en el grupo {self.nombre_grupo}.")

    def generar_reporte(self):
        """Recorre la colección y ejecuta dinámicamente el método sobrescrito correspondiente."""
        print(f"\n=================================================================")
        print(f"               REPORTE DEL GRUPO: {self.nombre_grupo}")
        print(f"=================================================================")
        if not self.integrantes:
            print("   [AVISO] No hay alumnos registrados en este grupo actualmente.")
        else:
            for i in self.integrantes:
                # Polimorfismo: cada objeto responde con su propia implementación del método
                print(f"-> {i.mostrar_informacion()}")
        print("=================================================================\n")


# 5. PROGRAMA PRINCIPAL CON INTERFAZ DE CONTROL
def menu():
    mi_grupo = Grupo("POO-A-2026")
    
    while True:
        print("--- MENÚ GESTOR ACADÉMICO (HERENCIA Y POLIMORFISMO) ---")
        print("1. Registrar Estudiante Regular (Licenciatura)")
        print("2. Registrar Estudiante de Posgrado")
        print("3. Agregar Calificación a Estudiante Regular")
        print("4. Mostrar Reporte General del Grupo")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            print("\n[NUEVO ESTUDIANTE REGULAR]")
            mat = input("Introduce la Matrícula: ").strip()
            nom = input("Introduce el Nombre: ").strip()
            carr = input("Introduce la Carrera: ").strip()
            
            if mat and nom and carr:
                nuevo_est = Estudiante(mat, nom, carr)
                mi_grupo.agregar_integrante(nuevo_est)
            else:
                print("\n[ERROR] Todos los campos son obligatorios para el registro.")
            print("\n" + "-"*50 + "\n")
            
        elif opcion == "2":
            print("\n[NUEVO ESTUDIANTE DE POSGRADO]")
            mat = input("Introduce la Matrícula: ").strip()
            nom = input("Introduce el Nombre: ").strip()
            inv = input("Introduce la Línea de Investigación: ").strip()
            tesis = input("Introduce el Título de Tesis (Opcional): ").strip()
            
            if mat and nom and inv:
                nuevo_pos = EstudiantePosgrado(mat, nom, inv)
                if tesis:
                    nuevo_pos.asignar_tesis(tesis)
                mi_grupo.agregar_integrante(nuevo_pos)
            else:
                print("\n[ERROR] Matrícula, Nombre y Línea de Investigación son obligatorios.")
            print("\n" + "-"*50 + "\n")
            
        elif opcion == "3":
            if not mi_grupo.integrantes:
                print("\n[AVISO] Operación inválida. No hay alumnos registrados en el sistema.\n")
                continue
                
            nom_buscar = input("\nIntroduce el Nombre del estudiante a calificar: ").strip()
            encontrado = False
            
            for alum in mi_grupo.integrantes:
                # Filtrado robusto usando isinstance para garantizar consistencia y polimorfismo
                if isinstance(alum, Estudiante) and alum.nombre.lower() == nom_buscar.lower():
                    try:
                        nota = float(input(f"Introduce la calificación para {alum.nombre} (0-100): "))
                        alum.agregar_calificacion(nota)
                        encontrado = True
                        break
                    except ValueError:
                        print("\n[ERROR] Tipo de dato no válido. Debes introducir un número entero o decimal.")
                        encontrado = True
                        break
            
            if not encontrado:
                print("\n[AVISO] Estudiante regular no encontrado. Comprueba que el nombre sea correcto y no pertenezca a Posgrado.")
            print("\n" + "-"*50 + "\n")
                
        elif opcion == "4":
            mi_grupo.generar_reporte()
            input("Presiona Enter para continuar...")
            print("\n" + "-"*50 + "\n")
            
        elif opcion == "5":
            print("\nCerrando el Sistema Gestor Académico de forma segura. ¡Hasta pronto!")
            break
        else:
            print("\n[ERROR] Opción inválida. Por favor, selecciona un número del 1 al 5.\n")

if __name__ == "__main__":
    menu()  