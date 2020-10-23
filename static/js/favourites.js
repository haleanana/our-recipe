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
          <a href="${recipe.url}">
            <img src="${recipe.recipeImage}" class="card-img-top" alt="${recipe.recipeName}"/>
          </a>
          <div class="card-body">
            <h5  id = "recipe-name" class="card-title">${recipe.recipeName}</h5>
            <p class="card-text" id = "recipe-des">${recipe.recipeDescription}</p>
          </div>
          <div class="card-footer text-center">
          <a href="${recipe.url}">
              View recipe
          </a>
          <span id="remove" onclick="removeFavourites('${recipe.id}')"><i class="far fa-trash-alt"></i></span>
          </div>
        </div>
      </div>
    </div>
  `
}
