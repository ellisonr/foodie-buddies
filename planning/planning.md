# Wikifoodia

## Why Wikifoodia?

If you're a "foodie" and active on any social media platform, you've probably come across posts from your friends and family and thought to yourself, "I want to dine there the next time I'm in the area." Unforunately, weeks or months go by until you're actually in that area. By that time, you've forgotten who it was that posted about that restaurant you wanted to try and you've forgotten which restaurant it was to begin with.

Personally, during various trips with my wife, I've wished I had documented these restaurants that my friends and family have posted about because I could seldom remember.

This application could serve as a tool for people to share their favorite and most memorable food experiences with other users. Now, users will have a specific place to go to for checking up on great places to eat. Gone are the days of scrolling and scrolling through Instagram and Facebook feeds hoping and wishing to find that one food picture to jog our memory. These food memories will now be easily accessible and shareable.

Note: This started off as FoodieBuddies, but morphed into Wikifoodia.

## Technical Plans

I'll be using Python and Django to create this application. It is the most recent framework we have learned in class, so I'd like further practice on using it. I plan to use SASS for my styling.

### My models will consist of:

#### Restaurant

-  name
-  cuisine
-  street address
-  city
-  state
-  country

#### Menu Item

-  name
-  price
-  description
-  image_url
-  restaurant (foreignkey for restaurant)

#### Comment

-  author (ask for username to be entered)
-  body
-  menu item (foreignkey for menu item)

### MVP:

An application that allows:

-  sign-up
-  log-in

-  create restaurant entry
-  create menu item entries for a single restaurant
-  create comments for menu item entries

-  delete restaurant entry
-  delete menu item entry
-  delete comment

-  update restaurant entry
-  update update menu item entry
-  update comment

### Expected Outcome

It's pretty straightforward, so I hope to just be able to make an application where users can be created and users can sign in. Each user will be able to create a post with description and pictures, but probably just a single picture for now just for MVP. Hopefully, through this project, I'll improve my understanding of what a user would find intuitive and building an application that guides a user instead of leaving guesswork as to what is supposed to happen next.

### Extra Features to Shoot For:

-  Picture Uploading instead of using image URL's
-  Favorites/adding to favorites
-  The use of tags
