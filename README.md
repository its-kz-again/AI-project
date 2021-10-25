# AI-project
ids , A* and bidirectional bfs algorithm

<h3>Project definition</h3>
Ali is a disciplined representative of the school because he is a very tidy boy. Ali has a duty to arrange class lines every morning before the school principal arrives.<br/>
Their school is in the form of a rectangle with a length of m and a width of n meters. The school also has n × m students, including Ali (n-1 class with m student, one class with m-1 student and Ali) and since the health organization has recommended to maintain a physical distance between people, From the beginning of each morning, each student in the school is placed in one of the 1×1 squares that has been crossed out in the school yard.<br/>
Each of these students belongs to a class and is of a certain height. For example, the student in the middle house is a student from class (a) with a height of 150. Ali must arrange the rows so that the students in a class are all in the same row and in that row, in descending order of height (tallest in the leftmost house).To this work, according to the recommendations of the Ministry of Health and the school principal, to avoid crowds in the school yard, Ali can change his place with one of the students left, right, up or down each time and continue to do so until all the rows are in order.After arranging all the queues, Ali should be on the left side of one of the queues so that he can get out of the queue without breaking it and go to the moderator to report his performance to him.<br/>
Note: The order of the queues does not matter; That is, class (b) can be in the first row and class (a) in the second row.<br/>
You need to implement the algorithms mentioned above and formulate the problem. Then solve the problem with the help of each of the algorithms.


<h3>Input format</h3>
In the first line of the entrance, the numbers n and m are given, which indicate the width and length of the school yard.<br/>
In the next (n) line, there are (m) combinations of characters and numbers, each representing the height and class of the student that this student has standed up in this house.For example, 160a indicates that the student standing here is a student in class (a) with a height of 160. Ali is also identified by the # character.

<h3>Sample input</h3>
3 3<br/>
190a 170a 160b<br/> 
180b 160a 160b<br/>
180c 160c #

<h3>One of the goals of the input sample</h3>
190a 170a 160a<br/>
180b 160b 160b<br/>
# 180c 160c



<h3>problem.py</h3>
usage goal : for Problem formulation

<h3>solution.py</h3>
usage goal : for show results

<h3>main.py</h3>
usage goal : for get input & To convert inputs to states & create initial node

<h3>p1.py</h3>
implement the ids algorithm<br/>
To study this algorithm, refer to the <a href="https://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/">this link.</a>

<h3>p2.py</h3>
implement the A* algorithm<br/>
To study this algorithm, refer to the <a href="https://www.geeksforgeeks.org/a-search-algorithm/">this link.</a>

<h3>p3.py</h3>
implement the bidirectional bfs algorithm<br/>
To study this algorithm, refer to the <a href="https://www.geeksforgeeks.org/bidirectional-search/">this link.</a>

