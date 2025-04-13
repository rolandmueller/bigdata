# Spark Exercise

Read the dataset 
```python
diamonds = spark.read.csv("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv", header="true", inferSchema="true")
```

### Dataset 

A dataset containing the prices and other attributes of almost 54,000 diamonds. The variables are as follows:

#### price
price in US dollars

#### carat
weight of the diamond. 1 carat is 0.2 gramm

#### cut
quality of the cut (Fair, Good, Very Good, Premium, Ideal)

#### color
diamond colour, from D (best) to J (worst)

#### clarity
a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))

#### x
length in mm (0--10.74)

#### y
width in mm (0--58.9)

#### z
depth in mm (0--31.8)

#### depth
total depth percentage = z / mean(x, y) = 2 * z / (x + y) (43--79)

#### table
width of top of diamond relative to widest point (43--95)


### How many diamonds do we have?
```python
diamonds.count()
```

### What is the schema of the DataFrame?

```python
diamonds.printSchema()
```

### Shows the first lines

```python
display(diamonds.show())
```


### Display the first lines as a table
```python
display(diamonds)
```

### Show basic statistics

```python
diamonds.describe("carat","price").show()
```

```python
display(diamonds.describe("carat","price"))
```

### Transformations 

We can use different data transformations like
- select
- where / filter (like where in SQL)
- grouBy
- agregations like avg, sum, max, min, mean, count
- limit 
- join
- drop (drops columns or rows)
- create new columns

### Select the column "cut" and show the distinct values

display(diamonds.select('cut').distinct())

### Filter only expensive diamonds

```python
expensive_diamonds = diamonds.where(diamonds["price"] > 15000)
```

### How many diamonds are expensive?
 
#### TODO: Try it by yourself


### Create a new dataframe df_cut that calculates the average price per cut

```python
dimonds_cut = diamonds.select("cut", "price").groupBy("cut").avg("price")
```

#### Display the result

```python
display(dimonds_cut)
```

Click on the '+' next to the table. Click on 'Visualization'. Visualization Type should be 'Bar'. Click on Save.

Why has the best cut ("ideal") not the best average price? 

### Create a new dataframe df_color that calculates the average price per color, sorted by color

#### TODO

### Create a Visualization: Create a Bar plot

#### TODO

### Create a new dataframe dimonds_prices that calculates the average price per all 4 Cs (color, carat, cut, clarity)

#### TODO

### Create a Visualization: Create a Scatterplot, with 'carat' on the x-column, avg(price) on the y-column, and cut on the group by

#### TODO

### 

# Use SQL in Spark Databricks

Save the Dataframe in the Delta Lake
```python
diamonds.write.format("delta").mode("overwrite").save("/delta/diamonds")
```

Now we create a SQL table
```python
%sql
DROP TABLE IF EXISTS diamonds;

CREATE TABLE diamonds USING DELTA LOCATION '/delta/diamonds/'
```

try it out:
```sql
%sql
SELECT * from diamonds
```

### Use SQL to select the color and price columns, averages the price, and groups and orders by color.

#### TODO

#### Create a bar chart

#### TODO

Create a screenshot of the notebook and upload it to Moodle

# Further Information
To find more tutorials, you can go for different topics:
- Getting started: https://docs.databricks.com/getting-started/index.html
- Data Engineering:  https://docs.databricks.com/workspace-index.html 
- Machine Learning: https://docs.databricks.com/machine-learning/index.html
- Data Warehousing and SQL: https://docs.databricks.com/sql/index.html
- Delta Lake: https://docs.databricks.com/delta/index.html



