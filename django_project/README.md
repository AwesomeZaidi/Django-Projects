# LoginPAY


## Demo
![](demo.gif)


LoginPAY is an appt that allows all kinds of users of all walks of life to LOG In and PAY Me. It's that easy. LoginPAY is a Python, Django project I developed while learning the framework.

## Project Structure

The project consists of 3 main apps

### Users

Users can can register, login, logout, and view their profile.

### Blog

The funny thing about this app is, initially this was where our app started. Make School started out at Make Games With Us, YouTube was a online video dating platform, so I guess all great ideas gotta start from somewhere!

This app allows users to view more about the app, see the home screen the reads Blog records from the database in chronological order.

We have a Post model for each blog that  has a title, content and linked to an Author.

### Payments

Payments app comes into place when a user logs in, then can go to their PAYMe navigation tab. This app utilies a third party API, Stripe to allow users to send money to me.

## Moving Forward

Moving forward, I would like to get more comfortable with Django REST Framework for future apps, deployment and connected a front end like React or React Native.
