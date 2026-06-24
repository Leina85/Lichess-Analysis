document.getElementById("stats-form").addEventListener("submit", handle_submit);

function handle_submit(event) {
    event.preventDefault();

    if (document.getElementById("show-win-stats").checked) {
        let element = document.getElementById("winner-section");
        element.classList.remove("hidden");
    }else {
    document.getElementById("winner-section").classList.add("hidden");
    }

    if (document.getElementById("show-eco-stats").checked) {
        let element = document.getElementById("eco-section");
        element.classList.remove("hidden");
    }else {
    document.getElementById("eco-section").classList.add("hidden");
    }

    if (document.getElementById("show-opening-stats").checked) {
        let element = document.getElementById("opening-section");
        element.classList.remove("hidden");
    }else {
    document.getElementById("opening-section").classList.add("hidden");
    }

    if (document.getElementById("show-termination-stats").checked) {
        let element = document.getElementById("termination-section");
        element.classList.remove("hidden");
    }else {
    document.getElementById("termination-section").classList.add("hidden");
    }

    if (document.getElementById("show-moves-stats").checked) {
        let element = document.getElementById("moves-section");
        element.classList.remove("hidden");
    }else {
    document.getElementById("moves-section").classList.add("hidden");
    }
}