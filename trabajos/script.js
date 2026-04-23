const botonAgregar = document.getElementById("btn-agregar");
const botonLimpiar = document.getElementById("btn-limpiar");
const listaProyectos = document.getElementById("lista-proyectos");
const botonesDetalle = document.querySelectorAll("button[data-action='ver-detalles']");
const botonTip = document.getElementById("btn-tip");
const resultadoTip = document.getElementById("resultado-tip");
const formContacto = document.getElementById("form-contacto");
const mensajeEnviado = document.getElementById("mensaje-enviado");
const themeToggle = document.getElementById("theme-toggle");
const switchLabel = document.getElementById("switch-label");

const tips = [
  "Toma 3 respiraciones profundas antes de empezar una tarea importante.",
  "La regla 2 minutos: si tarda menos de 2 minutos hazlo ya.",
  "Coloca tus dispositivos fuera del alcance para concentrarte mejor.",
  "Cada viernes revisa y actualiza tus metas de la semana.",
];

let indiceTip = 0;

function mostrarTip() {
  indiceTip = (indiceTip + 1) % tips.length;
  resultadoTip.querySelector("p").innerText = tips[indiceTip];
}

botonTip.addEventListener("click", mostrarTip);

botonAgregar.addEventListener("click", () => {
  const idea = prompt("Ingresa una nueva idea para la lista:");
  if (!idea) return;
  const item = document.createElement("li");
  item.textContent = idea;
  const btnEliminar = document.createElement("button");
  btnEliminar.textContent = "Eliminar";
  btnEliminar.className = "btn-tertiary";
  btnEliminar.addEventListener("click", () => item.remove());
  item.appendChild(btnEliminar);
  listaProyectos.appendChild(item);
});

botonLimpiar.addEventListener("click", () => {
  if (confirm("¿Estás seguro de que quieres borrar todas las ideas?")) {
    listaProyectos.innerHTML = "";
  }
});

botonesDetalle.forEach((btn) => {
  btn.addEventListener("click", () => {
    const detalle = btn.dataset.item;
    alert(`🔍 Detalles de: ${detalle}\n\nDescripción: Sigue los pasos prácticos para implementar el proyecto con facilidad.`);
  });
});

formContacto.addEventListener("submit", (evento) => {
  evento.preventDefault();
  mensajeEnviado.classList.remove("hidden");
  formContacto.reset();
  setTimeout(() => mensajeEnviado.classList.add("hidden"), 3200);
});

function aplicarTema(oscuro) {
  if (oscuro) {
    document.documentElement.classList.add("dark-mode");
    switchLabel.textContent = "Modo oscuro";
    themeToggle.checked = true;
  } else {
    document.documentElement.classList.remove("dark-mode");
    switchLabel.textContent = "Modo claro";
    themeToggle.checked = false;
  }
}

function iniciarTema() {
  const preferencia = localStorage.getItem("modo-tema");
  const quiereOscuro = preferencia ? preferencia === "oscuro" : window.matchMedia("(prefers-color-scheme: dark)").matches;
  aplicarTema(quiereOscuro);
}

themeToggle.addEventListener("change", () => {
  const activo = themeToggle.checked;
  aplicarTema(activo);
  localStorage.setItem("modo-tema", activo ? "oscuro" : "claro");
});

iniciarTema();

const carouselTrack = document.getElementById("carousel-track");
const carouselItems = Array.from(document.querySelectorAll(".carousel-item"));
const btnPrev = document.getElementById("prev-slide");
const btnNext = document.getElementById("next-slide");
const carouselStatus = document.getElementById("carousel-status");

let indiceCarousel = 0;

function actualizarCarousel() {
  carouselItems.forEach((item, index) => {
    item.classList.toggle("active", index === indiceCarousel);
  });
  carouselStatus.textContent = `Slide ${indiceCarousel + 1} de ${carouselItems.length}`;
}

btnPrev.addEventListener("click", () => {
  indiceCarousel = (indiceCarousel - 1 + carouselItems.length) % carouselItems.length;
  actualizarCarousel();
});

btnNext.addEventListener("click", () => {
  indiceCarousel = (indiceCarousel + 1) % carouselItems.length;
  actualizarCarousel();
});

setInterval(() => {
  indiceCarousel = (indiceCarousel + 1) % carouselItems.length;
  actualizarCarousel();
}, 5000);

actualizarCarousel();

const paletteButtons = Array.from(document.querySelectorAll(".palette-btn"));

const paletas = {
  azul: {
    "--primary": "#3b82f6",
    "--primary-dark": "#1d4ed8",
    "--secondary": "#60a5fa",
    "--accent": "#0284c7"
  },
  verde: {
    "--primary": "#10b981",
    "--primary-dark": "#0f766e",
    "--secondary": "#34d399",
    "--accent": "#059669"
  },
  purpura: {
    "--primary": "#8b5cf6",
    "--primary-dark": "#7c3aed",
    "--secondary": "#a78bfa",
    "--accent": "#c084fc"
  },
  naranja: {
    "--primary": "#f97316",
    "--primary-dark": "#ea580c",
    "--secondary": "#fb923c",
    "--accent": "#f59e0b"
  }
};

function aplicarPaleta(nombre) {
  const config = paletas[nombre];
  if (!config) return;
  Object.entries(config).forEach(([variable, valor]) => {
    document.documentElement.style.setProperty(variable, valor);
  });
  localStorage.setItem("paleta-colores", nombre);
  paletteButtons.forEach((btn) => btn.classList.toggle("selected", btn.dataset.palette === nombre));
}

paletteButtons.forEach((boton) => {
  boton.addEventListener("click", () => {
    aplicarPaleta(boton.dataset.palette);
  });
});

function iniciarPaleta() {
  const paletaGuardada = localStorage.getItem("paleta-colores") || "azul";
  aplicarPaleta(paletaGuardada);
}

iniciarPaleta();


