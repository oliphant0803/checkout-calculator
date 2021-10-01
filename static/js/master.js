var server = "http://127.0.0.1:5000";
var number = 0;
$('#numItem').html(number);
function update() {

    const togglePassword = document.querySelector('#togglePassword');
    const password = document.querySelector('#password');

    togglePassword.addEventListener('click', function (e) {
        const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
        password.setAttribute('type', type);
        this.classList.toggle('bi-eye');
    });
    // var number = 0;
    // document.getElementById("numItem").innerHTML = number;
    for(var i = 1; i<=18; i++){
        item_display(i, "/static/assets/placeholder.png", 1, "Item " + i);
    }
    get_cart_num(server, number);
}

function item_display (i, image, p, name){
    var itemDisplay = document.createElement("div");
    itemDisplay.setAttribute("class", "card w-100 mb-4");
    var cardDisplay = document.createElement("div");
    cardDisplay.setAttribute("class", "card-body");
    var cardImageContainer = document.createElement("div");
    var cardImage = document.createElement("img");
    cardImage.src = image;
    cardImage.setAttribute("class", "card-img img-fluid");
    cardImage.width = 96;
    cardImage.height = 350;
    cardImageContainer.appendChild(cardImage);
    cardDisplay.appendChild(cardImageContainer);
    itemDisplay.appendChild(cardDisplay);
    var cardBodyContainer = document.createElement("div");
    cardBodyContainer.setAttribute("class", "card-body text-center");
    var cardBody = document.createElement("div");
    cardBody.setAttribute("class", "mb-2")
    var itemTitle = document.createElement("h6");
    itemTitle.setAttribute("class", "font-weight-semibold mb-2");
    var itemName = name;
    itemTitle.innerHTML = itemName;
    cardBody.appendChild(itemTitle);
    cardBodyContainer.appendChild(cardBody);
    var priceTitle = document.createElement("h3");
    priceTitle.setAttribute("class", "mb-0 font-weight-semibold");
    var price = p;
    priceTitle.innerHTML = "$" + price;
    cardBodyContainer.appendChild(priceTitle);
    var cartButton = document.createElement("button");
    cartButton.type = "button";
    cartButton.setAttribute("class", "btn bg-cart");
    var cart = document.createElement("i");
    cart.setAttribute("class", "fa fa-cart-plus mr-2");
    cartButton.appendChild(cart);
    cartButton.innerHTML = "Add to Cart";
    cardBodyContainer.appendChild(cartButton);
    itemDisplay.appendChild(cardBodyContainer);
    document.getElementById(i).appendChild(itemDisplay);
}

function get_cart_num(){
} $(function(){
    $("#1").click(function() {
        console.log(number);
        $.ajax({
            type: "POST",
            url: server+"/sum",
            data:JSON.stringify(number),
            dataType: 'json'
        }).done(function(data) {
            console.log(data);
            number = data;
            $('#numItem').html(data);
        });
    });
});

function update_cart_num(){

}
