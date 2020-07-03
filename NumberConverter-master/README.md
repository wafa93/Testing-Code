# NumberConverter
A Python library that aims to convert Arabic letters to number. Also, numbers to letters. 

## Prerequisites
- Python 3 and above.

## Installation

To install the library, simply run the following command:

``` pip install () ```

## File Descriptions
- NumberToWords:
  * NumberToWord.py: contain the code to convert number to letter
- tests:
  * testNumberToWord.py: contains test cases.

## Usage

Command line:
```
$ num2words 431
أربعمائة و واحد و ثلاثون
$ num2words -8324
سالب ثمانية آلاف  و ثلاثمائة و أربعة و عشرون
```

In code, there's only one function to use:

```
>>> from num2words import num2words
>>> num2words(42)
اثنان وراربعون
>>> num2words(1431, lang='ar')
واحد ألف  و أربعمائة و واحد و ثلاثون
```
