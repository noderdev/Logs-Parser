# Logs-Parser
Log Parser for flow log data.

# Assumptions
1. The mapping of protocol number to keyword is done through a file called mapping.txt which is added in the current directory itself.
2. When you the program, you are expected to give the name/path of the file of log file data and tags mapping file.
3. The name of the output files are hard coded for this assessment.

# Requirements
1. The following assessment is done in python so any version of python will work. 
2. I've added a test file as well with few sample test cases. In order to run them, install pytest by running
```
pip install pytest   
```
And then run 
```
pytest
```

Step 2 is completely optional.

# How to run ?
1. Download the zip or git clone the folder on your system.
2. Open the folder in a code editor like visual studio and open the terminal. Alternately you can open terminal and cd into the folder.
3. Run python logs_parser.py.
4. You will be prompted to enter the name/path of the log file and tags mapping file.
5. Enter them and the output files tag_count.txt and combination_count.txt will be generated.

# Runtime Analysis

The time complexity of our algorithm is O(n) where n is the number of rows in the log files.
To calculate n, we have fo the following :-

Step 1: Calculate the size of a single row.
The length of the provided row is 108 bytes (avg).

Step 2: Convert 10MB (log file size) to bytes.

1 MB = 1,048,576 bytes, so 10MB = 10 * 1,048,576 = 10,485,760 bytes.
Step 3: Divide the total file size by the size of one row.

Number of rows = Total size of the file (in bytes) ÷ Size of one row (in bytes).
Number of rows = 10,485,760 bytes ÷ 108 bytes/row ≈ 97,090 rows.
Therefore, a 10MB file containing rows of 108 bytes each would contain approximately 97,090 rows

The space complexity is also O(n).

# Test
I've added few pytest unit test in the test_logs_parser.py .
It is testing for some runtime error test cases, but it not the complete set of tests.
