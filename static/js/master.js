var server = "http://127.0.0.1:5000";
var number = 0;
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
$('#numItem').html(number);
function update() {

    const togglePassword = document.querySelector('#togglePassword');
    const password = document.querySelector('#password');

    togglePassword.addEventListener('click', function (e) {
        const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
        password.setAttribute('type', type);
        this.classList.toggle('bi-eye');
    });

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
            url: server+"/sum",
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

}
