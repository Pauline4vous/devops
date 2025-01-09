/**
 * @event scroll
 * Logo disappears on window scrolling
 */
$(window).scroll(function () {
    $("#logo-img").css("opacity", 1 - $(window).scrollTop() / 50);
});

/**
 * Function to collapse item descriptions on cards
 * Creates an array from all elements with the same class
 * Loops through the array and toggles visibility
 * @event click
 */
function collapsingCards() {
    const cardCollapse = Array.from(
        document.getElementsByClassName("card-collapse")
    );

    cardCollapse.forEach((card) => {
        card.addEventListener("click", function (e) {
            e.preventDefault();
            const collapsedContent = card.nextElementSibling;
            collapsedContent.style.display =
                collapsedContent.style.display === "block" ? "none" : "block";
        });
    });
}

collapsingCards();

/**
 * @event keyup
 * Search bar functionality to filter items by name or description
 */
const searchInput = document.getElementById("search-bar");
if (searchInput) {
    searchInput.addEventListener("keyup", function () {
        const query = searchInput.value.toLowerCase();
        const cards = Array.from(document.getElementsByClassName("card"));
        cards.forEach((card) => {
            const title = card.querySelector(".card-title").innerText.toLowerCase();
            const description = card
                .querySelector(".card-text")
                .innerText.toLowerCase();
            if (title.includes(query) || description.includes(query)) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }
        });
    });
}
