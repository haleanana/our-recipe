/*removes classes to make it responsive on mobile view
This was done as it was not possible for me to use CSS 
to do this*/

/*$(window).on('resize load', function() {
  if ($(window).width() <= 768) { 
    $("#mobile").removeClass("row");
    $("#mobile").removeClass("row-cols-3")
    $("#showRecipeMobile").removeClass('col-4')
    $("#showRecipeMobile2").removeClass('col-8')
  }
});*/
const FAVOURITE_RECIPES = 'FAVOURITE_RECIPES'

function addFavourites(id, url, recipeName, recipeDescription, recipeImage){
    const recipe = {
        id, url, recipeName, recipeDescription,recipeImage
    }

    let favourites = localStorage.getItem(FAVOURITE_RECIPES)
    
    if (favourites) {
        favourites = JSON.parse(favourites)
        if (favourites.some(item => item.id === recipe.id)) return alert('Recipe is already in your favourites')
        favourites.push(recipe)
    } else {
        favourites = [recipe]
    }
    localStorage.setItem(FAVOURITE_RECIPES, JSON.stringify(favourites))
    
}

function removeFavourites(id) {
    let favourites = localStorage.getItem(FAVOURITE_RECIPES)
    if (favourites) {
        favourites = JSON.parse(favourites)
        favourites = favourites.filter(item => item.id !== id)
        localStorage.setItem(FAVOURITE_RECIPES, JSON.stringify(favourites))
        location.reload()
    }
}
