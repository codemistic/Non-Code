# What JWT is used for?
A JWT is used for authorisation, authorisation is making sure that the user that sends a request to your server is the same user that actually logged in during the authentication process.
it's authorizing that a user is an access to this particular system and the way is usually done is by using session.

for example, you have a session ID that you send down in the cookies of the browser and every time the client makes a request they send that session ID up to the server and the server checks its memory that what the user has that session ID it finds that user and it does the authorisation to make sure the user has access.

In JWT instead of cookies, it uses a JSON web token which is what it stands for.



![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/80valj3j1zhtlc56pnj0.png)

first, we're gonna take look at the traditional user login system that uses sessions and cookies to store the user. so the first that happens is the user actually logs in from the client by posting their email and password for example as soon as it gets to the server, the server is going to the authentication to make sure that the user is correct with the email and password it stores that user inside the session which stored in the memory of the server and it gets a unique ID and it sends the ID back to the browser using a cookie so that the browser always has that session ID that it sends up to the server every time It makes a request.
for example, the client makes another request that the session ID gets sent along with the cookie and the server makes the calculations and checks the session memory and checks based on the ID it verifies the user and sends the response back to the browser.


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/poq7lpw0ry1w710pgqig.png)

The other form of authentication is JWT it works very similarly in the beginning, we make a POST request with email and password to the server just like before but instead of storing information on the server inside the session memory what happens is that the server creates a JSON Web Token (JWT) and it signs it with its own secret key so the server knows if you change it then it's invalid it can check that with its secret key.

The main difference here is nothing is stored on the server, the server doesn't store the user, this JWT has all the information about the user built into it. so the server sends JWT back down to the browser and it can choose to store that. for example, it can do cookie storage and it works similarly.

Know the client sends a request to the server and it includes  JSON Web Token so it knows what user s authenticating with it and the server checks the token with its own secret key and it verifies that this web token has not been changed. If the client changed the JSON Web Token and changed the user information then it can say it's invalid but if nothing is changed with JWT and the user is authorized to use that resource it sends the response back to the client.

## Why use JWT?
Now that we talked about how JWT works, and what it is now let's see why would you want to use JWT.
let's take a look at a very simple one of the common use cases of JWT.



![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0u560pu6cgdsv5yvp3a1.png)

Here we have two different serves, we have a bank that owns a server that runs all their banking applications and their banking website and all the baking information, but they also own a separate server and this takes care of all the retirement plans they allow people to invest and do retirement plans on a completely separate web application, but they want their users that login into the bank to also be able to automatically log into their retirement account, so the switch from bank to retirement server they don't want their user to log back in so that it makes it seamless and looks like they are on the same application. This is very common in large-scale industries 

What happens is that when you use a normal session-based server your session is stored in the bank server and not inside the retirement server so the users need to log back in because they need to have their session stored in the retirement server because the session ID from the client is not found in the retirement server.



![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0jepyh4w8qok14ievhbs.png)

But when you use JWT you share the same secret key between the bank and the retirement server and all you need to do is send the same JWT from the client to both of them and you'll be authenticated both times without having to re-log back in.

SO the important thing about JWT is, no matter how many different servers you have no matter how many different applications, or load balancers you have it doesn't matter, the user can authenticate  with any of those servers as long has the same secret key between them.


```
app.post('/api/login', async (req, res) => {
	const { username, password } = req.body
	const user = await User.findOne({ username }).lean()

	if (!user) {
		return res.json({ status: 'error', error: 'Invalid username/password' })
	}

	if (await bcrypt.compare(password, user.password)) {

		const token = jwt.sign(
			{
				id: user._id,
				username: user.username
			},
			JWT_SECRET
		)

		return res.json({ status: 'ok', data: token })
	}

	res.json({ status: 'error', error: 'Invalid username/password' })
})
``` 

above is an example of how you can use JWT for logging a user in the application using a post request in nodejs.
