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

### Select  the column "cut" and show the distinct values

display(diamonds.select('cut').distinct())

### Filter only expensive diamonds

```python
expensive_diamonds = diamonds.where(diamonds["price"] > 15000)
```

### How many diamonds are expensive?
 
#### TODO: Try it by yourself

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

### Create a new dataframe df_cut that calculates the average price per cut

```python
dimonds_cut = diamonds.groupBy("cut").avg("price")
```

#### Display the result

```python
display(dimonds_cut)
```

Click on the '+' next to the table. Click on 'Visualization'. Visualization Type should be 'Bar'. Click on Save.

The result looks strange. Why is the price of a 'very good' cut, lower than of a 
### Create a new dataframe df_cut that calculates the average price per cut




