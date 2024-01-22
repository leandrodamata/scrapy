First of all, the reason I created this, was because I wanted to help my girlfriend with this sneaker she wanted to buy but thought it was expensive,
So I created this program to track the price of the sneaker and show when it's bellow a specific price.

Here's how to use it

1) change the code to your e-mail: 
in receiver variable, where is written "Insert your email here" put your e-mail to test, and in the last line, where is written "Insert your email here", write your e-mail
2) run the code

I build this using Python and the requests, smtplib, email.message and ssl libraries

The program get's an user agent to use with the requests of the url of the sneakers.
In the urls we can see that almost in every site the products have a code, and with this code, I created a dynamic field url where I can insert the code as a variable called number, 
and with this, create a new link to find the information I wanted on this new page. With the webscrap on the website, the searched data was found, in this case,
the name and price of the sneaker Vans Ultrarange Rapidweld Black White, and also, I put a second sneaker url to show the name and price, but that's just for fun and seeing with it would work.
After getting the data, we store it on a variable that I called productprice1.

Now we start building the e-mail sending part, and in this part is where I had most trouble with... I will explain the problems below now.

The e-mail problem: I learned about the smtplib, email.message and ssl libraries to know how to sent an e-mail with Python,
So I created a gmail just for this and start putting my hands into work and testing this project,
everything was great in the start, but my problem started when I tried to run the code hahaha.
I got a message saying that my username or password was wrong and the program couldn't work properly because of this,
after checking it many times and even changing my password, it still doesn't work, and in this moment I realized it could be anything with the two-step verification.
Now I started searching about it and tryiung to know how it works to solve my problem with the login in the program, but still nothing was resolving it.
And in this moment I saw on my google account that I couldn't work with less safety apps, and that's exatcly what my code was trying to do hahahaha.
So, to solve this, we created and app password inside the new google account, copy it and use this password to access the account that was sending the e-mails.
With this the project worked properly, and now I can run it whenever I want to see if the price went down or not.

Future Ideas: 
- Running it on a server to try it and see how it's going to work
- Using any database to track the price history



