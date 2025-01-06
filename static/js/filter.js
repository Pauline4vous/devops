/**
 * @event onchange
 * Fetching category selected in dropdown bar in html
 * Sending selection to Python for query backend database
 * Receiving filtered data back and calling function to loop through
 * @callback <loopItems>
 */
    const selectCat = document.getElementById("search-category");
    const card = document.getElementById("card-item");

    selectCat.onchange = function() {
        cat = selectCat.value;
    
        fetch(`${window.origin}/items/filter`, {
            method: "POST",
            body: JSON.stringify(cat),
            cache: 'no-cache',
            headers: new Headers({
                "content-type": "application/json"
            })
        })
        .then(function(response) {
            response.json().then(function(data){
                loopItems(data);
            });
        })
        .catch(function(err){
            console.log(err);
            alert(`Error: ${err}. To return to the main page, go to ${location.hostname}`);
        });
    };

/**
 * Looping through @param {array} Array of filtered items
 * Removing id hex number from object to construct url for editing item inside template literal
 * @callback <injectCard> to append html template to an empty variable
 * Injecting ID element with new html
 * @callback <collapsingCards> so new filtered template can also collapse
 */
function loopItems(data) {
     cardContent = '';
    data.forEach(item => {
        itemId = item._id.$oid;
        cardContent += injectCard(item);
    });
    $("#card-item").html(cardContent);
    collapsingCards();
}

/**
 * Switch function to return specific icon classes depending of item category
 * @param {object} Item with keys and values, including category to be used for switch
 */
function whichCat(item){
    let itemCat = item.item_category;
    switch(itemCat) {
        case 'Outdoor':
            return 'fa-cloud-sun';
            break;
        case 'Kids':
            return 'fa-child';
            break;
        case 'Household':
            return 'fa-home';
            break;
        case 'Other':
            return 'fa-random';
            break;
        default:
            return;
    }
}

/**
 * Function to inject html to a variable using template literals
 * @callback <whichCat> to have specific icon to add to html depending of category
 * @param {object} Item to add its keys and values to html
 */
function injectCard(item) {
    whichCat(item);
    cardHtml = `
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
                            <a type='button' class='card-collapse light-text px-0 mx-0'>
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
                    ${(() => {
                        if (item.item_img){
                            return `<div class="card-img-contain text-left mb-3">
                                        <img src="${item.item_img}" class="card-img-top card-img" alt="Item Image">
                                    </div>`;
                        }
                    })()}
                    <div class="row my-3">
                        <div class="col-12">>
                            <a href="mailto:${item.item_contact}" class="card-link">Contact</a>
                            <span class="card-subtitle mt-0">${item.username}</span>
                        </div>
                    </div>
                    <div class="row my-3">
                        <div class="col-12">
                            <a href="/items/update/${itemId}" class="btn bg-darkgreen light-text">Edit</a>
                        </div>
                    </div>
				</div>
			</div>
		</div>
        `;
        return cardHtml;
}
