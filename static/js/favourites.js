$(function() {
    loadFavourites();
});
function loadFavourites() {
    let favourites = localStorage.getItem(FAVOURITE_RECIPES)
    if (favourites) {
        favourites = JSON.parse(favourites)
        let recipeItems = ""
        favourites.forEach(recipe => {
            recipeItems += recipeItem(recipe)
        })
        $('#favourites-wrapper').empty().append(recipeItems)
    }
}

function recipeItem(recipe) {
    return `
  <div class="col mb-4">
        <div class="card h-100">
          <a href="${recipe.url}"><img class="card-img-top" src="${recipe.recipeImage}" alt= /></a>
          <div class="card-body">
            <h5 id="recipe-name">${recipe.recipeName}</h5>
            <p class="card-text" id="recipe-des">${recipe.recipeDescription}</p>
            <a href="${recipe.url}"><div class="card-footer text-center">
              View recipe
            </div>
            </a>
          </a>
        </div>
      </div>
  </div>
  `
}