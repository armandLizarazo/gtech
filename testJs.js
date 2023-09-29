// script.js

// Define un objeto JavaScript que contiene la información relacionada.
var informacionRelacionada = {
  opcion1: "Esta es la información para la Opción 1.",
  opcion2: "Aquí tienes detalles sobre la Opción 2.",
  opcion3: "La Opción 3 tiene su propia descripción.",
};

// Obtiene el elemento de la lista desplegable y el párrafo donde se mostrará la información.
var lista = document.getElementById("palabras");
var informacion = document.getElementById("informacion");

// Agrega un event listener para detectar cambios en la selección.
lista.addEventListener("change", function () {
  var seleccion = lista.value; // Obtiene el valor seleccionado.

  // Muestra la información relacionada en el párrafo.
  informacion.textContent = informacionRelacionada[seleccion];
});
