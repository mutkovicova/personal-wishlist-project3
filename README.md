# Wishlist project

The purpose of this project is to create a wishlist for a user to populate with products, or experiences, they would like to purchase.

Am I responsive screenshot here.

## Table of Contents

1. [Data modeling](#data-modeling)
2. [Design](#design)
3. [Debugging](#debugging)
4. [Technologies used](#technologies-used)
5. [Credit](#credit)

## Data modeling

![data model](/assets/readme-files/wishlist-data-model.png)

The wishlist items will each have certain input fields, ranging from basic integer fields like id to boolean fields which identify whether the item is considered luxury by the user.

These data fields allow a user to have an overview of each wishlist item, and relate back to the categories when required.

## Design

The intent for this was to be simple, clean and utilitarian. As a wishlist, the purpose is to have a way to add, edit, and delete items. This does not need over-the-top design, for now.

I did however decide to deviate slightly from the original taskmanager material by putting the menu items on the right in the navbar, as that felt natural to me based on website etiquette.

I also decided to make the button to add items go to the right, as that is naturally where I would see action.

I utilised Materialize cards, using in particular the simple card layout as well as adding the tabs to hide action items (such as edit and delete) so that these items couldn't be accidentally edited or deleted. I wanted those actions to be further away from a users touch. Mock up from Materialize below:

![card design](assets/readme-files/card-wireframe.png)

Finally, the colour choices were designed to be simple.

## Testing

### Lighthouse

![lighthouse testing](assets/readme-files/lighthouse-testing.png)

Lighthouse testing came back with green across the board so I feel satisfied with this. Especially with 93% accessibility, when considering the yellow and white of the tabs.

### Python validator

[PEP8 validator](https://www.pythonchecker.com/) suggested changes to spacing around a function and equal signs in parameters. The GitPod editor does not likes this, but I have implemented PEP8 recommendations.
The only other thing that I have ignored is that a line shouldn't be too long, as I did not want to have a singular function over 2 lines, as it makes it personally less legible to me while working with it.

## Debugging

### Cards

Materialize handily provided a code to initialise these cards via JavaScript (which I didn't think I'd need again!) if you read the initial paragraph more closely, and hidden behind another link, so I did this and it solved my issue.

### Card tabs

I wanted my cards to have tabs for the additional information and editing capability, in order to make the interface cleaner for the user. This however was hampered by these tabs not working. After resolving a similar issue on the cards initially, I went searching Stack Overflow and found that in fact, even though it is not documented, the tabs do need a JS script to initialise and I implemented this. [Stack Overflow source](https://stackoverflow.com/questions/40677831/materialize-css-tabs-are-not-working). After this, a singular card worked, but not all the others, so I had a look at the previous JS code to figure out how it applied to all and just added All onto the end of my querySelector.

### Icons

This is a weird one and it was purely discovered through trial and error, but while choosing icons on Font Awesome, I tried other styles in the 5.15.4 version and unless they started with 'fas', they did not display. So if replacing, choose an icon starting with fas if possible.

## Technologies used

### [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)

HTML5 was used for basic structure of the site.

### [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3)

CSS3 was used minimally to fix issues with formatting in certain areas.

### [Materialize 1.0.0](https://materializecss.com/)

The Materialize framework was utilised to create the cards, buttons and general standard formatting of the site.

### [Flask](https://flask.palletsprojects.com/en/2.2.x/)

Flask was used to kickstart the Python logic in this app and provide a starting point.

### [Python](https://www.python.org/)

Python was used to create the database integration.

### Am I Responsive?

Am I Responsive? was used to create the screenshot for the finished project.

### [Font Awesome 5.15.4](https://fontawesome.com/)

Font Awesome was used to add a little bit of interest to the form, as well as the buttons, across the site.

## Future development

Order by date and time created:
didn't have time to figure this out this time around



## Credit

Massive credit given to Tim at Code Institute and the walkthrough for the Relational Databases module. This wishlist is an amended version of his task manager and some standard bits of code (such as those in the app.py file) are borrowed directly from his work.

Secondly, a big thank you to my friend Ariela for once again sitting down with me and helping me through this project. I personally found the pivot from JavaScript to Python quite difficult, and she is actually a .NET developer so appreciated the learning opportunity. Together, we figured bugs out and learned a lot!



## Gitpod Reminders

### HTMl, CSS, JS

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

### Python

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

### Heroku

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to Account Settings in the menu under your avatar.
2. Scroll down to the API Key and click Reveal
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

### Troubleshoot

THE THING:
set_pg

IF psql not working
