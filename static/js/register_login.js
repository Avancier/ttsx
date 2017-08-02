/**
 * Created by xyt on 17/8/2.
 */


	$('#user_name_reg').blur(function() {

		name = $(this).val();
		$.ajax({
			method: "GET",
			url: "check_name",
			data: {"name": name},
			dataType: "json"
		}).done(function (data) {
			var b =data["body"]
			alert(typeof b);
			if(b == "1"){

			}
        });

	});