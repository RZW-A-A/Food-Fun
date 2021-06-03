var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var foodId = this.dataset.food
		var action = this.dataset.action
		console.log('foodId:', foodId, 'Action:', action)
		console.log('USER:', user)

        if (user == 'AnonymousUser'){
			console.log("login to cart")
			addCookieItem(foodId, action)

		}else{
		    // logged in user
			updateUserOrder(foodId, action)
		}
	})
}

function updateUserOrder(foodId, action){
	console.log('User is authenticated, sending data...')

	var url = '/updateitem/'

	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({'foodId':foodId, 'action':action})
	})
	.then((response) => {
		  return response.json();
	})
	.then((data) => {
		  location.reload()
	});
}

function addCookieItem(foodId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[foodId] == undefined){
		cart[foodId] = {'quantity':1}

		}else{
			cart[foodId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[foodId]['quantity'] -= 1

		if (cart[foodId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[foodId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"

	location.reload()
}
