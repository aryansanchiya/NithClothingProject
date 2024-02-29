$(document).ready(function(response){

    $('.paywithrazorpay').click(function (e){
        e.preventDefault();

        var firstname = $("[name='firstname']").val();
        var lastname = $("[name='lastname']").val();
        var address = $("[name='address']").val();
        var city = $("[name='city']").val();
        var state = $("[name='state']").val();
        var country = $("[name='country']").val();
        var code = $("[name='code']").val();
        var phone = $("[name='phone']").val();
        var token = $("[name='csrfmiddlewaretoken']").val();
        if(firstname == "" || lastname == "" || address == "" || city == "" || state == "" || country == "" || code == "" || phone == ""){
            // swal("Alert!","All fields are mandatory", "error");
            alert("error")
            return false;
        }
        else{
            // console.alert(fname)
            $.ajax({
                method : "GET",
                url : "/proceed_to_pay",
                dataType : "json",
                // datatype : "datatype",
                success: function (response){
                    var options = {
                        "key": "rzp_test_xftiEQRdK00lAf", // Enter the Key ID generated from the Dashboard
                        "amount": response.total_price * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "NithClothing",
                        "description": "Test Transaction",
                        "image": "https://example.com/your_logo",
                        // "order_id": "order_IluGWxBm9U8zJ8", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (responseb){
                            alert(responseb.razorpay_payment_id);
                            $.ajax({
                                method: "POST",
                                url: "placeorder",
                                headers:{
                                    "X-CSRFToken": token
                                },
                                data:  {
                                'firstname': firstname,
                                'lastname': lastname,
                                'address':address,
                                'city': city,
                                'state': state,
                                'country': country,
                                'code': code,
                                'phone': phone,
                                'payment_id': responseb.razorpay_payment_id,
                                'csrfmiddlewaretoken': token,
                                } ,
                                success: function (responseb) {
                                    window.location.href = '/home'
                                } 
                            });
                        },
                        "prefill": {
                            "name": firstname+ " "+lastname,
                            // "email": "gaurav.kumar@example.com",
                            "contact": phone
                        },
                        // "notes": {
                        //     "address": "Razorpay Corporate Office"
                        // },
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();
                }
            
            });
        }
    });
});