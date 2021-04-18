/*globals $:false, moment:false, jQuery: false */

// ==UserScript==
// @name         Get Item Names
// @namespace    
// @version      0.1
// @description  Converts a table of items into a usable string for the item filter
// @author       Chelyocarpus
// @match        https://pathofexile.fandom.com/wiki/List_of_helmets
// @icon         https://www.google.com/s2/favicons?domain=fandom.com
// @grant        none
// @require      https://code.jquery.com/jquery-3.3.1.min.js
// @require      https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.22.2/moment.min.js
// ==/UserScript==
//moment().format("HH:mm:ss") + ": " +

//wait until document has finished loading, then start the function
$( document ).ready( myFunction );

var DEBUG = true;
var cars = [];

function log(msg) {
    if (DEBUG) {
        console.log(msg);
    }
}

function myFunction(jQuery) {
    let amountOfItems = $(".wikitable tbody:eq(0) tr").length - 1
    log(amountOfItems)

    for (let i = 1; i <= amountOfItems; i++) {
        var nameOfItem = $("tbody tr:eq("+i+") td span span a").text();
        log(nameOfItem)

        cars[i - 1] = nameOfItem;
        log(cars)
    }
}

 $("tbody tr").click(function () {
     let product = $('a', this).html();
     let infRate = $('.i',this).html();
     let note = $('.n',this).html();
     log(product);
 });
