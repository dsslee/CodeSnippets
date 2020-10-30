# Bash Scripting Tutorial

## Page Outline

* 1. [Basics](#1-Basic)
* 2. [Using Arrays](#2-Using-Arrays)
* 3. [If Statements](#3-If-statement)
* 4. [For Loops](#4-For-Loops)

## 1. Basics
|Command|Description|
|--|--|
|echo $1| echo the first ARGV arguments|
|echo $2| echo the second ARGV arguments|
|echo $@| echo out the entire ARGV arguments|
|echo $#| echo out the size of ARGV array|
|echo "The date is `date`."|shell within a shell|

### 1.1) Examples
```bash
$ # === numeric example ====
$ model1=87.65
$ model2=89.20
$ echo "The total score is $(echo "$model1 + $model2" | bc)"

#==== calculator =====
# Get first ARGV into variable
$ temp_f=$1

# Subtract 32
$ temp_f2=$(echo "scale=2; $temp_f - 32" | bc)

# Multiply by 5/9 and print
$ temp_c=$(echo "scale=2; $temp_f2 * 5 / 9" | bc)

# Print the temp
$ echo $temp_c

#===== Extracting data from a file =====
# Create three variables from the temp data files' contents
$ temp_a=$(cat temps/region_A)
$ temp_b=$(cat temps/region_B)
$ temp_c=$(cat temps/region_C)

# Print out the three variables
$ echo "The three temperatures were "$temp_a", "$temp_b", and "$temp_c""
```
## 2. Using Arrays
declare array by either:
- declare -a myarray
- myarray=()

### 2.1 Arrays in an Array
```bash
#===== METHOD 1 =====
my_arrays=(1 2 3 4 5 4 3 2)
echo "Return all items: "${my_arrays[@]}""
echo "Return last item: "${my_arrays[-1]}""
echo "Slicing array from index 1, return next 2 item: "${my_arrays[@]:1:2}""

# appending to array
my_arrays+=(1)
echo "Return all items: "${my_arrays[@]}""

#===== METHOD 2 =====
declare -a capital_cities
capital_cities+=("Seoul")
capital_cities+=("Toronto")
capital_cities+=("Washington")
echo "Return all items: "${capital_cities[@]}""

# Print out the entire array
echo ${capital_cities[@]}

# Print out the array length
echo ${#capital_cities[@]}

#===== Example =====
# Create variables from the temperature data files
temp_b="$(cat temps/region_B)"
temp_c="$(cat temps/region_C)"
echo "$temp_b"
echo "$temp_c"

# Create an array with these variables as elements
region_temps=("$temp_b" "$temp_c")
echo ${region_temps[@]}

# Call an external program to get average temperature
average_temp=$(echo "scale=2; (${region_temps[0]} + ${region_temps[1]}) / 2" | bc)
echo $average_temp

# Append average temp to the array
region_temps+=("$average_temp")

# Print out the whole array
echo ${region_temps[@]}


#===== Appending line from a file to an array =====
# declare an array
keywordlist=()

# read file
while IFS= read -r line || [[ "$line" ]]; do
    keywordlist+=("$line")
done < keyword.txt
echo "Keywords: "${keywordlist[@]}""

#print array element
for item in ${keywordlist[*]}; do
    echo $item
done
```

### 2.2 Associative Array(Dictionarys)
```bash
# declare first
declare -A model_metrics 

# add elements
model_metrics=([model_name]="knn" [model_accuracy]=98 [model_f1]=0.82)

# index using key to return a value
echo ${model_metrics[model_name]}

# return all keys
echo ${!model_metrics[@]}
```

## 3. If Statements
|Command|Description|
|--|--|
|> < = != | |
|&& \|\| |AND OR |
|-eq|for 'equal to'|
|-ne|for 'not equal to'|
|-lt|for 'less than'|
|-le|for 'less than or equal to'|
|-gt|for 'greater than' |
|-ge|for 'greater than or equal to'|
|-e|if the file exists|
|-s|if the file exists and has size greater than zero|
|-r|if the file exists and is readable|
|-w|if the file exists and is writable|
```bash
#===== String IF statements =====
x="Queen"
if [ $x == "King" ]; then
    echo "$x is a King!"
else
    echo "$x is not a King!"
fi

#===== Arithmetic IF statements =====
x=10
if (($x >5); then
    echo "$x is more tha 5!"
fi

if [ $x -gt 5 ]; then
    echo "$x is more tha 5!"
fi

#===== IF with Multiple conditions =====
x=10
if [ $x -gt 5] && [ $x -lt 11 ]; then
  echo "$x is more than 5 and less than 11!"
fi

if [[ $x -gt 5 && $x -lt 11 ]]; then
  echo "$x is more than 5 and less than 11!"
fi

#===== IF with command line programs =====
if grep -q 'Hello' words.txt; then
  echo "Hello is inside!"
fi

#===== IF with shell within a shell =====
if $(grep -q 'Hello' words.txt); then
  echo "Hello is inside!"
fi

#==== Sorting Models =====
# given: 
|model1.txt|model2.txt|
|--|--|
|Model Name: KNN Accuracy: 89 F1: 0.87 Date: 2019-12-01| Model Name: Random Forest Accuracy: 96 F1: 0.89 Date: 2019-12-01|

# Extract Accuracy from first ARGV element
accuracy=$(grep Accuracy $1 | sed 's/.* //')

# Conditionally move into good_models folder
if [ $accuracy -ge 90 ]; then
    mv $1 good_models/
fi

# Conditionally move into bad_models folder
if [ $accuracy -lt 90 ]; then
    mv $1 bad_models/
fi

#===== Moving Relevant Files =====
# Create variable from first ARGV element
sfile=$1

# Create an IF statement on first ARGV element's contents
if grep -q 'SRVM_' $sfile && grep -q 'vpt' $sfile ; then
	# Move file if matched
	mv $sfile good_logs/
fi
```

## 4 For Loops 
```bash
#===== For loop number ranges =====
for x in {1..5..2}
do
  echo $x
 done
 
#===== For loops with Glob expansions =====
for model in model_results/*
do
  echo $model
 done
 
 #===== For loops with shell within a shell =====
for model in $(ls model_results/ | grep -i '2009'
do
  echo $model
 done
```
