function update() {

    const togglePassword = document.querySelector('#togglePassword');
    const password = document.querySelector('#password');

    togglePassword.addEventListener('click', function (e) {
        const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
        password.setAttribute('type', type);
        this.classList.toggle('bi-eye');
    });
    var number = 0;
    document.getElementById("numItem").innerHTML = number;


    for(var i = 1; i<=18; i++){
        item_display(i, "/webpages/assets/placeholder.png", 1, "Item " + i);
    }
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

        
{/* <div class="card w-100 mb-4">
    <div class="card-body">
        <div> <img src="/webpages/assets/placeholder.png" class="card-img img-fluid" width="96" height="350" alt=""> </div>
    </div>
    <div class="card-body bg-light text-center">
        <div class="mb-2">
            <h6 class="font-weight-semibold mb-2"> Item 1</a> </h6>
        </div>
        <h3 class="mb-0 font-weight-semibold">$1</h3>
        <button type="button" class="btn bg-cart"><i class="fa fa-cart-plus mr-2"></i> Add to cart</button>
    </div>
</div> */}
