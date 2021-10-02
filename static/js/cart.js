var server = "http://127.0.0.1:5000";
var name_info = [
    "item 1", "item 2", "item 3", "item 4", "item 5", "item 6",
    "item 7", "item 8", "item 9", "item 10", "item 11", "item 12",
    "item 13", "item 14", "item 15", "item 16", "item 17", "item 18"
];
var img_info = [
    "/static/assets/placeholder.png", "/static/assets/placeholder.png", "/static/assets/placeholder.png", 
    "/static/assets/placeholder.png", "/static/assets/placeholder.png", "/static/assets/placeholder.png",
    "/static/assets/placeholder.png", "/static/assets/placeholder.png", "/static/assets/placeholder.png", 
    "/static/assets/placeholder.png", "/static/assets/placeholder.png", "/static/assets/placeholder.png",
    "/static/assets/placeholder.png", "/static/assets/placeholder.png", "/static/assets/placeholder.png", 
    "/static/assets/placeholder.png", "/static/assets/placeholder.png", "/static/assets/placeholder.png"
];
var price_info = [
    1, 2, 3, 4, 5, 6, 7, 8, 9,
    10, 11, 12, 13, 14, 15, 16, 17, 18
];

var discount_code = [
    "OLIBAKA01", "OLIBAKA02", "OLIBAKA03",
    "OLIBAKA04", "OLIBAKA05", "OLIBAKA06"
];

var discount_amount = [
    0.8, 0.9, 0.9, 0.5, 0.8, 0.7
];

var shipping_option = [
    "Same-Day $15.00",
    "Fast $10.00",
    "Standard $5.00"
];

var shipping_amount = [
    15, 10, 5
];


var ids = [];
var prices = [];
var itemNum = [];
var imgs = [];
var itemnames = [];
var discount = 1;
var shipping = 0;

function cartUpdate() {

    get_ids();
    get_prices();
    get_item_counts();
    get_item_imgs();
    get_item_names();

    for (var i = 0; i<prices.length; i++){
        listenCartUpdate(ids[i], imgs[i], itemnames[i], itemNum[i], prices[i]);
    }

    get_num_item();
    updateSummary();
}

function updateSummary(){
    get_shipping();
    calculate_discount();
    console.log(discount);
    calculatePrice();
}

function calculate_discount(){
    let input = document.getElementById('code').value;
    input=input.toUpperCase();
    console.log(input);
    for (var i = 0; i< discount_code.length; i++){
        if (discount_code[i] == input){
            discount = discount_amount[i];
        }
    }
}

function get_shipping(){
    let input = document.getElementById('shipping').value;
    console.log(input);
    for (var i = 0; i< shipping_option.length; i++){
        if (shipping_option[i] == input){
            shipping = shipping_amount[i];
        }
    }
}

function get_ids(){
} $(function(){
    postData = {};
    $.ajax({
        type: "POST",
        url: server+"/getids",
        data: postData,
        datatype: 'json'
    }).done(function(data){
        console.log(data);
        ids = data;
    });
});

function get_prices(){
} $(function(){
    postData = {};
    $.ajax({
        type: "POST",
        url: server+"/getprices",
        data: postData,
        datatype: 'json'
    }).done(function(data){
        console.log(data);
        prices = data;
    });
});

function get_item_counts(){
} $(function(){
    postData = {};
    $.ajax({
        type: "POST",
        url: server+"/getcounts",
        data: postData,
        datatype: 'json'
    }).done(function(data){
        console.log(data);
        itemNum = data;
    });
});

function get_item_imgs(){
} $(function(){
    postData = {};
    $.ajax({
        type: "POST",
        url: server+"/getimgs",
        data: postData,
        datatype: 'json'
    }).done(function(data){
        console.log(data);
        imgs = data;
    });
});

function get_item_names(){
} $(function(){
    postData = {};
    $.ajax({
        type: "POST",
        url: server+"/getnames",
        data: postData,
        datatype: 'json'
    }).done(function(data){
        console.log(data);
        itemnames = data;
    });
});

function listenCartUpdate(id, image, name, numItem, price) {
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
    deleteDiv.setAttribute("id", id);
    deleteDiv.onclick = function(){listenDelete(id)};
    var numDiv = document.createElement("a");
    numDiv.innerHTML = numItem;
    var addDiv = document.createElement("a");
    var addKey = document.createElement("i");
    addKey.setAttribute("class", "icon fas fa-plus add");
    addDiv.appendChild(addKey);
    addDiv.setAttribute("id", id);
    addDiv.onclick = function(){listenAdd(id)};
    col4Div.appendChild(deleteDiv);
    col4Div.appendChild(numDiv);
    col4Div.appendChild(addDiv);
    mainRow.appendChild(col4Div);
    var col5Div = document.createElement("div");
    col5Div.setAttribute("class", "col value");
    col5Div.innerHTML = "$" + price;
    var removeKey = document.createElement("i");
    removeKey.setAttribute("class", "far fa-trash-alt remove");
    removeKey.setAttribute("id", id)
    removeKey.onclick = function(){listenDeleteAll(id)};
    col5Div.appendChild(removeKey);
    mainRow.appendChild(col5Div);
    newRow.appendChild(mainRow);
    document.getElementById("cart-items").appendChild(newRow);
}

function get_num_item(){
} $(function(){
    postData = {};
    $.ajax({
        type: "POST",
        url: server+"/cartnum",
        data: postData,
        datatype: 'json'
    }).done(function(data){
        console.log(data);
        number = data;
        document.getElementById("numItem").innerHTML = number;
        document.getElementById("numItemCart").innerHTML = number;
        document.getElementById("numItemSummary").innerHTML = number;
    });
});

function calculatePrice(){
    var totalPrice = 0.00;
    for (var i=0; i<prices.length; i++){
        totalPrice += prices[i]; 
    }
    if (totalPrice != 0){
        totalPrice = parseFloat(totalPrice + shipping) * parseFloat(discount);
    }
    document.getElementById("beforeTaxPrice").innerHTML = Math.round(totalPrice * 100) / 100;;
    document.getElementById("tax").innerHTML = Math.round(totalPrice * 0.13 * 100) / 100;
    document.getElementById("total").innerHTML = Math.round(totalPrice * 1.13 * 100) / 100;
}

function listenAdd(id){
    var curr_id = parseInt(id);
    console.log(curr_id);
    $.ajax({
        type: "POST",
        url: server+"/addincart",
        data: "id=" + curr_id
    });
    location.reload();
} 

function listenDelete(id){
    var curr_id = parseInt(id);
    console.log(curr_id);
    $.ajax({
        type: "POST",
        url: server+"/deleteincart",
        data: "id=" + curr_id
    });
    location.reload();
}

function listenDeleteAll(id){
    var curr_id = parseInt(id);
    console.log(curr_id);
    $.ajax({
        type: "POST",
        url: server+"/removeincart",
        data: "id=" + curr_id
    });
    location.reload();
}