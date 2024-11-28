class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'{self.nombre}, {self.edad} años'

class Gerente(Persona):
    def __init__(self, nombre, edad, responsabilidad):
        super().__init__(nombre, edad)
        self.responsabilidad = responsabilidad

    def __str__(self):
        return f'{self.nombre}, {self.edad} años, Gerente responsable de {self.responsabilidad}'

class Dueño(Persona):
    def __init__(self, nombre, edad, propiedad):
        super().__init__(nombre, edad)
        self.propiedad = propiedad

    def __str__(self):
        return f'{self.nombre}, {self.edad} años, Dueño de {self.propiedad}'

class Administrativo(Persona):
    def __init__(self, nombre, edad, departamento):
        super().__init__(nombre, edad)
        self.departamento = departamento

    def __str__(self):
        return f'{self.nombre}, {self.edad} años, Administrativo del departamento de {self.departamento}'

class Docente(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def __str__(self):
        return f'{self.nombre}, {self.edad} años, Docente de {self.materia}'

class Maestranza(Persona):
    def __init__(self, nombre, edad, tareas):
        super().__init__(nombre, edad)
        self.tareas = tareas

    def __str__(self):
        return f'{self.nombre}, {self.edad} años, Maestranza encargado de {self.tareas}'

