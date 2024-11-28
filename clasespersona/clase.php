<?php
class Persona {
    protected $nombre;
    protected $edad;

    public function __construct($nombre, $edad) {
        $this->nombre = $nombre;
        $this->edad = $edad;
    }

    public function __toString() {
        return $this->nombre . ", " . $this->edad . " años";
    }
}

class Gerente extends Persona {
    private $responsabilidad;

    public function __construct($nombre, $edad, $responsabilidad) {
        parent::__construct($nombre, $edad);
        $this->responsabilidad = $responsabilidad;
    }

    public function __toString() {
        return parent::__toString() . ", Gerente responsable de " . $this->responsabilidad;
    }
}

class Dueno extends Persona {
    private $propiedad;

    public function __construct($nombre, $edad, $propiedad) {
        parent::__construct($nombre, $edad);
        $this->propiedad = $propiedad;
    }

    public function __toString() {
        return parent::__toString() . ", Dueño de " . $this->propiedad;
    }
}

class Administrativo extends Persona {
    private $departamento;

    public function __construct($nombre, $edad, $departamento) {
        parent::__construct($nombre, $edad);
        $this->departamento = $departamento;
    }

    public function __toString() {
        return parent::__toString() . ", Administrativo del departamento de " . $this->departamento;
    }
}

class Docente extends Persona {
    private $materia;

    public function __construct($nombre, $edad, $materia) {
        parent::__construct($nombre, $edad);
        $this->materia = $materia;
    }

    public function __toString() {
        return parent::__toString() . ", Docente de " . $this->materia;
    }
}

class Maestranza extends Persona {
    private $tareas;

    public function __construct($nombre, $edad, $tareas) {
        parent::__construct($nombre, $edad);
        $this->tareas = $tareas;
    }

    public function __toString() {
        return parent::__toString() . ", Maestranza encargado de " . $this->tareas;
    }
}
