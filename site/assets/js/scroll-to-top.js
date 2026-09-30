(function() {
    // Créer le bouton
    let btn = document.createElement("button");
    btn.id = "backToTop";
    btn.innerHTML = '<i class="fa-solid fa-arrow-up"></i>';
    document.body.appendChild(btn);

    // Affichage du bouton quand on descend
    window.addEventListener("scroll", function() {
        if (window.scrollY > 200) {
            btn.style.display = "flex";
        } else {
            btn.style.display = "none";
        }
    });

    // Remonter en haut en douceur
    btn.addEventListener("click", function() {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
})();

