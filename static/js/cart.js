function cartUpdate() {

    const togglePassword = document.querySelector('#togglePassword');
    const password = document.querySelector('#password');

    togglePassword.addEventListener('click', function (e) {
        const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
        password.setAttribute('type', type);
        this.classList.toggle('bi-eye');
    });
    document.getElementById("numItem").innerHTML = number;
    document.getElementById("numItemCart").innerHTML = number;
    document.getElementById("numItemSummary").innerHTML = number;

    var prices = [1, 1, 1];
    var itemsNum = [1, 1, 1];

    listenCartUpdate("/static/assets/placeholder.png", "Item 1", itemsNum[0], prices[0]);
    listenCartUpdate("/static/assets/placeholder.png", "Item 2", itemsNum[1], prices[1]);
    listenCartUpdate("/static/assets/placeholder.png", "Item 3", itemsNum[2], prices[2]);

    calculatePrice(prices, itemsNum);
}

function listenCartUpdate(image, name, numItem, price) {
    var newRow = document.createElement("div");
    newRow.setAttribute("class", "row border-top border-bottom");
    var mainRow = document.createElement("div");
    mainRow.setAttribute("class", "row main align-items-center");
    var col2Div = document.createElement("div");
    col2Div.setAttribute("class", "col-2");
    var imageContainer = document.createElement("img");
    imageContainer.src = image;
    imageContainer.setAttribute("class", "img-fluid");
    col2Div.appendChild(imageContainer);
    mainRow.appendChild(col2Div);
    var col3Div = document.createElement("div");
    col3Div.setAttribute("class", "col");
    var row3Div = document.createElement("div");
    row3Div.setAttribute("class", "row");
    row3Div.innerHTML = name;
    col3Div.appendChild(row3Div);
    mainRow.appendChild(col3Div);
    var col4Div = document.createElement("div");
    col4Div.setAttribute("class", "col");
    var deleteDiv = document.createElement("a");
    var deleteKey = document.createElement("i");
    deleteKey.setAttribute("class", "icon fas fa-minus delete");
    deleteDiv.appendChild(deleteKey);
    var numDiv = document.createElement("a");
    numDiv.innerHTML = numItem;
    var addDiv = document.createElement("a");
    var addKey = document.createElement("i");
    addKey.setAttribute("class", "icon fas fa-plus add");
    addDiv.appendChild(addKey);
    col4Div.appendChild(deleteDiv);
    col4Div.appendChild(numDiv);
    col4Div.appendChild(addDiv);
    mainRow.appendChild(col4Div);
    var col5Div = document.createElement("div");
    col5Div.setAttribute("class", "col value");
    col5Div.innerHTML = "$" + price;
    var removeKey = document.createElement("i");
    removeKey.setAttribute("class", "far fa-trash-alt remove");
    col5Div.appendChild(removeKey);
    mainRow.appendChild(col5Div);
    newRow.appendChild(mainRow);
    document.getElementById("cart-items").appendChild(newRow);
}

function summaryUpdate(){

}

function calculatePrice(prices, itemsNum){
    var totalPrice = 0;
    for (var i=0; i<prices.length; i++){
        totalPrice += prices[i] * itemsNum[i]; 
    }
    document.getElementById("beforeTaxPrice").innerHTML = totalPrice;
    document.getElementById("tax").innerHTML = Math.round(totalPrice * 0.13 * 100) / 100;
    document.getElementById("total").innerHTML = Math.round(totalPrice * 1.13 * 100) / 100;
}