Hi I'm [Ifeoma Igwe](https://www.linkedin.com/in/ifeoma-igwe-69b84b16b/) and I wanted to document how you can avoid an error I kept getting when trying to read a csv file in google colab.
Reading csv files in python is one of the simplest things to do but can get very frustrating when you get encoding errors, or human readable characters have been converted to special characters only understood by a computer.

So, first things first, what is encoding? Apparently, since Python 3.0, characters in strings are represented by a code point. This encoding means to represent a unicode string as a string of bytes instead and this is done by calling the encode() method.  

# Encoding types
There's different unicode encoding types including:
- UTF-8
- UTF-16
- UTF-32
- ISO-8859-1

# Encoding in Python
Python's default encoding type is utf-8, meaning when you're reading a csv file without specifying a different encoding type, utf-8 is what will be used. 
This should read your file easily uless there are special characters in the file that cannot be decoded by utf-8, in which case you run into the error below:
"UnicodeDecodeError: 'utf8' codec can't decode byte 0x80 in position 3131: invalid start byte."

I understood that the UnicodeDecodeError meant utf8 was the wrong encoding and on some ocassions was able to read the files by specidying other encoding types such as "ISO-8859-1." However, even though I was able to successfully read the file in python, there would be special characters that did not make any sense.
A special character for example is when a word like "'" is converted to "â€™" so that a word like "I'm" looks like " Iâ€™m." I've had large files of scraped social media data and some sentences don't even make sense i.e. they look like this, "I need the whole story man because etf ðŸ˜‚ðŸ˜‚ðŸ˜‚" it can be very annoying to do topic modelling or build wordclouds with.
It's also possible to open the file in binary mode, which I don't like to do because it makes it impossible for me to work with as I don't understand that format.

So I spent days reading about unicoding and encoding, trying to find the solution to the problem. After wasting time looking for ways to transform those characters to the right format in python, I realized the problem was local, especially when I open csv files in excel without importing it. Doing this messes up the characters in the file because mac has its own encoding type.

After knowing this, I tried importing files to my excel and transforming to utf8 format but this didn't work either because my excel version is outdated and the new version is not compatible with my old mac either.

# Solution
Okay now that I understood the problem, there are three steps I now take before uploading my file in google colab:
- Step 1: Download the csv file without opening it in excel 
- Step 2: Open the file with numbers (on mac)
- Step 3: Export the file as csv with utf8 format

And just like that, the solution turned out to be much simpler than I thought!



# References
1. [Types of encoding techniques](https://www.javatpoint.com/types-of-encoding-techniques)
2. [Unicode Howto](https://docs.python.org/3/howto/unicode.html#:~:text=UTF%2D8%20is%20one%20of,used%20than%20UTF%2D8.)
3. [Python string encode()](https://www.programiz.com/pythonprogramming/methods/string/encode#:~:text=Since%20Python%203.0%2C%20strings%20are,process%20is%20known%20as%20encoding.)
