function showTab(tab) {
  const ogc = document.getElementById("ogcTab");
  const sos = document.getElementById("sosTab");

  if (tab === "ogc") {
    ogc.style.display = "block";
    sos.style.display = "none";

    //  CRITICAL FIX
    setTimeout(() => {
      if (window.map) {
        map.updateSize();
      }
    }, 100);
  } else {
    ogc.style.display = "none";
    sos.style.display = "block";
  }

  // update active button
  document
    .querySelectorAll(".tab-btn")
    .forEach((btn) => btn.classList.remove("active"));
  event.target.classList.add("active");
}
