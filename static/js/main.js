// courtesy of Simen Daehlin from my first milestone, via https://codepen.io/Eventyret/pen/RXBNaJ
/**
 * @event scroll
 * Logo disappear on window scrolling 
 */
$(window).scroll(function(){
    $("#logo-img").css("opacity", 1 - $(window).scrollTop() / 50);
});

/**
 * Function to collapse item description on card
 * Creating array from all elements with same class
 * Looping through array
 * @event click 
 */
function collapsingCards(){
    let cardCollapse = Array.from(document.getElementsByClassName("card-collapse"));

cardCollapse.forEach(card => {
    card.addEventListener("click", function(e){
    e.preventDefault();
    let collapsedContent = card.nextElementSibling;
    if(collapsedContent.style.display === "block"){
        collapsedContent.style.display = "none";
    } else collapsedContent.style.display = "block";
});
});
}

collapsingCards();