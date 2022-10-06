<h1 align="center">
Scraping Google Search URL
</h1>

## Introduction

Web scraping is a technique for obtaining usable data for a specific purpose. In essence, the website contains a large amount of data, if you want to get that data then one way is by web scraping.

In this post, we will try scraping urls on Google and learn how to optimize searches using the Google search operator.

<img
  alt='Meme'
  src='https://res.cloudinary.com/dlpb6j88q/image/upload/v1650258328/jagad.dev/posts/scraping-google-search-with-python-and-beautifulsoup4/0_Bj_O1jRFzZjKxzi4_pnssel.jpg'
  width='550'
  height='400'
/>

Source Image: [Automating Social Media Contests with Web Scraping | by Jason Yip | Towards Data Science](https://towardsdatascience.com/automating-social-media-contests-with-web-scraping-41c55ff6022a)

## Getting Started

Clone this repository by executing the following command:

```bash
$ git clone https://github.com/jagadyudha/google-scraper
```

Install the libraries that are required by executing the following command:

```bash
# Python3
$ pip3 install -r requirements.txt

# or

# Python2
$ pip install -r requirements.txt
```

Before we jump into how to run the project, we need to know how this project works.

1. Identify google search url
2. Collect data from urls
3. Find `div` tag with class `g`
4. FInd `a` tag inside class that we found in step 3

## How to Run the Project

To run the code is quite simple. Just write the following command:

```bash
# Python3
$ python3 main.py

# or

# Python2
$ python main.py
```

Input pages and input data will be displayed after executing the above command. Input pages is the number of Google pages that you want to scrape it, while input data is the keyword you want to search for.

<img
  alt='Output'
  src='https://res.cloudinary.com/dlpb6j88q/image/upload/v1650265187/jagad.dev/posts/scraping-google-search-with-python-and-beautifulsoup4/output_x6vsfc.png'
  width='765'
  height='208'
/>

## Optimize Search With Google Search Operators

Google search operators are often used to find information that is specific, allowing for accurate search results even when the information is tough to track down.

We may also use the Google search operator in this project. For example, I will find a pdf file with the keyword `learning Python`.

So, I will search with keyword `filetype:pdf intext:learning Python`

<Image
  alt='search with google search operators'
  src='https://res.cloudinary.com/dlpb6j88q/image/upload/v1650268568/jagad.dev/posts/scraping-google-search-with-python-and-beautifulsoup4/Search_with_google_search_operators_mzacyk.png'
  width='1222'
  height='467'
/>

Unfortunately, if you use Google Search Operators too often, it can bring up captchas.

<img
  alt='Use Google Search Operators too often'
  src='https://res.cloudinary.com/dlpb6j88q/image/upload/v1650270958/jagad.dev/posts/scraping-google-search-with-python-and-beautifulsoup4/cons_w5wvru.png'
  width='595'
  height='239'
/>

## Google Search Operators Cheat Sheet

Previously, I have given an example of using Google Search Operators. For more details, you can check out the following cheat sheet: [Google Search Operators Cheat Sheet (notion.site)](https://aged-clave-571.notion.site/Google-Search-Operators-Cheat-Sheet-e0b50566aa2a4dc6a9643dceda52a3a4)

## Conclusion

With the help of this tool, we can do scraping automatically without the need to copy URLs one by one. However, there is an unsolved problem with captcha when using it too often.
