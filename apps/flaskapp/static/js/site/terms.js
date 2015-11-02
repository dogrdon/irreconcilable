$(function(){

	$('button').click(function(){

		var term = $('#term_text').val().trim();
		var search_url = "http://lookup.dbpedia.org/api/search/PrefixSearch?QueryClass=&QueryString=" + term

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
						$('.results').append('<li><p>'+label+' | ' +uri+ ': ' + desc+'</p></li>')
					}
				}
			},
			error: function(error){
				//if we have an error, then we'll just have to decide what to do.
				alert("something went wrong, check console");
				console.log(error);
			}

		});
	});
});