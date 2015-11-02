$(function(){

	$('#search').click(function(){
		$('#results').empty();
		var term = $('#term_text').val().trim();
		var search_url = "http://lookup.dbpedia.org/api/search/PrefixSearch?QueryClass=&MaxHits=50&QueryString=" + term

		console.log("searching on" + search_url)
		
		$.ajax({
			beforeSend: function(request){
				request.setRequestHeader("Accept", "application/json")
			},
			url: search_url, 
			type: 'GET',
			success: function(response){
				//if we get results back, we want to display them and a new form for sending back to flask
				results = response['results'];
				for (var i in results){
					if (results.hasOwnProperty(i)){
						var item = results[i];
						var label = item['label'];
						var uri = item['uri'];
						var desc = item['description'];
						$('#results').append('<input type="radio" name="choice" value="' + uri  + '">"'
												+ label + ': '
												+ desc
												+ '</input><br/>');
					}
				}
				$('#results').prepend('<button id="confirm" type="button">Confirm Selection</button><br/>');
			},
			error: function(error){
				//if we have an error, then we'll just have to decide what to do.
				alert("something went wrong, check console");
				console.log(error);
			}

		});
	});
	
	$('#confirm').click(function(){
		//user clicks here when they've selected the most fitting option
		var choice = $('form input[type=radio]:checked').val();
		alert('are you sure you want to send'+choice+'?');
		
		//prep the data for posting

		$.ajax({
			url: '/add_term',
			type: 'POST',
			data: "Noting",//the data that we are posting to the server
			success: function(response){},
			error: function(error){}
		})
	});

});