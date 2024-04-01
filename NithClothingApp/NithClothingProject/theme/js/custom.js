$('.addToCartBtn').click(function(e){
    e.preventDefault();

    var product_id = $(this).closest('.product_data').find('.prod_id').val();
    var product_qty = $(this).closest('.product_data').find('.prod_qty').val();
    var product_size = $(this).closest('.product_data').find('.product_size').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();
    // console.log("")
    $.ajax({
        method: "POST",
        url: "/addtocart",
        data: {
            'product_id':product_id,
            'product_qty': product_qty,
            'product_size':product_size,
            // 'size_22':size_22,
            // 'size_23':size_23,
            // 'size_24':size_24,
            // 'size_25':size_25,
            // 'size_26':size_26,
            // 'size_27':size_27,
            csrfmiddlewaretoken : token
        },
        dataType:'json',
        success: function (response) {
            alert(response.status);  // Display the status message
        },
    });
    $('.product-close').click(function (e){
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        // var product_qty = $(this).closest('.product_data').find('.prod_qty').val();
        // var product_size = $(this).closest('.product_data').find('.product_size').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url : "dlt_cart_item",
            data : {
                'product_id': product_id,
                csrfmiddlewaretoken : token
            }
        })

    });
}
)