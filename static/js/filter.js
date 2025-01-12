/**
 * @event onchange
 * Fetching category selected in the dropdown bar in HTML
 * Sending selection to Flask backend via query parameters
 * Receiving filtered data back and calling the function to loop through
 * @callback <loopItems>
 */
const selectCat = document.getElementById("search-category");
const card = document.getElementById("card-item");

selectCat.onchange = function () {
    const cat = selectCat.value;
    const searchQuery = new URLSearchParams(window.location.search).get("search") || ""; // Get current search query

    // Create URL with query parameters for filtering
    const filterUrl = `${window.origin}/?search=${searchQuery}&item_category=${cat}`;

    fetch(filterUrl, {
        method: "GET",
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json",
        }),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then((data) => loopItems(data))
        .catch((err) => {
            console.error(err);
            alert(`Error: ${err}. Please refresh the page or return to the main page.`);
        });
};

/**
 * Looping through @param {array} Array of filtered items
 * Removing id hex number from the object to construct the URL for editing the item inside a template literal
 * Rebuilding the card content dynamically and injecting it into the DOM
 * @callback <collapsingCards> so new filtered templates can also collapse
 */
function loopItems(data) {
    let cardContent = "";
    data.forEach((item) => {
        cardContent += injectCard(item);
    });
    card.innerHTML = cardContent;
    collapsingCards(); // Ensure collapsing functionality applies to the new cards
}

/**
 * Switch function to return specific icon classes depending on item category
 * @param {object} item - The item object with keys and values, including category
 */
function whichCat(item) {
    const itemCat = item.item_category;
    switch (itemCat) {
        case "Outdoor":
            return "fa-cloud-sun";
        case "Kids":
            return "fa-child";
        case "Household":
            return "fa-home";
        case "Other":
            return "fa-random";
        default:
            return "";
    }
}

/**
 * Function to inject HTML into a variable using template literals
 * @callback <whichCat> to add a specific icon to the HTML depending on the category
 * @param {object} item - The item object to add its keys and values to the HTML
 */
function injectCard(item) {
    const cardHtml = `
        <div class="col-12 col-sm-6 col-lg-4">
            <div class="card my-2 text-center">
                <div class="card-body p-0">
                    <div class="row my-3">
                        <div class="col-10 px-0">
                            <h3 class="card-title text-uppercase mb-4">${item.item_name}</h3>
                        </div>
                        <div class="col-2 mt-2">
                            <h5 class="card-subtitle mb-4">
                                <i class="fas ${whichCat(item)}"></i>
                            </h5>
                        </div>
                    </div>
                    <div class="row my-3">
                        <div class="col">
                            <a type="button" class="card-collapse light-text px-0 mx-0">
                                <h6>Find more info about this item...<i class="pl-2 fas fa-chevron-down"></i></h6>
                            </a>
                            <p class="card-text collapsed-content text-left px-0 mx-0 lgreen-text">${item.item_description}</p>
                        </div>
                    </div>
                    <div class="row my-3">
                        <div class="col">
                            <h6>Can be collected in ${item.item_location}</h6>
                        </div>
                    </div>
                    ${
                        item.item_img
                            ? `<div class="card-img-contain text-left mb-3">
				<img src="${item.item_img}" class="card-img-top card-img" alt="Item Image">
                              </div>`
                            : ""
                    }
                    <div class="row my-3">
                        <div class="col-12">
                            <a href="mailto:${item.item_contact}" class="card-link">Contact</a>
                            <span class="card-subtitle mt-0">${item.username}</span>
                        </div>
                    </div>
                    <div class="row my-3">
                        <div class="col-12">
                            <a href="/items/update/${item._id.$oid}" class="btn bg-darkblue white-text">Edit</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
    return cardHtml;
}
