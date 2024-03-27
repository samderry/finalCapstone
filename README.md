<h1 align="center">finalCapstone - Sentiment Analysis</h3>

<!-- TABLE OF CONTENTS -->
## Table of Contents
<ol>
  <li><a href="#description">Description</a></li>
  <li><a href="#prerequisites">Prerequisites</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#credits">Credits</a></li>
</ol>
<br/>

## Description
This project generates sentiment analysis. The task involved analysing the sentiment 
of a sample set of customer reviews for Amazon products. The dataset comprises 28,332 products reviews 
including basic product information, rating, review text, and more for each product. The analysis required that 
the dataset review text be cleaned prior to processing.

The dataset was pre-processed by selecting only the product review text, and removing any records with a 
missing product review. Prior to determining the sentiment for each review, the text was converted to 
lowercase, stripped of any leading whitespace characters, and cleaned of identifiable stop words to try and 
reduce the quantity of redundant content from the review.
<br/>
<br/>

## Prerequisites
1. Install module 'spacy'
```
pip install spacy
```
2. Install module 'spacytextblob'
```
pip install spacytextblob
```
3. Install module 'pandas'
```
pip install pandas
```
4. Install simple model package
```
python -m spacy download en_core_web_sm
```
<br/>

## Installation

Clone the repo
```
git clone https://github.com/samderry/finalCapstone
```

<!-- USAGE -->
## Usage

> [!IMPORTANT]
> The data file contained in 'amazon_product_reviews.zip' must be extracted to the project folder before running the program
<br/>

Run the program
```
python sentiment_analysis.py
```
<br/>


The program should output up to 10 entries from each category of sentiment.

> ![#00FF00](https://placehold.co/15x15/00FF00/00FF00.png) Positive

> ![#FFB401](https://placehold.co/15x15/FFB401/FFB401.png) Neutral

> ![#FF0000](https://placehold.co/15x15/FF0000/FF0000.png) Negative

<br/>

The program output should appear as below.
<br/>
<br/>
![image](https://github.com/samderry/finalCapstone/assets/154550636/8baed101-6650-4f5f-bab0-37d9bda1365b)

<!-- CREDITS -->
## Credits
Sam Derry
