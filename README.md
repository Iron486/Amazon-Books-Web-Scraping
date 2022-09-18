# Amazon Books Web Scraping
 [Amazon most popular data science related books dataset](https://www.kaggle.com/datasets/die9origephit/amazon-data-science-books).

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F6372737%2Fc913ddc103f20c3668a67eda7a92336b%2Famazon-text-books.jpg?generation=1663537491733005&alt=media)


The dataset contains 946 books obtained from scraping [Amazon](https://www.amazon.com) books related to data science, statistics, data analysis, Python, deep learning and machine learning. <br>
You can find this dataset on [Kaggle](https://www.kaggle.com/datasets/die9origephit/amazon-data-science-books) or directly [here](https://github.com/Iron486/Amazon-Books-Web-Scraping/blob/main/spiders/final_book_dataset_kaggle.csv). <br>
It includes 18 columns:


- **title**: title of the book
- **author**: author (or the authors) of the book
- **price**: price (in dollars)
- **pages**: number of pages
- **avg_reviews**: average reviews (out of 5)
- **n_reviews**: reviews done for each book
- **star5**: percentage of 5 star reviews
- **star4**: percentage of 4 star reviews
- **star3**: percentage of 3 star reviews
- **star2**: percentage of 2 star reviews
- **star1**: percentage of 1 star reviews
- **dimensions**: size of the book (in inches)
- **weight**: weight (in pounds or ounces)
- **language**: language of the book
- **publisher**: publisher
- **ISBN-13**: ISBN_13 code
- **link**: link of the Amazon book
- **complete_link**: complete link of the Amazon book (including the domain `https://amazon.com`)

###  **Inspiration**

You can perform an exploratory data analysis of the dataset, working with `Pandas` or `Numpy`.
Interesting visualizations can be performed too using, for instance, Python libraries to plot the different features.
This dataset can be also used to practice queries using `SQL` or `Pandas`.
Moreover, you can also rank the books based on the number of positive reviews or you can explore the dataset to have a reference for buying data-science-related books in the future. <br>

**Remember to star the repository if you found the dataset useful :)**.

###  **Collection methodology**

The dataset was obtained through web scraping from Amazon.

More than 1700 books were scraped, fetching the most important information for each book.
Duplicated were deleted, each column has been formatted and made easy to use for data analysis purposes.
Links with a lot of missing values were deleted, and in some cases, were filled with an appropriate value based on the column. Therefore, the total number of books passed from 1788 to 946. 
<br>
[Here](https://github.com/Iron486/Amazon-Books-Web-Scraping/tree/main/spiders), you can find all the notebooks (in .ipynb) I used to scrape and clean the data.
