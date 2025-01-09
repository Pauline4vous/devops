<h1 align="center">

<a href="https://freecycle.net/" target="_blank"><img src="https://i.ibb.co/vYK0KB8/Screenshot-2020-03-10-at-1-14-15-AM.png" alt="Freecycle Mockup"/></a>

</h1>

<div align="center">

<a href="https://freecycle.net/" target="_blank"><img src="https://i.ibb.co/4ZfmYSJ/logo-2.png" width='200' height='150' alt="Freecycle logo"></a>

</div>

Table of Contents
Introduction
How to Freecycle
Freecycling Etiquette
What to Freecycle
Including a Photo
Writing a Freecycle Post
UX
Strategy: Why and what?
Scope: Features
Existing Features
Planned Features
Skeleton: Presentation
Surface: Design
Technology Used
Deployment
Testing
Credits
<h2 id="introduction">Introduction</h2>

Freecycle is a grassroots and entirely nonprofit movement that connects people looking to give away unwanted items with people who need those items—for free. The platform allows members to exchange items within their local communities, helping reduce waste, preserve resources, and keep useful items out of landfills.

<h2 id="how-to-freecycle">How to Freecycle</h2>

Freecycling involves three simple steps:

Find a group near you: Use the Recycling Group Finder to locate nearby groups. If no groups are available, consider starting one through platforms like the Freecycle Network or others like the ReUseIt Network and Sharing Is Giving.
Post items or requests: Groups typically allow four types of posts:
Offer: Let others know what you’re giving away.
Taken: Inform others that the item has been claimed.
Wanted: Request an item you need.
Found: Let others know you’ve received an item.
Check before buying: Before purchasing an item, check if someone in your group is offering it for free. Similarly, give away items before discarding them.
<h2 id="freecycling-etiquette">Freecycling Etiquette</h2>

Be respectful and courteous to other members.
Communicate promptly when responding to posts.
Avoid spam and irrelevant content.
Ensure the items you offer are clean and safe to use.
<h2 id="what-to-freecycle">What to Freecycle</h2>

You can freecycle almost anything, as long as it’s legal, safe, and in usable condition. Examples include:

Furniture
Electronics
Clothes
Household items
For more ideas, visit the What to Freecycle page.

<h2 id="including-a-photo">Including a Photo</h2>

Adding a photo to your post increases the chances of your item being taken. Ensure the image is clear and accurately represents the item.

<h2 id="writing-a-freecycle-post">Writing a Freecycle Post</h2>

Follow these tips when creating a post:

Provide a clear and concise title (e.g., "Offer: Wooden Table").
Include a detailed description of the item, including its condition.
Specify your location and preferred method of pickup.
<h2 id="ux">UX</h2>

Strategy: Why and What?
Primary Target Audience
Freecycle is targeted at individuals and families who are environmentally conscious and wish to reduce waste while benefiting from free exchanges.

Goals of the Platform
To provide an easy-to-use platform to give away and receive items for free.
To foster a sense of community and encourage sustainable living.
To reduce waste and promote the reuse of items.
<h2 id="scope-features">Scope: Features</h2>

Existing Features
User Posts: Members can create posts to offer, request, or claim items.
Search Functionality: Filter items by location and category.
Local Groups: Members can join groups specific to their towns or regions.
Volunteer Moderators: Groups are moderated to ensure a safe and respectful environment.
Planned Features
Interactive Map: Display item locations on a map for easier discovery.
Private Messaging: Enable members to communicate securely within the platform.
Donation Support: Allow users to donate to support the platform’s operations.
<h2 id="skeleton-presentation">Skeleton: Presentation</h2>

The platform is designed with simplicity and usability in mind. Key features include:

A homepage with recent posts and announcements.
A search bar for finding items by category or location.
Clear navigation links to groups, posts, and user profiles.
<h2 id="surface-design">Surface: Design</h2>

Color Scheme
Primary Color: Soft green (#6cbb5a) to reflect eco-friendliness.
Secondary Color: White (#ffffff) for a clean and minimalistic look.
Typography
Font Family: Arial, Helvetica, sans-serif for readability.
Logo
The logo features a recycling symbol integrated with the platform name, symbolizing sustainability and reuse.

<h2 id="technology-used">Technology Used</h2>

Frontend: HTML, CSS, JavaScript
Backend: Python (Flask), MongoDB
Deployment: Heroku, AWS
<h2 id="deployment">Deployment</h2>

Local Deployment Steps:

Clone the repository:
bash

Copy
git clone https://github.com/username/freecycle.git
Install dependencies:
bash

Copy
pip install -r requirements.txt
Create a .env file with the following variables:
bash

Copy
MONGO_URI=<your-mongo-uri>
SECRET_KEY=<your-secret-key>
Run the application:
bash

Copy
python app.py
<h2 id="testing">Testing</h2>

The platform has been tested across various browsers and devices for responsiveness, functionality, and user experience. Key tests include:

Registration/Login: Ensured users can create accounts and log in securely.
Post Creation: Verified that users can create, edit, and delete posts.
Search Functionality: Tested the search feature for accuracy and speed.
<h2 id="credits">Credits</h2>

Freecycle Network: Inspiration for the platform’s concept and design.
Open Source Libraries: Bootstrap, Flask, and MongoDB were used to build the platform.
