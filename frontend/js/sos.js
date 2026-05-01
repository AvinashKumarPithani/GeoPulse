async function loadSOS() {
  const res = await fetch("http://127.0.0.1:8000/observations/xml");
  const xmlStr = await res.text();

  const parser = new DOMParser();
  const xml = parser.parseFromString(xmlStr, "text/xml");

  const obs = xml.getElementsByTagName("Observation");
  const tbody = document.querySelector("#sosTable tbody");

  tbody.innerHTML = "";

  for (let i = 0; i < obs.length; i++) {
    tbody.innerHTML += `
      <tr>
        <td>${obs[i].getElementsByTagName("sensor_id")[0].textContent}</td>
        <td>${obs[i].getElementsByTagName("temperature")[0].textContent}</td>
        <td>${obs[i].getElementsByTagName("humidity")[0].textContent}</td>
        <td>${obs[i].getElementsByTagName("wind_speed")[0].textContent}</td>
        <td>${obs[i].getElementsByTagName("pressure")[0].textContent}</td>
      </tr>
    `;
  }
}