# Spark Exercise

```python
diamonds = spark.read.csv("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv", header="true", inferSchema="true")
```

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

