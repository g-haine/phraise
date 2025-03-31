// assets/js/counter.js
const namespace = "phraise";
const key = "{{ page.url | slugify }}";

fetch(`https://api.countapi.xyz/hit/${namespace}/${key}`)
.then(res => res.json())
.then(data => {
  document.getElementById("hit-counter").innerText = `Visits: ${data.value}`;
});
