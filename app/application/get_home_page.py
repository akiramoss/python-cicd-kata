from fastapi.responses import HTMLResponse

PAGINA = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Python CI/CD Kata</title>
<style>
  :root { --naranja: #f2a20c; --azul: #6dc5e9; --azul-oscuro: #3fa9d4; --gris: #37474f; --suave: #f0f3f5; }
  * { box-sizing: border-box; }
  body {
    margin: 0; min-height: 100vh; display: grid; place-items: center;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; color: var(--gris); background: #fff; overflow: hidden;
  }
  .circulo { position: fixed; border-radius: 50%; z-index: -1; }
  .c1 { width: 70vmin; height: 70vmin; background: var(--naranja); right: -25vmin; top: -20vmin; }
  .c2 { width: 28vmin; height: 28vmin; background: var(--azul); left: -8vmin; bottom: -8vmin; }
  .tarjeta {
    background: #fff; border-radius: 24px; padding: 48px 56px; text-align: center;
    box-shadow: 0 20px 60px rgba(55, 71, 79, 0.15); max-width: 90vw;
  }
  h1 { margin: 0 0 8px; font-size: 28px; }
  p { margin: 0 0 32px; color: #5e6b75; }
  .dado {
    width: 160px; height: 160px; margin: 0 auto 32px; border-radius: 28px; background: var(--suave);
    display: grid; place-items: center; font-size: 88px; font-weight: 800;
  }
  .dado.gira { animation: gira 0.4s ease; }
  @keyframes gira { from { transform: rotate(-90deg) scale(0.6); } to { transform: rotate(0) scale(1); } }
  button {
    border: 0; border-radius: 999px; padding: 14px 32px; font-size: 18px; font-weight: 700;
    color: #fff; background: var(--naranja); cursor: pointer; font-family: inherit;
  }
  button:hover { filter: brightness(1.05); }
  .pie { margin-top: 24px; font-size: 14px; }
  .pie a { color: var(--azul-oscuro); }
</style>
</head>
<body>
<div class="circulo c1"></div>
<div class="circulo c2"></div>
<main class="tarjeta">
  <h1>Python CI/CD Kata</h1>
  <p>Una API muy sencilla que tira un dado.</p>
  <div class="dado" id="dado">?</div>
  <button id="tirar">Tirar el dado</button>
  <div class="pie"><a href="/docs">Ver la API en /docs</a></div>
</main>
<script>
  const dado = document.getElementById("dado");
  document.getElementById("tirar").addEventListener("click", async () => {
    try {
      const respuesta = await fetch("/dice/roll");
      const valor = await respuesta.json();
      dado.classList.remove("gira");
      void dado.offsetWidth;
      dado.textContent = valor;
      dado.classList.add("gira");
    } catch {
      dado.textContent = "!";
    }
  });
</script>
</body>
</html>
"""


def get_home_page() -> HTMLResponse:
    return HTMLResponse(content=PAGINA)
