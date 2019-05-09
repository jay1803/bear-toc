# R 语言 数据帧
#code/language/r
---
数据帧是表或二维阵列状结构，其中每一列包含一个变量的值，并且每一行包含来自每一列的一组值。
以下是数据帧的特性。
* 列名称应为非空。
* 行名称应该是唯一的。
* 存储在数据帧中的数据可以是数字，因子或字符类型。
* 每个列应包含相同数量的数据项。

## 创建数据帧
```
# Create the data frame.
emp.data <- data.frame(
   emp_id = c (1:5), 
   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
   salary = c(623.3,515.2,611.0,729.0,843.25), 
   
   start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11",
      "2015-03-27")),
   stringsAsFactors = FALSE
)
# Print the data frame.			
print(emp.data)
```
当我们执行上面的代码，它产生以下结果 -
```
emp_id    emp_name     salary     start_date
1     1     Rick        623.30     2012-01-01
2     2     Dan         515.20     2013-09-23
3     3     Michelle    611.00     2014-11-15
4     4     Ryan        729.00     2014-05-11
5     5     Gary        843.25     2015-03-27
```

## 获取数据帧的结构
通过使用str()函数可以看到数据帧的结构。
```
# Create the data frame.
emp.data <- data.frame(
   emp_id = c (1:5), 
   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
   salary = c(623.3,515.2,611.0,729.0,843.25), 
   
   start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11",
      "2015-03-27")),
   stringsAsFactors = FALSE
)
# Get the structure of the data frame.
str(emp.data)
```
当我们执行上面的代码，它产生以下结果 -
```
'data.frame':   5 obs. of  4 variables:
 $ emp_id    : int  1 2 3 4 5
 $ emp_name  : chr  "Rick" "Dan" "Michelle" "Ryan" ...
 $ salary    : num  623 515 611 729 843
 $ start_date: Date, format: "2012-01-01" "2013-09-23" "2014-11-15" "2014-05-11" ...
```

## 数据框中的数据摘要
可以通过应用 *summary()* 函数获取数据的统计摘要和性质。 
```
# Create the data frame.
emp.data <- data.frame(
   emp_id = c (1:5), 
   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
   salary = c(623.3,515.2,611.0,729.0,843.25), 
   
   start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11",
      "2015-03-27")),
   stringsAsFactors = FALSE
)
# Print the summary.
print(summary(emp.data))
```
当我们执行上面的代码，它产生以下结果 -
```
emp_id    emp_name             salary        start_date        
 Min.   :1   Length:5           Min.   :515.2   Min.   :2012-01-01  
 1st Qu.:2   Class :character   1st Qu.:611.0   1st Qu.:2013-09-23  
 Median :3   Mode  :character   Median :623.3   Median :2014-05-11  
 Mean   :3                      Mean   :664.4   Mean   :2014-01-14  
 3rd Qu.:4                      3rd Qu.:729.0   3rd Qu.:2014-11-15  
 Max.   :5                      Max.   :843.2   Max.   :2015-03-27
```

## 从数据帧提取数据
使用列名称从数据框中提取特定列。
```
# Create the data frame.
emp.data <- data.frame(
   emp_id = c (1:5),
   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
   salary = c(623.3,515.2,611.0,729.0,843.25),
   
   start_date = as.Date(c("2012-01-01","2013-09-23","2014-11-15","2014-05-11",
      "2015-03-27")),
   stringsAsFactors = FALSE
)
# Extract Specific columns.
result <- data.frame(emp.data$emp_name,emp.data$salary)
print(result)
```
当我们执行上面的代码，它产生以下结果 -
```
emp.data.emp_name emp.data.salary
1              Rick          623.30
2               Dan          515.20
3          Michelle          611.00
4              Ryan          729.00
5              Gary          843.25
```
先提取前两行，然后提取所有列
```
# Create the data frame.
emp.data <- data.frame(
   emp_id = c (1:5),
   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
   salary = c(623.3,515.2,611.0,729.0,843.25),
   
   start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11",
      "2015-03-27")),
   stringsAsFactors = FALSE
)
# Extract first two rows.
result <- emp.data[1:2,]
print(result)
```
当我们执行上面的代码，它产生以下结果 -
```
emp_id    emp_name   salary    start_date
1      1     Rick      623.3     2012-01-01
2      2     Dan       515.2     2013-09-23
```
用第2和第4列提取第3和第5行
```
# Create the data frame.
emp.data <- data.frame(
   emp_id = c (1:5), 
   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
   salary = c(623.3,515.2,611.0,729.0,843.25), 
   
	start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11",
      "2015-03-27")),
   stringsAsFactors = FALSE
)

# Extract 3rd and 5th row with 2nd and 4th column.
result <- emp.data[c(3,5),c(2,4)]
print(result)
```
当我们执行上面的代码，它产生以下结果 -
```
emp_name start_date
3 Michelle 2014-11-15
5     Gary 2015-03-27
```

## 扩展数据帧
可以通过添加列和行来扩展数据帧。
### 添加列
只需使用新的列名称添加列向量。
```
# Create the data frame.
emp.data <- data.frame(
   emp_id = c (1:5), 
   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
   salary = c(623.3,515.2,611.0,729.0,843.25), 
   
   start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11",
      "2015-03-27")),
   stringsAsFactors = FALSE
)

# Add the "dept" coulmn.
emp.data$dept <- c("IT","Operations","IT","HR","Finance")
v <- emp.data
print(v)
```
当我们执行上面的代码，它产生以下结果 -
```
emp_id   emp_name    salary    start_date       dept
1     1    Rick        623.30    2012-01-01       IT
2     2    Dan         515.20    2013-09-23       Operations
3     3    Michelle    611.00    2014-11-15       IT
4     4    Ryan        729.00    2014-05-11       HR
5     5    Gary        843.25    2015-03-27       Finance
```
### 添加行
要将更多行永久添加到现有数据帧，我们需要引入与现有数据帧相同结构的新行，并使用 *rbind()* 函数。
在下面的示例中，我们创建一个包含新行的数据帧，并将其与现有数据帧合并以创建最终数据帧。
```
# Create the first data frame.
emp.data <- data.frame(
   emp_id = c (1:5), 
   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
   salary = c(623.3,515.2,611.0,729.0,843.25), 
   
   start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11",
      "2015-03-27")),
   dept = c("IT","Operations","IT","HR","Finance"),
   stringsAsFactors = FALSE
)

# Create the second data frame
emp.newdata <- 	data.frame(
   emp_id = c (6:8), 
   emp_name = c("Rasmi","Pranab","Tusar"),
   salary = c(578.0,722.5,632.8), 
   start_date = as.Date(c("2013-05-21","2013-07-30","2014-06-17")),
   dept = c("IT","Operations","Fianance"),
   stringsAsFactors = FALSE
)

# Bind the two data frames.
emp.finaldata <- rbind(emp.data,emp.newdata)
print(emp.finaldata)
```
当我们执行上面的代码，它产生以下结果 -
```
emp_id     emp_name    salary     start_date       dept
1      1     Rick        623.30     2012-01-01       IT
2      2     Dan         515.20     2013-09-23       Operations
3      3     Michelle    611.00     2014-11-15       IT
4      4     Ryan        729.00     2014-05-11       HR
5      5     Gary        843.25     2015-03-27       Finance
6      6     Rasmi       578.00     2013-05-21       IT
7      7     Pranab      722.50     2013-07-30       Operations
8      8     Tusar       632.80     2014-06-17       Fianance
```
---
## REFERENCE
[R语言 数据帧_w3cschool](https://www.w3cschool.cn/r/r_data_frames.html)
