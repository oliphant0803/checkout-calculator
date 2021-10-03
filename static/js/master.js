var server = "0.0.0.0";
var number;

var name_info = [
    "LED bulb 806", "LED bulb 800", "LED bulb 600", "LED bulb 450", "LED bulb 380", "LED bulb 400",
    "LED spotlight", "LED abinet", "Remote Control", "Gateway", "Wireless Dimmer", "Control Outlet",
    "Motion Sensor", "Signal Repeater", "Dimmer kit", "Remote Control Kit", "Control Outlet Kit", "Gateway Kit E12"
];
var img_info = [
    "/static/assets/1.png", "/static/assets/2.png", "/static/assets/3.png", 
    "/static/assets/4.png", "/static/assets/5.png", "/static/assets/6.png", 
    "/static/assets/7.png", "/static/assets/8.png", "/static/assets/9.png", 
    "/static/assets/10.png", "/static/assets/11.png", "/static/assets/12.png", 
    "/static/assets/13.png", "/static/assets/14.png", "/static/assets/15.png", 
    "/static/assets/16.png", "/static/assets/17.png", "/static/assets/18.png"
];
var price_info = [
    11.99, 19.99, 14.99, 17.99, 16.99, 14.99, 7.99, 25.00, 17.99,
    29.99, 7.99, 14.99, 14.99, 14.99, 9.99, 29.99, 19.99, 99.00
];
function update() {

    for(var i = 0; i<18; i++){
        var id = i+1;
        item_display(id, name_info[i], img_info[i], price_info[i]);
    }
    get_cart_num();
}

function item_display(id, name, img_src, price){
    var item_image = document.getElementById("img-item"+id);
    item_image.src = img_src;
    var price_tag = document.getElementById("price-tag"+id);
    price_tag.innerHTML = price;
    var name_tag = document.getElementById("name-tag"+id);
    name_tag.innerHTML = name;
}

function get_cart_num(){
    number = update_cart_num();
} $(function(){
    $(".bg-cart").click(function() {
        console.log(this.id);
        id = parseInt(this.id) - 1;
        postData = {
            item_id: id+1,
            name: name_info[id], 
            price: price_info[id], 
            img_src:  img_info[id]
        };
        console.log(postData);
        $.ajax({
            type: "POST",
            url: "/sum",
            data: postData,
            dataType: 'json'
        }).done(function(data) {
            console.log(data);
            number = data;
            $('#numItem').html(number);
        });
    });
});

function update_cart_num(){
} $(function(){
    postData = {};
    $.ajax({
        type: "POST",
        url: "/cartnum",
        data: postData,
        datatype: 'json'
    }).done(function(data){
        console.log(data);
        number = data;
        $('#numItem').html(number);
    });
});

function search_item() {
    let input = document.getElementById('searchbar').value
    input=input.toLowerCase();
    let x = document.getElementsByClassName('card');
    for (i = 0; i < x.length; i++) { 
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            x[i].parentElement.style.display = "none";
        }
        else {   
            x[i].parentElement.style.display = "flex";            
        }
    }
}
