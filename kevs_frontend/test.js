/* LIBRARIES NEEDED
var axios = require('axios')
const pokemon = require('pokemontcgsdk')
*/



/*
 * This is how we get the data from the previous pages form.
 * 
 * The flow here is this:
 * User goes to the page where they want to add a new pokemon card.
 * User fills out form, using dropdowns for each one except name and HP
 * When they click submit it should route them here, this will call the api
 * with the form data they filled out and return an array of card objects.
 * 
 * Each card object has a name, img, card id etc etc.
 * All we want to do is display the image of all the cards returned by the API,
 * and allow the user to select one! (either with href on photo, radial button 
 * under each photo or something else)
 *
 * Once we know which one is selected, POST the requested data to /api/pokemon_create
 *
 *
 *
 * Some information code for my lovey
 *
 * How to get data from page:
 * handleSubmit(event) {
 *  event.preventDefault();
 *  const data = new FormData(event.target);
 *  const name = data.get('name')
 *
 * VERY INTERESTING:
 * The preventdefault causes submit to not 'submit', meaning it can do all this processing
 * before leaving the page etc
 *
 *
 *
 * How to send data to the pokemon card API:
 * pokemon.card.where({name:'pikachu',hp:'120',types:'lightning,metal',subtype:'stage 1'}
 *
 * How to loop over the returned data
 * pokemon.card.where({name: 'pikachu'})
 * .then(cards => {
 *   cards.forEach(card => {
 *     display(card.imageUrl)
 *   })
 * })
 *




