<h2 align = "center">Our Recipe</h2>

<p align ="center">An online communal cookbook<br>
This website was designed so anyone can browse through tasty recipes as well as submit and share their own tasy recipe.
Purposefully done to be clean and simple; users can navigate very easily so they can either try someone else's recipe or share theirs to others.
</p>

## Table of Contents

[**Demo**](#demo)

[**UX**](#ux)

[**Technologies Used**](#technologies-used)

[**Testing**](#testing)

[**Bugs and Fixes**](#bugs-and-fixes)

[**Deployment**](#deployment)

[**Credits**](#credits)

## Demo

<a href= "https://our-recipe.herokuapp.com/" target= "_blank">Live Demo</a>

<img width = "100%" src = "static/img/mockup/demo.gif">

[**back to top**](#table-of-contents)
## UX

### Goals

The goal of this website is to create a user submitted library of recipes that is unique and with a "non-commercial" feel. Clean and simple, users should feel like they are cooking 
recipes from their grandparents, parents, friends and people close to them. 

### Target audience goals

This website is catered for people who loves to cook recipes with a "local" feel regardless of age and gender.

User needs:
- Selection of unique, non-commercial and user submitted recipes.
- Be able to share their own recipe.
- Simple and clean design.
- Free from ads, blogs and other "clutter".
- Easy to navigate in any device.

How this website meets their needs:
- Users are able to submit their own recipe.
- Growing collection of user submitted recipes to choose from.
- Design is simple and clean but still visually appealing.
- No blogs , unneccessary clutter or ads.
- The design such as a fixed Navbar makes its very easy to navigate around.

### Goals as a developer
- Expand my portfolio.
- Practice my Python ,Database and Framework skills as well as refresh my HTML,CSS and JS skills.
- A communal online cookbook with a collection of unique and user submitted recipes.
- Increase users which will also grow the number of recipes available.

### User stores

As a user, what I would want in a recipe website:
1. Direct and easy way to get to the recipe I want.
2. A number of recipes to choose from.
3. Submit and contribute my own recipes.
4. For recipes to have that "home-made" feel.
5. Access the website from any device.

### Research

I visited a number of recipes website for inspiration and to discover what works and what doesnt. I personally find it irritating that when I pick a recipe, 
I have to scroll past blogs and photos before getting to the information Im after. I also found that most recipes have a restaurant and commercial feel 
to it.

### Design choices

**Colour scheme**
- The initial colour design (refer to [**Wireframe**](#wireframes)) leaned towards a feminine feel so the colours were changed.
- The primary colours for this website are #fff , #51808B and different shades of grey. The colours are chosen because they are gender neutral 
so it caters to all users regardless of gender.
- The colour combination also presents a clean and simple looking website because the colours are not too "strong".

**Fonts**
- Intially, I used Pacifico:cursive for the header fonts. I decided to change the fonts as this was not reflective of my design goals.
- I'm using Poppins as my main font as this presents a much simpler and cleaner feel which is one of my design goals.

**Ease of use**
- Navbar is fixed at the top so users will always have access to the main/important pages.

**Recipes Page**
- Initial design was to display the available recipes (name and cooking time) in a collapsible accordion. The design was updated to cards as
the collapsible accordion simply did not allow me to provide enough information for the users browsing through the recipes page.
- Cards are nows used to display the available recipes as this allows me to display a lot more information to the user such as images, short description, prep time and etc.
- Cards also provide a cleaner and less cluttered look which reflects the "clean" look goal.
- Search bar added so users can quickly search recipes.

**Footer**
- Footer was added to the final design. The footer section allows me to put navlinks at the bottom of the page which will increase ease of use for users.

### Wireframes

Figma was used to create my mock ups.

**Mock up Home**
<img src = "static/img/mockup/mockuphome.png">

**Mock up view recipe page**
<img src = "static/img/mockup/mockuprecipe.png">

**Mock up add recipe page**
<img src = "static/img/mockup/mockupaddrecipe.png">


[**back to top**](#table-of-contents)

## Features

- [x] Users are able to add their own recipes.
- [x] Users are able to edit and update recipes.
- [x] Search bar for recipes where users can search any keyword related to the recipe that they want.
- [x] Time stamps for updated and added recipes.
- [x] Newest recipe will be the first on the recipe list.
- [x] Newly added recipes will have a "New" tag. This will disappear the day after its posted.
- [x] Ability to add recipes on Favourites.
- [x] Recipes already in Favourites will have the Favourites button disabled and the text will say "Favourited".
- [x] Fixed Navbar so users can always find their way around.
- [x] Form validation.
- [x] Users can subscribe with their email. 
- [x] Collapsible navbar on mobile view.
- [x] Jumbotron with "Hello" animated in different languages.
- [x] Footer with access to navlinks and social links.
- [x] Recipe library displayed in cards with images.

## Features to add

- [ ] User registry and login.
- [ ] Users are only able to update and delete recipes if it was submitted by them.
- [ ] The option to filter recipes by category, cooktime, preptime and etc.
- [ ] Pagination for when the library grows.
- [ ] Weekly automated emails for subsribers.
- [ ] Ability to rate the recipes and users to comment.
- [ ] More information such as servings, calories , nutrition value and etc.
- [ ] Admin access to delete, edit and update recipes.
- [ ] Admin ability to review recipes before website displays it.
- [ ] The ability to upload a photo file instead of a url.
- [ ] Auto-sizer and optimizer for photos.
- [ ] Improve Search feature.

[**back to top**](#table-of-contents)

## Technologies used

**HTML** - To create the foundation and structure of my website. <br>
**CSS** - To add styles and make my website visually appealing.<br>
**Figma** - To create the wireframe of my website.<br>
**Javascript** - To expand the capability and interactivity of my website.<br>
**Python** - The core language used in this project.<br>
**Flask, Jinja, Pymongo** - Frameworks used for this project to help tie everything together.<br>
**Bootstrap CDN** - Components from BS library heavily used in this website.<br>
**MongoDB/Atlas** - To store and grab user submitted data for my website.<br>
**GitHub**- To store and share this project.<br>
**Heroku** - To deploy my website.<br>
**Font Awesome**- To access the icons that I wanted for this website.<br>
**Gitpod**- To write my code using their IDE.<br>

## Testing 

### Validated through:

- [W3C Markup Validation]( https://validator.w3.org/) for HTML.
- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) for CSS.
- [JSHint](https://jshint.com/) for JavaScript.
- [Autoprefixer CSS]( https://autoprefixer.github.io/) for browser compatibility.

### Tested through 

- Google Lighthouse
- [Mobile Friendly Test - Result](https://search.google.com/test/mobile-friendly?id=9Plrf2ZSoX8vpdkyxBGLeA)
- Chrome developer tools
- [BrowserStack](https://www.browserstack.com/)

**Testing was done by me and 6 users**

The following scenarios were tested:

1. **Submit recipe and Update button**
- All buttons 

