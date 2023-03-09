function change_site_mode(){
    let html = document.querySelector("html");
    let toggle = document.getElementById("toggle");

    if (toggle.value == "off")
    {
        html.setAttribute("data-bs-theme", "light");
        toggle.value = "on"
    }

    else if (toggle.value == "on")
    {
        html.setAttribute("data-bs-theme", "dark");
        toggle.value = "off"
    }
}