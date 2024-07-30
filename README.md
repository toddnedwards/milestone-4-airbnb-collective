# Code Institute - Level 5 Diploma in Web Application Development - Milestone Project 4


# My AirBnB Collective

## About The Website

MyAirBnB Collective is an online booking platform for airbnb properties to make life as easy as possible for its users to stay away from home. The interactive website allows users to search through properties of their liking, searching by location and number of bedrooms too to make their journey as easy as possible. 

Users can book a property, add a taxi from the airport to the property, create a profile and look back at their previous bookings as well.

This is something I wanted to create as I sometimes have to travel for work and I liked the idea of having an easy platform, similar to ones that exist but adding extras such as knowing if they're pet friendly etc, and also to organise the taxi for me too so it's one less thing that I have to worry about. 

I liked the idea of this platform for users to potentially add their own properties and be reviewed by admin in the future too.

View the live website [here](https://my-airbnb-collective-57b00b515cab.herokuapp.com/).

# Contents
* [User Experience (UX)](#user-experience)
  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)
  * [Scope Plane](#scope-plane)
    * [Feature Planning](#feature-planning)
  * [Structure Plane](#structure-plane)
    * [User Stories](#user-stories)
    * [Database Schema](#database-schema)
  * [Skeleton Plane](#skeleton-plane)
    * [Wireframes](#wireframes)
  * [Surface Plane](#surface-plane)
    * [Colour Scheme](#colour-scheme)
    * [Typography](#typography)
    * [Imagery](#imagery)
    * [Base Mockup](#base-mockup)
* [Features](#features)
  * [General Features of The Site](#general-features-of-of-the-site)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)
* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Database Used](#database-used)
  * [Frameworks Used](#frameworks-used)
  * [Libraries & Packages Used](#libraries--packages-used)
  * [Programs Used](#programs-used)
  * [Stripe](#stripe)
* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
* [Testing](#testing)
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)


## User Experience

### **Project Goals**

The goal of the myairbnb-collective is to allow users to search through properties depending on location and number of bedrooms, as well as other factors such as pet friendly, wifi facilities etc to suit their needs. 

From here, once the user has chosen the property they like, they can then choose which dates they would like to stay at the property and proceed to checkout to book the property. From here, the user will also be given the option to create an account where they will be able to view their personal details and order history.

If the customer has any issues with their bookings, they also need the ability to contact the admin of the site with any queries, through phone number, email or contact form.

### User Stories

##### Viewing and Navigation

As a shopper:

| I want to...                                            | So I can...                                                                                               |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| See all menu options on all devices clearly             | Navigate easily around the site to find what I want                                                       |
| See the purpose of the site immediately                 | To see if it is a product that I want or not, and understand it quickly before I leave the site           |
| View a list of properties                               | Choose a property that I would like to visit                                                              |
| View the properties locations                           | Decide if it is the right location for me to visit                                                        |
| View facilities such as wifi, pet friendly, parking etc | Decide quickly if it has the facilities that I need quickly, so I can find something suitable to my needs |
| View the properties details individual                  | Find out more about the specific property and its amenities that I wish to potentially book               |
| View a date range                                       | See what dates that I would like to book                                                                  |
| See how much my booking is once I have chosen dates     | See quickly if it is too expensive for me and possibly adjust the dates                                   |

##### Registration And User Accounts

As a registered user/ user about to create an account:

| I want to...                                                               | So I can...                                                                             |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Be able to register an account easily                                      | Have an account to view my profile                                                      |
| Be able to login in to my registered account                               | See my account details                                                                  |
| Recover my password incase I forget                                        | Continue to use my account I have created                                               |
| Receive an email confirmation when registering                             | Confirm that I have entered my correct details and the account will be registered to me |
| Have a user profile                                                        | See my personal information and view order history                                      |
| Be able to save my personal information to my profile when using checkout  | Save time having to enter my details again on future bookings                           |
| Be able to edit my personal information in my profile view                 | Update any change to my personal details or address                                     |
| Be able to logout from my account                                          | Keep my information safe if my device is left unattended                                |



------------

hover effect for properties images provided from:

https://www.geeksforgeeks.org/how-to-zoom-an-image-on-mouse-hover-using-css/

couldn't get crispy forms to work, followed this: https://stackoverflow.com/questions/75495403/django-returns-templatedoesnotexist-when-using-crispy-forms



help with date picker:

https://stackoverflow.com/questions/59450570/how-to-create-start-date-and-end-date-picker-in-one-textbox-using-jquery-and-the


strip time datetime function:

https://www.geeksforgeeks.org/python-datetime-strptime-function/




redirect timeout found at:

https://stackoverflow.com/questions/16890899/how-can-i-make-a-delay-of-5-sec-while-redirecting-one-page-to-another-in-django