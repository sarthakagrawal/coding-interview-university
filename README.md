# Coding Interview University

<b> This is a fork of the excellent repo by John Washam on preparing for software engineering interviers. This is heavily modified, with timelines that are appropriate for me and with reduced material. </b>

## Table of Contents

- [How to use it](#how-to-use-it)
- [Don't feel you aren't smart enough](#dont-feel-you-arent-smart-enough)
- [About Video Resources](#about-video-resources)
- [Interview Process & General Interview Prep](#interview-process--general-interview-prep)
- [Book List](#book-list)
- [Before you Get Started](#before-you-get-started)
- [Prerequisite Knowledge -- 5/19/20](#prerequisite-knowledge)
- [The Daily Plan](#the-daily-plan)
- [Algorithmic complexity / Big-O / Asymptotic analysis -- 5/19/20](#algorithmic-complexity--big-o--asymptotic-analysis)
- [Data Structures](#data-structures)
  - [Arrays -- 5/21/20](#arrays)
  - [Linked Lists -- 5/22/20](#linked-lists)
  - [Stack -- 5/26/20](#stack)
  - [Queue -- 5/27/20](#queue)
  - [Hash table -- 5/28/20](#hash-table)
- [More Knowledge](#more-knowledge)
  - [Binary search -- 5/29/20](#binary-search)
  - [Bitwise operations -- 5/29/20](#bitwise-operations)
- [Trees](#trees)
  - [Trees - Notes & Background -- 6/1/20](#trees---notes--background)
  - [Binary search trees: BSTs -- 6/3/20](#binary-search-trees-bsts)
  - [Heap / Priority Queue / Binary Heap -- 6/5/20](#heap--priority-queue--binary-heap)
  - balanced search trees (general concept, not details)
  - traversals: preorder, inorder, postorder, BFS, DFS
- [Sorting](#sorting)
  - selection -- 6/8/20
  - insertion -- 6/9/20
  - heapsort -- 6/10/20
  - quicksort -- 6/11/20
  - merge sort -- 6/12/20
- [Graphs](#graphs)
  - directed -- 6/15/20
  - undirected -- 6/16/20
  - adjacency matrix -- 6/17/20
  - adjacency list -- 6/18/20
  - traversals: BFS, DFS -- 6/19/20
- [Even More Knowledge](#even-more-knowledge)
  - [Recursion -- 6/24/20](#recursion)
  - [Dynamic Programming -- 6/26/20](#dynamic-programming)
  - [Object-Oriented Programming -- 7/1/20](#object-oriented-programming)
  - [Design Patterns -- 7/2/20](#design-patterns)
  - [Combinatorics (n choose k) & Probability -- 7/3/20](#combinatorics-n-choose-k--probability)
  - [NP, NP-Complete and Approximation Algorithms -- 7/4/20](#np-np-complete-and-approximation-algorithms)
  - [Caches -- 7/5/20](#caches)
  - [Processes and Threads -- 7/5/20](#processes-and-threads)
  - [Testing -- 7/5/20](#testing)
  - [Scheduling -- 7/6/20](#scheduling)
  - [String searching & manipulations -- 7/6/20](#string-searching--manipulations)
  - [Tries -- 7/8/20](#tries)
  - [Floating Point Numbers -- 7/9/20](#floating-point-numbers)
- [Final Review](#final-review)
- [Coding Question Practice](#coding-question-practice)
- [Coding exercises/challenges](#coding-exerciseschallenges)
- [Once you're closer to the interview](#once-youre-closer-to-the-interview)

---

## How to use it

Everything below is an outline, and you should tackle the items in order from top to bottom.

I'm using Github's special markdown flavor, including tasks lists to check progress.

**Create a new branch so you can check items like this, just put an x in the brackets: [x]**

    Fork a branch and follow the commands below

`git checkout -b progress`

`git remote add jwasham https://github.com/jwasham/coding-interview-university`

`git fetch --all`

    Mark all boxes with X after you completed your changes

`git add .`

`git commit -m "Marked x"`

`git rebase jwasham/master`

`git push --force`

[More about Github-flavored markdown](https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown)

## Don't feel you aren't smart enough

- Successful software engineers are smart, but many have an insecurity that they aren't smart enough.
- [The myth of the Genius Programmer](https://www.youtube.com/watch?v=0SARbwvhupQ)
- [It's Dangerous to Go Alone: Battling the Invisible Monsters in Tech](https://www.youtube.com/watch?v=1i8ylq4j_EY)

## About Video Resources

Some videos are available only by enrolling in a Coursera or EdX class. These are called MOOCs.
Sometimes the classes are not in session so you have to wait a couple of months, so you have no access.

    I'd appreciate your help to add free and always-available public sources, such as YouTube videos to accompany the online course videos.
    I like using university lectures.

## Interview Process & General Interview Prep

- [ ] [ABC: Always Be Coding](https://medium.com/always-be-coding/abc-always-be-coding-d5f8051afce2#.4heg8zvm4)
- [ ] [Whiteboarding](https://medium.com/@dpup/whiteboarding-4df873dbba2e#.hf6jn45g1)
- [ ] [Effective Whiteboarding during Programming Interviews](http://www.coderust.com/blog/2014/04/10/effective-whiteboarding-during-programming-interviews/)
- [ ] [Demystifying Tech Recruiting](https://www.youtube.com/watch?v=N233T0epWTs)
- [ ] How to Get a Job at the Big 4:
  - [ ] [How to Get a Job at the Big 4 - Amazon, Facebook, Google & Microsoft (video)](https://www.youtube.com/watch?v=YJZCUhxNCv8)
- [ ] Cracking The Coding Interview Set 1:
  - [ ] [Gayle L McDowell - Cracking The Coding Interview (video)](https://www.youtube.com/watch?v=rEJzOhC5ZtQ)
  - [ ] [Cracking the Coding Interview with Author Gayle Laakmann McDowell (video)](https://www.youtube.com/watch?v=aClxtDcdpsQ)
- [ ] Cracking the Facebook Coding Interview
  - [ ] [The Approach](https://www.youtube.com/watch?v=wCl9kvQGHPI)
  - [ ] [Problem Walkthrough](https://www.youtube.com/watch?v=4UWDyJq8jZg)
- [ ] Prep Course:
  - [ ] [Software Engineer Interview Unleashed (paid course)](https://www.udemy.com/software-engineer-interview-unleashed):
    - Learn how to make yourself ready for software engineer interviews from a former Google interviewer.
  - [ ] [Python for Data Structures, Algorithms, and Interviews (paid course)](https://www.udemy.com/python-for-data-structures-algorithms-and-interviews/):
    - A Python centric interview prep course which covers data structures, algorithms, mock interviews and much more.
  - [ ] [Intro to Data Structures and Algorithms using Python (Udacity free course)](https://www.udacity.com/course/data-structures-and-algorithms-in-python--ud513):
    - A free Python centric data structures and algorithms course.
  - [ ] [Data Structures and Algorithms Nanodegree! (Udacity paid Nanodegree)](https://www.udacity.com/course/data-structures-and-algorithms-nanodegree--nd256):
    - Get hands-on practice with over 100 data structures and algorithm exercises and guidance from a dedicated mentor to help prepare you for interviews and on-the-job scenarios.

## Book List

This is a shorter list than what I used. This is abbreviated to save you time.

### Interview Prep

- [ ] [Programming Interviews Exposed: Coding Your Way Through the Interview, 4th Edition](https://www.amazon.com/Programming-Interviews-Exposed-Through-Interview/dp/111941847X/)
  - answers in C++ and Java
  - this is a good warm-up for Cracking the Coding Interview
  - not too difficult, most problems may be easier than what you'll see in an interview (from what I've read)
- [ ] [Cracking the Coding Interview, 6th Edition](http://www.amazon.com/Cracking-Coding-Interview-6th-Programming/dp/0984782850/)
  - answers in Java

### Language Specific

### C++

I haven't read these two, but they are highly rated and written by Sedgewick. He's awesome.

- [ ] [Algorithms in C++, Parts 1-4: Fundamentals, Data Structure, Sorting, Searching](https://www.amazon.com/Algorithms-Parts-1-4-Fundamentals-Structure/dp/0201350882/)
- [ ] [Algorithms in C++ Part 5: Graph Algorithms](https://www.amazon.com/Algorithms-Part-Graph-3rd-Pt-5/dp/0201361183/)

If you have a better recommendation for C++, please let me know. Looking for a comprehensive resource.

### Python

- [ ] [Data Structures and Algorithms in Python](https://www.amazon.com/Structures-Algorithms-Python-Michael-Goodrich/dp/1118290275/)
  - by Goodrich, Tamassia, Goldwasser
  - I loved this book. It covered everything and more.
  - Pythonic code
  - my glowing book report: https://startupnextdoor.com/book-report-data-structures-and-algorithms-in-python/

## Before you Get Started

This list grew over many months, and yes, it kind of got out of hand.

Here are some mistakes I made so you'll have a better experience.

### 1. You Won't Remember it All

I watched hours of videos and took copious notes, and months later there was much I didn't remember. I spent 3 days going
through my notes and making flashcards so I could review.

Read please so you won't make my mistakes:

[Retaining Computer Science Knowledge](https://startupnextdoor.com/retaining-computer-science-knowledge/).

A course recommended to me (haven't taken it): [Learning how to Learn](https://www.coursera.org/learn/learning-how-to-learn)

### 2. Use Flashcards

To solve the problem, I made a little flashcards site where I could add flashcards of 2 types: general and code.
Each card has different formatting.

I made a mobile-first website so I could review on my phone and tablet, wherever I am.

Make your own for free:

- [Flashcards site repo](https://github.com/jwasham/computer-science-flash-cards)
- [My flash cards database (old - 1200 cards)](https://github.com/jwasham/computer-science-flash-cards/blob/master/cards-jwasham.db):
- [My flash cards database (new - 1800 cards)](https://github.com/jwasham/computer-science-flash-cards/blob/master/cards-jwasham-extreme.db):

Keep in mind I went overboard and have cards covering everything from assembly language and Python trivia to machine learning and statistics. It's way too much for what's required.

**Note on flashcards:** The first time you recognize you know the answer, don't mark it as known. You have to see the
same card and answer it several times correctly before you really know it. Repetition will put that knowledge deeper in
your brain.

An alternative to using my flashcard site is [Anki](http://ankisrs.net/), which has been recommended to me numerous times. It uses a repetition system to help you remember.
It's user-friendly, available on all platforms and has a cloud sync system. It costs \$25 on iOS but is free on other platforms.

My flashcard database in Anki format: https://ankiweb.net/shared/info/25173560 (thanks [@xiewenya](https://github.com/xiewenya))

### 3. Start doing coding interview questions while you're learning data structures and algorithms,

You need to apply what you're learning to solving problems, or you'll forget. I made this mistake. Once you've learned a topic,
and feel comfortable with it, like linked lists, open one of the coding interview books and do a couple of questions regarding
linked lists. Then move on to the next learning topic. Then later, go back and do another linked list problem,
or recursion problem, or whatever. But keep doing problems while you're learning. You're not being hired for knowledge,
but how you apply the knowledge. There are several books and sites I recommend.
See here for more: [Coding Question Practice](#coding-question-practice)

### 4. Review, review, review

I keep a set of cheat sheets on ASCII, OSI stack, Big-O notations, and more. I study them when I have some spare time.

Take a break from programming problems for a half hour and go through your flashcards.

### 5. Focus

There are a lot of distractions that can take up valuable time. Focus and concentration are hard. Turn on some music
without lyrics and you'll be able to focus pretty well.

## The Daily Plan

Some subjects take one day, and some will take multiple days. Some are just learning with nothing to implement. I plan to take 1-2 passes through the material. The first pass should take 8 weeks and will be done with Python. The plan is to spend 1-2 days on a subtopic, watch videos/read about the topic, and then complete relevant exercises on Leetcode.

- Python - using built-in types (to keep practicing Python)
- and write tests to ensure I'm doing it right, sometimes just using simple assert() statements

<i> Optional second pass:

- C++ - without using built-in types
- C++ - using built-in types, like STL's std::list for a linked list </i>

Once I've learned the basics of the relevant data structures/algorithms in this syllabus, the plan is to devote my remaining time to Leetcode practice. In any case, I'll reevaluate in two months, in mid-July.

## Prerequisite Knowledge -- 5/19/20

- [x] **How computers process a program:**
  - [x] [How CPU executes a program (video)](https://www.youtube.com/watch?v=XM4lGflQFvA)
  - [x] [How computers calculate - ALU (video)](https://youtu.be/1I5ZMmrOfnA)
  - [x] [Registers and RAM (video)](https://youtu.be/fpnE6UAfbtU)
  - [x] [The Central Processing Unit (CPU) (video)](https://youtu.be/FZGugFqdr60)
  - [x] [Instructions and Programs (video)](https://youtu.be/zltgXvg6r3k)

## Algorithmic complexity / Big-O / Asymptotic analysis -- 5/19/20

- Nothing to implement
- There are a lot of videos here. Just watch enough until you understand it. You can always come back and review.
- If some of the lectures are too mathy, you can jump down to the bottom and watch the discrete mathematics videos to get the background knowledge.
- [x] [Harvard CS50 - Asymptotic Notation (video)](https://www.youtube.com/watch?v=iOq5kSKqeR4)
- [ ] [Big O Notations (general quick tutorial) (video)](https://www.youtube.com/watch?v=V6mKVRU1evU)
- [ ] [Big O Notation (and Omega and Theta) - best mathematical explanation (video)](https://www.youtube.com/watch?v=ei-A_wy5Yxw&index=2&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- [ ] Skiena:
  - [video](https://www.youtube.com/watch?v=gSyDMtdPNpU&index=2&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)
  - [slides](http://www3.cs.stonybrook.edu/~algorith/video-lectures/2007/lecture2.pdf)
- [ ] [A Gentle Introduction to Algorithm Complexity Analysis](http://discrete.gr/complexity/)
- [ ] [Orders of Growth (video)](https://www.coursera.org/lecture/algorithmic-thinking-1/orders-of-growth-6PKkX)
- [ ] [Asymptotics (video)](https://www.coursera.org/lecture/algorithmic-thinking-1/asymptotics-bXAtM)
- [ ] [UC Berkeley Big O (video)](https://archive.org/details/ucberkeley_webcast_VIS4YDpuP98)
- [ ] [UC Berkeley Big Omega (video)](https://archive.org/details/ucberkeley_webcast_ca3e7UVmeUc)
- [ ] [Amortized Analysis (video)](https://www.youtube.com/watch?v=B3SpQZaAZP4&index=10&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- [ ] [Illustrating "Big O" (video)](https://www.coursera.org/lecture/algorithmic-thinking-1/illustrating-big-o-YVqzv)
- [ ] TopCoder (includes recurrence relations and master theorem):
  - [Computational Complexity: Section 1](https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-1/)
  - [Computational Complexity: Section 2](https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-2/)
- [ ] [Cheat sheet](http://bigocheatsheet.com/)

## Data Structures

- ### Arrays -- 5/21/20

  - Implement an automatically resizing vector.
    \_ Sarthak's note -- I glazed by the implementation since in Python you can't use pointers/the only possible implementation of an array in Python seems to involve the use of List, which makes it pretty simple.
  - [x] Description:
    - [Arrays (video)](https://www.coursera.org/learn/data-structures/lecture/OsBSF/arrays)
    - [UC Berkeley CS61B - Linear and Multi-Dim Arrays (video)](https://archive.org/details/ucberkeley_webcast_Wp8oiO_CZZE) (Start watching from 15m 32s)
    - [Basic Arrays (video)](https://archive.org/details/0102WhatYouShouldKnow/02_04-basicArrays.mp4)
    - [Multi-dim (video)](https://archive.org/details/0102WhatYouShouldKnow/02_05-multidimensionalArrays.mp4)
    - [Dynamic Arrays (video)](https://www.coursera.org/learn/data-structures/lecture/EwbnV/dynamic-arrays)
    - [Jagged Arrays (video)](https://www.youtube.com/watch?v=1jtrQqYpt7g)
    - [Jagged Arrays (video)](https://archive.org/details/0102WhatYouShouldKnow/02_06-jaggedArrays.mp4)
    - [Resizing arrays (video)](https://archive.org/details/0102WhatYouShouldKnow/03_01-resizableArrays.mp4)
  - [ ] Implement a vector (mutable array with automatic resizing):
    - [ ] Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.
    - [ ] new raw data array with allocated memory
      - can allocate int array under the hood, just not use its features
      - start with 16, or if starting number is greater, use power of 2 - 16, 32, 64, 128
    - [ ] size() - number of items
    - [ ] capacity() - number of items it can hold
    - [ ] is_empty()
    - [ ] at(index) - returns item at given index, blows up if index out of bounds
    - [ ] push(item)
    - [ ] insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
    - [ ] prepend(item) - can use insert above at index 0
    - [ ] pop() - remove from end, return value
    - [ ] delete(index) - delete item at index, shifting all trailing elements left
    - [ ] remove(item) - looks for value and removes index holding it (even if in multiple places)
    - [ ] find(item) - looks for value and returns first index with that value, -1 if not found
    - [ ] resize(new_capacity) // private function
      - when you reach capacity, resize to double the size
      - when popping an item, if size is 1/4 of capacity, resize to half
  - [ ] Time
    - O(1) to add/remove at end (amortized for allocations for more space), index, or update
    - O(n) to insert/remove elsewhere
  - [ ] Space
    - contiguous in memory, so proximity helps performance
    - space needed = (array capacity, which is >= n) \* size of item, but even if 2n, still O(n)

- ### Linked Lists -- 5/22/20

  - [x] Description:
    - [x] [singly linked lists (video)](https://www.coursera.org/learn/data-structures/lecture/kHhgK/singly-linked-lists)
    - [x] [CS 61B - Linked Lists 1 (video)](https://archive.org/details/ucberkeley_webcast_htzJdKoEmO0)
    - [x] [CS 61B - Linked Lists 2 (video)](https://archive.org/details/ucberkeley_webcast_-c4I3gFYe3w)
  - [ ] [C Code (video)](https://www.youtube.com/watch?v=QN6FPiD0Gzo) - not the whole video, just portions about Node struct and memory allocation.
  - [ ] Linked List vs Arrays:
    - [Core Linked Lists Vs Arrays (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/rjBs9/core-linked-lists-vs-arrays)
    - [In The Real World Linked Lists Vs Arrays (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/QUaUd/in-the-real-world-lists-vs-arrays)
  - [ ] [why you should avoid linked lists (video)](https://www.youtube.com/watch?v=YQs6IC-vgmo)
  - [ ] Gotcha: you need pointer to pointer knowledge:
        (for when you pass a pointer to a function that may change the address where that pointer points)
        This page is just to get a grasp on ptr to ptr. I don't recommend this list traversal style. Readability and maintainability suffer due to cleverness.
    - [Pointers to Pointers](https://www.eskimo.com/~scs/cclass/int/sx8.html)
  - [ ] implement (I did with tail pointer & without):
    - [ ] size() - returns number of data elements in list
    - [ ] empty() - bool returns true if empty
    - [ ] value_at(index) - returns the value of the nth item (starting at 0 for first)
    - [ ] push_front(value) - adds an item to the front of the list
    - [ ] pop_front() - remove front item and return its value
    - [ ] push_back(value) - adds an item at the end
    - [ ] pop_back() - removes end item and returns its value
    - [ ] front() - get value of front item
    - [ ] back() - get value of end item
    - [ ] insert(index, value) - insert value at index, so current item at that index is pointed to by new item at index
    - [ ] erase(index) - removes node at given index
    - [ ] value_n_from_end(n) - returns the value of the node at nth position from the end of the list
    - [ ] reverse() - reverses the list
    - [ ] remove_value(value) - removes the first item in the list with this value
  - [x] Doubly-linked List
    - [Description (video)](https://www.youtube.com/watch?v=JdQeNxWCguQ) (originial recc was behind paywall, so I substituted this youtube video)
    - No need to implement

- ### Stack

  - [x] [Stacks (video)](https://www.coursera.org/learn/data-structures/lecture/UdKzQ/stacks)
  - [x] [Using Stacks Last-In First-Out (video)](https://archive.org/details/0102WhatYouShouldKnow/05_01-usingStacksForLast-inFirst-out.mp4)
  - [x] Will not implement. Implementing with array is trivial.

- ### Queue

  - [x] [Using Queues First-In First-Out(video)](https://archive.org/details/0102WhatYouShouldKnow/05_03-usingQueuesForFirst-inFirst-out.mp4)
  - [x] [Queue (video)](https://www.coursera.org/lecture/data-structures/queues-EShpq)
  - [x] [Circular buffer/FIFO](https://en.wikipedia.org/wiki/Circular_buffer)
  - [x] [Priority Queues (video)](https://archive.org/details/0102WhatYouShouldKnow/05_04-priorityQueuesAndDeques.mp4)
  - [ ] Implement using linked-list, with tail pointer:
    - enqueue(value) - adds value at position at tail
    - dequeue() - returns value and removes least recently added element (front)
    - empty()
  - [ ] Implement using fixed-sized array:
    - enqueue(value) - adds item at end of available storage
    - dequeue() - returns value and removes least recently added element
    - empty()
    - full()
  - [ ] Cost:
    - a bad implementation using linked list where you enqueue at head and dequeue at tail would be O(n)
      because you'd need the next to last element, causing a full traversal each dequeue
    - enqueue: O(1) (amortized, linked list and array [probing])
    - dequeue: O(1) (linked list and array)
    - empty: O(1) (linked list and array)

- ### Hash table

  - [ ] Videos:

    - [x] [Hashing with Chaining (video)](https://www.youtube.com/watch?v=0M_kIqhwbFo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8)
    - [x] [Table Doubling, Karp-Rabin (video)](https://www.youtube.com/watch?v=BRO7mVIFt08&index=9&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [ ] [Open Addressing, Cryptographic Hashing (video)](https://www.youtube.com/watch?v=rvdJDijO2Ro&index=10&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [x][pycon 2010: the mighty dictionary (video)](https://www.youtube.com/watch?v=C4Kc8xzcA68)
    - [ ] [(Advanced) Randomization: Universal & Perfect Hashing (video)](https://www.youtube.com/watch?v=z0lJ2k0sl1g&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=11)
    - [ ] [(Advanced) Perfect hashing (video)](https://www.youtube.com/watch?v=N0COwN14gt0&list=PL2B4EEwhKD-NbwZ4ezj7gyc_3yNrojKM9&index=4)

  - [ ] Online Courses:

    - [ ] [Understanding Hash Functions (video)](https://archive.org/details/0102WhatYouShouldKnow/06_02-understandingHashFunctions.mp4)
    - [ ] [Using Hash Tables (video)](https://archive.org/details/0102WhatYouShouldKnow/06_03-usingHashTables.mp4)
    - [ ] [Supporting Hashing (video)](https://archive.org/details/0102WhatYouShouldKnow/06_04-supportingHashing.mp4)
    - [ ] [Language Support Hash Tables (video)](https://archive.org/details/0102WhatYouShouldKnow/06_05-languageSupportForHashTables.mp4)
    - [ ] [Core Hash Tables (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/m7UuP/core-hash-tables)
    - [ ] [Data Structures (video)](https://www.coursera.org/learn/data-structures/home/week/4)
    - [ ] [Phone Book Problem (video)](https://www.coursera.org/learn/data-structures/lecture/NYZZP/phone-book-problem)
    - [ ] distributed hash tables:
      - [Instant Uploads And Storage Optimization In Dropbox (video)](https://www.coursera.org/learn/data-structures/lecture/DvaIb/instant-uploads-and-storage-optimization-in-dropbox)
      - [Distributed Hash Tables (video)](https://www.coursera.org/learn/data-structures/lecture/tvH8H/distributed-hash-tables)

  - [ ] implement with array using linear probing
    - hash(k, m) - m is size of hash table
    - add(key, value) - if key already exists, update value
    - exists(key)
    - get(key)
    - remove(key)

## More Knowledge

- ### Binary search

  - [x] [Binary Search (video)](https://www.youtube.com/watch?v=D5SrAga1pno)
  - [ ] [Binary Search (video)](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)
  - [x] [detail](https://www.topcoder.com/community/competitive-programming/tutorials/binary-search/)
  - [ ] Implement:
    - binary search (on sorted array of integers)
    - binary search using recursion

- ### Bitwise operations
  - [ ] [Bits cheat sheet](https://github.com/jwasham/coding-interview-university/blob/master/extras/cheat%20sheets/bits-cheat-sheet.pdf) - you should know many of the powers of 2 from (2^1 to 2^16 and 2^32)
  - [ ] Get a really good understanding of manipulating bits with: &, |, ^, ~, >>, <<
    - [x] [words](<https://en.wikipedia.org/wiki/Word_(computer_architecture)>)
    - [ ] Good intro:
          **Sarthak note**: I started working on the below video, but I don't see the relevance to entry level coding interviews. May come back later.
          [Bit Manipulation (video)](https://www.youtube.com/watch?v=7jkIUgLC29I)
    - [ ] [C Programming Tutorial 2-10: Bitwise Operators (video)](https://www.youtube.com/watch?v=d0AwjSpNXR0)
    - [ ] [Bit Manipulation](https://en.wikipedia.org/wiki/Bit_manipulation)
    - [ ] [Bitwise Operation](https://en.wikipedia.org/wiki/Bitwise_operation)
    - [ ] [Bithacks](https://graphics.stanford.edu/~seander/bithacks.html)
    - [ ] [The Bit Twiddler](https://bits.stephan-brumme.com/)
    - [ ] [The Bit Twiddler Interactive](https://bits.stephan-brumme.com/interactive.html)
    - [ ] [Bit Hacks (video)](https://www.youtube.com/watch?v=ZusiKXcz_ac)
  - [ ] 2s and 1s complement
    - [Binary: Plusses & Minuses (Why We Use Two's Complement) (video)](https://www.youtube.com/watch?v=lKTsv6iVxV4)
    - [1s Complement](https://en.wikipedia.org/wiki/Ones%27_complement)
    - [2s Complement](https://en.wikipedia.org/wiki/Two%27s_complement)
  - [ ] count set bits
    - [4 ways to count bits in a byte (video)](https://youtu.be/Hzuzo9NJrlc)
    - [Count Bits](https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan)
    - [How To Count The Number Of Set Bits In a 32 Bit Integer](http://stackoverflow.com/questions/109023/how-to-count-the-number-of-set-bits-in-a-32-bit-integer)
  - [ ] swap values:
    - [Swap](https://bits.stephan-brumme.com/swap.html)
  - [ ] absolute value:
    - [Absolute Integer](https://bits.stephan-brumme.com/absInteger.html)

## Trees

- ### Trees - Notes & Background

  - [x][series: core trees (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/ovovP/core-trees)
  - [ ] [Series: Trees (video)](https://www.coursera.org/learn/data-structures/lecture/95qda/trees)
  - basic tree construction
  - traversal
  - manipulation algorithms
  - [x] [BFS(breadth-first search) and DFS(depth-first search) (video)](https://www.youtube.com/watch?v=uWL6FJhq5fM)
    - BFS notes:
      - level order (BFS, using queue)
      - time complexity: O(n)
      - space complexity: best: O(1), worst: O(n/2)=O(n)
    - DFS notes:
      - time complexity: O(n)
      - space complexity:
        best: O(log n) - avg. height of tree
        worst: O(n)
      - inorder (DFS: left, self, right)
      - postorder (DFS: left, right, self)
      - preorder (DFS: self, left, right)

- ### Binary search trees: BSTs

  - [x] [Binary Search Tree Review (video)](https://www.youtube.com/watch?v=x6At0nzX92o&index=1&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
  - [ ] [Series (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/p82sw/core-introduction-to-binary-search-trees)
    - starts with symbol table and goes through BST applications
  - [ ] [Introduction (video)](https://www.coursera.org/learn/data-structures/lecture/E7cXP/introduction)
  - [ ] [MIT (video)](https://www.youtube.com/watch?v=9Jry5-82I68)
  - C/C++:
    - [ ] [Binary search tree - Implementation in C/C++ (video)](https://www.youtube.com/watch?v=COZK7NATh4k&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=28)
    - [ ] [BST implementation - memory allocation in stack and heap (video)](https://www.youtube.com/watch?v=hWokyBoo0aI&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=29)
    - [ ] [Find min and max element in a binary search tree (video)](https://www.youtube.com/watch?v=Ut90klNN264&index=30&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
    - [ ] [Find height of a binary tree (video)](https://www.youtube.com/watch?v=_pnqMz5nrRs&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=31)
    - [ ] [Binary tree traversal - breadth-first and depth-first strategies (video)](https://www.youtube.com/watch?v=9RHO6jU--GU&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=32)
    - [ ] [Binary tree: Level Order Traversal (video)](https://www.youtube.com/watch?v=86g8jAQug04&index=33&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
    - [ ] [Binary tree traversal: Preorder, Inorder, Postorder (video)](https://www.youtube.com/watch?v=gm8DUJJhmY4&index=34&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
    - [ ] [Check if a binary tree is binary search tree or not (video)](https://www.youtube.com/watch?v=yEwSGhSsT0U&index=35&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
    - [ ] [Delete a node from Binary Search Tree (video)](https://www.youtube.com/watch?v=gcULXE7ViZw&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=36)
    - [ ] [Inorder Successor in a binary search tree (video)](https://www.youtube.com/watch?v=5cPbNCrdotA&index=37&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
  - [ ] Implement:
    - [ ] insert // insert value into tree
    - [ ] get_node_count // get count of values stored
    - [ ] print_values // prints the values in the tree, from min to max
    - [ ] delete_tree
    - [ ] is_in_tree // returns true if given value exists in the tree
    - [ ] get_height // returns the height in nodes (single node's height is 1)
    - [ ] get_min // returns the minimum value stored in the tree
    - [ ] get_max // returns the maximum value stored in the tree
    - [ ] is_binary_search_tree
    - [ ] delete_value
    - [ ] get_successor // returns next-highest value in tree after given value, -1 if none

- ### Heap / Priority Queue / Binary Heap
  - visualized as a tree, but is usually linear in storage (array, linked list)
  - [ ] [Heap](<https://en.wikipedia.org/wiki/Heap_(data_structure)>)
  - [ ] [Introduction (video)](https://www.coursera.org/learn/data-structures/lecture/2OpTs/introduction)
  - [ ] [Naive Implementations (video)](https://www.coursera.org/learn/data-structures/lecture/z3l9N/naive-implementations)
  - [ ] [Binary Trees (video)](https://www.coursera.org/learn/data-structures/lecture/GRV2q/binary-trees)
  - [ ] [Tree Height Remark (video)](https://www.coursera.org/learn/data-structures/supplement/S5xxz/tree-height-remark)
  - [ ] [Basic Operations (video)](https://www.coursera.org/learn/data-structures/lecture/0g1dl/basic-operations)
  - [ ] [Complete Binary Trees (video)](https://www.coursera.org/learn/data-structures/lecture/gl5Ni/complete-binary-trees)
  - [ ] [Pseudocode (video)](https://www.coursera.org/learn/data-structures/lecture/HxQo9/pseudocode)
  - [ ] [Heap Sort - jumps to start (video)](https://youtu.be/odNJmw5TOEE?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3291)
  - [ ] [Heap Sort (video)](https://www.coursera.org/learn/data-structures/lecture/hSzMO/heap-sort)
  - [ ] [Building a heap (video)](https://www.coursera.org/learn/data-structures/lecture/dwrOS/building-a-heap)
  - [ ] [MIT: Heaps and Heap Sort (video)](https://www.youtube.com/watch?v=B7hVxCmfPtM&index=4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
  - [ ] [CS 61B Lecture 24: Priority Queues (video)](https://archive.org/details/ucberkeley_webcast_yIUFT6AKBGE)
  - [ ] [Linear Time BuildHeap (max-heap)](https://www.youtube.com/watch?v=MiyLo8adrWw)
  - [ ] Implement a max-heap:
    - [ ] insert
    - [ ] sift_up - needed for insert
    - [ ] get_max - returns the max item, without removing it
    - [ ] get_size() - return number of elements stored
    - [ ] is_empty() - returns true if heap contains no elements
    - [ ] extract_max - returns the max item, removing it
    - [ ] sift_down - needed for extract_max
    - [ ] remove(i) - removes item at index x
    - [ ] heapify - create a heap from an array of elements, needed for heap_sort
    - [ ] heap_sort() - take an unsorted array and turn it into a sorted array in-place using a max heap
      - note: using a min heap instead would save operations, but double the space needed (cannot do in-place).

## Sorting

- [ ] Notes:

  - Implement sorts & know best case/worst case, average complexity of each:
    - no bubble sort - it's terrible - O(n^2), except when n <= 16
  - [ ] stability in sorting algorithms ("Is Quicksort stable?")
    - [Sorting Algorithm Stability](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability)
    - [Stability In Sorting Algorithms](http://stackoverflow.com/questions/1517793/stability-in-sorting-algorithms)
    - [Stability In Sorting Algorithms](http://www.geeksforgeeks.org/stability-in-sorting-algorithms/)
    - [Sorting Algorithms - Stability](http://homepages.math.uic.edu/~leon/cs-mcs401-s08/handouts/stability.pdf)
  - [ ] Which algorithms can be used on linked lists? Which on arrays? Which on both?
    - I wouldn't recommend sorting a linked list, but merge sort is doable.
    - [Merge Sort For Linked List](http://www.geeksforgeeks.org/merge-sort-for-linked-list/)

- For heapsort, see Heap data structure above. Heap sort is great, but not stable.

- [ ] [Sedgewick - Mergesort (5 videos)](https://www.coursera.org/learn/algorithms-part1/home/week/3)

  - [ ] [1. Mergesort](https://www.coursera.org/learn/algorithms-part1/lecture/ARWDq/mergesort)
  - [ ] [2. Bottom up Mergesort](https://www.coursera.org/learn/algorithms-part1/lecture/PWNEl/bottom-up-mergesort)
  - [ ] [3. Sorting Complexity](https://www.coursera.org/learn/algorithms-part1/lecture/xAltF/sorting-complexity)
  - [ ] [4. Comparators](https://www.coursera.org/learn/algorithms-part1/lecture/9FYhS/comparators)
  - [ ] [5. Stability](https://www.coursera.org/learn/algorithms-part1/lecture/pvvLZ/stability)

- [ ] [Sedgewick - Quicksort (4 videos)](https://www.coursera.org/learn/algorithms-part1/home/week/3)

  - [ ] [1. Quicksort](https://www.coursera.org/learn/algorithms-part1/lecture/vjvnC/quicksort)
  - [ ] [2. Selection](https://www.coursera.org/learn/algorithms-part1/lecture/UQxFT/selection)
  - [ ] [3. Duplicate Keys](https://www.coursera.org/learn/algorithms-part1/lecture/XvjPd/duplicate-keys)
  - [ ] [4. System Sorts](https://www.coursera.org/learn/algorithms-part1/lecture/QBNZ7/system-sorts)

- [ ] UC Berkeley:

  - [ ] [CS 61B Lecture 29: Sorting I (video)](https://archive.org/details/ucberkeley_webcast_EiUvYS2DT6I)
  - [ ] [CS 61B Lecture 30: Sorting II (video)](https://archive.org/details/ucberkeley_webcast_2hTY3t80Qsk)
  - [ ] [CS 61B Lecture 32: Sorting III (video)](https://archive.org/details/ucberkeley_webcast_Y6LOLpxg6Dc)
  - [ ] [CS 61B Lecture 33: Sorting V (video)](https://archive.org/details/ucberkeley_webcast_qNMQ4ly43p4)

- [ ] [Bubble Sort (video)](https://www.youtube.com/watch?v=P00xJgWzz2c&index=1&list=PL89B61F78B552C1AB)
- [ ] [Analyzing Bubble Sort (video)](https://www.youtube.com/watch?v=ni_zk257Nqo&index=7&list=PL89B61F78B552C1AB)
- [ ] [Insertion Sort, Merge Sort (video)](https://www.youtube.com/watch?v=Kg4bqzAqRBM&index=3&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
- [ ] [Insertion Sort (video)](https://www.youtube.com/watch?v=c4BRHC7kTaQ&index=2&list=PL89B61F78B552C1AB)
- [ ] [Merge Sort (video)](https://www.youtube.com/watch?v=GCae1WNvnZM&index=3&list=PL89B61F78B552C1AB)
- [ ] [Quicksort (video)](https://www.youtube.com/watch?v=y_G9BkAm6B8&index=4&list=PL89B61F78B552C1AB)
- [ ] [Selection Sort (video)](https://www.youtube.com/watch?v=6nDMgr0-Yyo&index=8&list=PL89B61F78B552C1AB)

- [ ] Merge sort code:
  - [ ] [Using output array (C)](http://www.cs.yale.edu/homes/aspnes/classes/223/examples/sorting/mergesort.c)
  - [ ] [Using output array (Python)](https://github.com/jwasham/practice-python/blob/master/merge_sort/merge_sort.py)
  - [ ] [In-place (C++)](https://github.com/jwasham/practice-cpp/blob/master/merge_sort/merge_sort.cc)
- [ ] Quick sort code:

  - [ ] [Implementation (C)](http://www.cs.yale.edu/homes/aspnes/classes/223/examples/randomization/quick.c)
  - [ ] [Implementation (C)](https://github.com/jwasham/practice-c/blob/master/quick_sort/quick_sort.c)
  - [ ] [Implementation (Python)](https://github.com/jwasham/practice-python/blob/master/quick_sort/quick_sort.py)

- [ ] Implement:

  - [ ] Mergesort: O(n log n) average and worst case
  - [ ] Quicksort O(n log n) average case
  - Selection sort and insertion sort are both O(n^2) average and worst case
  - For heapsort, see Heap data structure above.

- [ ] Not required, but I recommended them:
  - [ ] [Sedgewick - Radix Sorts (6 videos)](https://www.coursera.org/learn/algorithms-part2/home/week/3)
    - [ ] [1. Strings in Java](https://www.coursera.org/learn/algorithms-part2/lecture/vGHvb/strings-in-java)
    - [ ] [2. Key Indexed Counting](https://www.coursera.org/learn/algorithms-part2/lecture/2pi1Z/key-indexed-counting)
    - [ ] [3. Least Significant Digit First String Radix Sort](https://www.coursera.org/learn/algorithms-part2/lecture/c1U7L/lsd-radix-sort)
    - [ ] [4. Most Significant Digit First String Radix Sort](https://www.coursera.org/learn/algorithms-part2/lecture/gFxwG/msd-radix-sort)
    - [ ] [5. 3 Way Radix Quicksort](https://www.coursera.org/learn/algorithms-part2/lecture/crkd5/3-way-radix-quicksort)
    - [ ] [6. Suffix Arrays](https://www.coursera.org/learn/algorithms-part2/lecture/TH18W/suffix-arrays)
  - [ ] [Radix Sort](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#radixSort)
  - [ ] [Radix Sort (video)](https://www.youtube.com/watch?v=xhr26ia4k38)
  - [ ] [Radix Sort, Counting Sort (linear time given constraints) (video)](https://www.youtube.com/watch?v=Nz1KZXbghj8&index=7&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
  - [ ] [Randomization: Matrix Multiply, Quicksort, Freivalds' algorithm (video)](https://www.youtube.com/watch?v=cNB2lADK3_s&index=8&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
  - [ ] [Sorting in Linear Time (video)](https://www.youtube.com/watch?v=pOKy3RZbSws&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf&index=14)

As a summary, here is a visual representation of [15 sorting algorithms](https://www.youtube.com/watch?v=kPRA0W1kECg).
If you need more detail on this subject, see "Sorting" section in [Additional Detail on Some Subjects](#additional-detail-on-some-subjects)

## Graphs

Graphs can be used to represent many problems in computer science, so this section is long, like trees and sorting were.

- Notes:

  - There are 4 basic ways to represent a graph in memory:
    - objects and pointers
    - adjacency matrix
    - adjacency list
    - adjacency map
  - Familiarize yourself with each representation and its pros & cons
  - BFS and DFS - know their computational complexity, their tradeoffs, and how to implement them in real code
  - When asked a question, look for a graph-based solution first, then move on if none.

- [ ] MIT(videos):

  - [ ] [Breadth-First Search](https://www.youtube.com/watch?v=s-CYnVz-uh4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=13)
  - [ ] [Depth-First Search](https://www.youtube.com/watch?v=AfSk24UTFS8&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=14)

- [ ] Skiena Lectures - great intro:

  - [ ] [CSE373 2012 - Lecture 11 - Graph Data Structures (video)](https://www.youtube.com/watch?v=OiXxhDrFruw&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=11)
  - [ ] [CSE373 2012 - Lecture 12 - Breadth-First Search (video)](https://www.youtube.com/watch?v=g5vF8jscteo&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=12)
  - [ ] [CSE373 2012 - Lecture 13 - Graph Algorithms (video)](https://www.youtube.com/watch?v=S23W6eTcqdY&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=13)
  - [ ] [CSE373 2012 - Lecture 14 - Graph Algorithms (con't) (video)](https://www.youtube.com/watch?v=WitPBKGV0HY&index=14&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)
  - [ ] [CSE373 2012 - Lecture 15 - Graph Algorithms (con't 2) (video)](https://www.youtube.com/watch?v=ia1L30l7OIg&index=15&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)
  - [ ] [CSE373 2012 - Lecture 16 - Graph Algorithms (con't 3) (video)](https://www.youtube.com/watch?v=jgDOQq6iWy8&index=16&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)

- [ ] Graphs (review and more):

  - [ ] [6.006 Single-Source Shortest Paths Problem (video)](https://www.youtube.com/watch?v=Aa2sqUhIn-E&index=15&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
  - [ ] [6.006 Dijkstra (video)](https://www.youtube.com/watch?v=2E7MmKv0Y24&index=16&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
  - [ ] [6.006 Bellman-Ford (video)](https://www.youtube.com/watch?v=ozsuci5pIso&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=17)
  - [ ] [6.006 Speeding Up Dijkstra (video)](https://www.youtube.com/watch?v=CHvQ3q_gJ7E&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=18)
  - [ ] [Aduni: Graph Algorithms I - Topological Sorting, Minimum Spanning Trees, Prim's Algorithm - Lecture 6 (video)](https://www.youtube.com/watch?v=i_AQT_XfvD8&index=6&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
  - [ ] [Aduni: Graph Algorithms II - DFS, BFS, Kruskal's Algorithm, Union Find Data Structure - Lecture 7 (video)](https://www.youtube.com/watch?v=ufj5_bppBsA&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=7)
  - [ ] [Aduni: Graph Algorithms III: Shortest Path - Lecture 8 (video)](https://www.youtube.com/watch?v=DiedsPsMKXc&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=8)
  - [ ] [Aduni: Graph Alg. IV: Intro to geometric algorithms - Lecture 9 (video)](https://www.youtube.com/watch?v=XIAQRlNkJAw&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=9)
  - [ ] ~~[CS 61B 2014 (starting at 58:09) (video)](https://youtu.be/dgjX4HdMI-Q?list=PL-XXv-cvA_iAlnI-BQr9hjqADPBtujFJd&t=3489)~~
  - [ ] [CS 61B 2014: Weighted graphs (video)](https://archive.org/details/ucberkeley_webcast_zFbq8vOZ_0k)
  - [ ] [Greedy Algorithms: Minimum Spanning Tree (video)](https://www.youtube.com/watch?v=tKwnms5iRBU&index=16&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
  - [ ] [Strongly Connected Components Kosaraju's Algorithm Graph Algorithm (video)](https://www.youtube.com/watch?v=RpgcYiky7uw)

- Full Coursera Course:

  - [ ] [Algorithms on Graphs (video)](https://www.coursera.org/learn/algorithms-on-graphs/home/welcome)

- I'll implement:
  - [ ] DFS with adjacency list (recursive)
  - [ ] DFS with adjacency list (iterative with stack)
  - [ ] DFS with adjacency matrix (recursive)
  - [ ] DFS with adjacency matrix (iterative with stack)
  - [ ] BFS with adjacency list
  - [ ] BFS with adjacency matrix
  - [ ] single-source shortest path (Dijkstra)
  - [ ] minimum spanning tree
  - DFS-based algorithms (see Aduni videos above):
    - [ ] check for cycle (needed for topological sort, since we'll check for cycle before starting)
    - [ ] topological sort
    - [ ] count connected components in a graph
    - [ ] list strongly connected components
    - [ ] check for bipartite graph

## Even More Knowledge

- ### Recursion

  - [ ] Stanford lectures on recursion & backtracking:
    - [ ] [Lecture 8 | Programming Abstractions (video)](https://www.youtube.com/watch?v=gl3emqCuueQ&list=PLFE6E58F856038C69&index=8)
    - [ ] [Lecture 9 | Programming Abstractions (video)](https://www.youtube.com/watch?v=uFJhEPrbycQ&list=PLFE6E58F856038C69&index=9)
    - [ ] [Lecture 10 | Programming Abstractions (video)](https://www.youtube.com/watch?v=NdF1QDTRkck&index=10&list=PLFE6E58F856038C69)
    - [ ] [Lecture 11 | Programming Abstractions (video)](https://www.youtube.com/watch?v=p-gpaIGRCQI&list=PLFE6E58F856038C69&index=11)
  - when it is appropriate to use it
  - how is tail recursion better than not?
    - [ ] [What Is Tail Recursion Why Is It So Bad?](https://www.quora.com/What-is-tail-recursion-Why-is-it-so-bad)
    - [ ] [Tail Recursion (video)](https://www.youtube.com/watch?v=L1jjXGfxozc)

- ### Dynamic Programming

  - You probably won't see any dynamic programming problems in your interview, but it's worth being able to recognize a problem as being a candidate for dynamic programming.
  - This subject can be pretty difficult, as each DP soluble problem must be defined as a recursion relation, and coming up with it can be tricky.
  - I suggest looking at many examples of DP problems until you have a solid understanding of the pattern involved.
  - [ ] Videos:
    - the Skiena videos can be hard to follow since he sometimes uses the whiteboard, which is too small to see
    - [ ] [Skiena: CSE373 2012 - Lecture 19 - Introduction to Dynamic Programming (video)](https://youtu.be/Qc2ieXRgR0k?list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&t=1718)
    - [ ] [Skiena: CSE373 2012 - Lecture 20 - Edit Distance (video)](https://youtu.be/IsmMhMdyeGY?list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&t=2749)
    - [ ] [Skiena: CSE373 2012 - Lecture 21 - Dynamic Programming Examples (video)](https://youtu.be/o0V9eYF4UI8?list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&t=406)
    - [ ] [Skiena: CSE373 2012 - Lecture 22 - Applications of Dynamic Programming (video)](https://www.youtube.com/watch?v=dRbMC1Ltl3A&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=22)
    - [ ] [Simonson: Dynamic Programming 0 (starts at 59:18) (video)](https://youtu.be/J5aJEcOr6Eo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3558)
    - [ ] [Simonson: Dynamic Programming I - Lecture 11 (video)](https://www.youtube.com/watch?v=0EzHjQ_SOeU&index=11&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
    - [ ] [Simonson: Dynamic programming II - Lecture 12 (video)](https://www.youtube.com/watch?v=v1qiRwuJU7g&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=12)
    - [ ] List of individual DP problems (each is short):
          [Dynamic Programming (video)](https://www.youtube.com/playlist?list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr)
  - [ ] Yale Lecture notes:
    - [ ] [Dynamic Programming](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#dynamicProgramming)
  - [ ] Coursera:
    - [ ] [The RNA secondary structure problem (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/80RrW/the-rna-secondary-structure-problem)
    - [ ] [A dynamic programming algorithm (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/PSonq/a-dynamic-programming-algorithm)
    - [ ] [Illustrating the DP algorithm (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/oUEK2/illustrating-the-dp-algorithm)
    - [ ] [Running time of the DP algorithm (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/nfK2r/running-time-of-the-dp-algorithm)
    - [ ] [DP vs. recursive implementation (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/M999a/dp-vs-recursive-implementation)
    - [ ] [Global pairwise sequence alignment (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/UZ7o6/global-pairwise-sequence-alignment)
    - [ ] [Local pairwise sequence alignment (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/WnNau/local-pairwise-sequence-alignment)

* ### Learn C

  - C is everywhere. You'll see examples in books, lectures, videos, _everywhere_ while you're studying.
  - [ ] [C Programming Language, Vol 2](https://www.amazon.com/Programming-Language-Brian-W-Kernighan/dp/0131103628)
    - This is a short book, but it will give you a great handle on the C language and if you practice it a little
      you'll quickly get proficient. Understanding C helps you understand how programs and memory work.
    - [answers to questions](https://github.com/lekkas/c-algorithms)

- ### Object-Oriented Programming

  - [ ] [Optional: UML 2.0 Series (video)](https://www.youtube.com/watch?v=OkC7HKtiZC0&list=PLGLfVvz_LVvQ5G-LdJ8RLqe-ndo7QITYc)
  - [ ] SOLID OOP Principles: [SOLID Principles (video)](https://www.youtube.com/playlist?list=PL4CE9F710017EA77A)

- ### Design patterns
  - [ ] [Quick UML review (video)](https://www.youtube.com/watch?v=3cmzqZzwNDM&list=PLGLfVvz_LVvQ5G-LdJ8RLqe-ndo7QITYc&index=3)
  - [ ] Learn these patterns:
    - [ ] strategy
    - [ ] singleton
    - [ ] adapter
    - [ ] prototype
    - [ ] decorator
    - [ ] visitor
    - [ ] factory, abstract factory
    - [ ] facade
    - [ ] observer
    - [ ] proxy
    - [ ] delegate
    - [ ] command
    - [ ] state
    - [ ] memento
    - [ ] iterator
    - [ ] composite
    - [ ] flyweight
  - [ ] [Chapter 6 (Part 1) - Patterns (video)](https://youtu.be/LAP2A80Ajrg?list=PLJ9pm_Rc9HesnkwKlal_buSIHA-jTZMpO&t=3344)
  - [ ] [Chapter 6 (Part 2) - Abstraction-Occurrence, General Hierarchy, Player-Role, Singleton, Observer, Delegation (video)](https://www.youtube.com/watch?v=U8-PGsjvZc4&index=12&list=PLJ9pm_Rc9HesnkwKlal_buSIHA-jTZMpO)
  - [ ] [Chapter 6 (Part 3) - Adapter, Facade, Immutable, Read-Only Interface, Proxy (video)](https://www.youtube.com/watch?v=7sduBHuex4c&index=13&list=PLJ9pm_Rc9HesnkwKlal_buSIHA-jTZMpO)
  - [ ] [Series of videos (27 videos)](https://www.youtube.com/playlist?list=PLF206E906175C7E07)
  - [ ] [Head First Design Patterns](https://www.amazon.com/Head-First-Design-Patterns-Freeman/dp/0596007124)
    - I know the canonical book is "Design Patterns: Elements of Reusable Object-Oriented Software", but Head First is great for beginners to OO.
  - [ ] [Handy reference: 101 Design Patterns & Tips for Developers](https://sourcemaking.com/design-patterns-and-tips)
  - [ ] [Design patterns for humans](https://github.com/kamranahmedse/design-patterns-for-humans#structural-design-patterns)

* ### Combinatorics (n choose k) & Probability

  - [ ] [Math Skills: How to find Factorial, Permutation and Combination (Choose) (video)](https://www.youtube.com/watch?v=8RRo6Ti9d0U)
  - [ ] [Make School: Probability (video)](https://www.youtube.com/watch?v=sZkAAk9Wwa4)
  - [ ] [Make School: More Probability and Markov Chains (video)](https://www.youtube.com/watch?v=dNaJg-mLobQ)
  - [ ] Khan Academy:
    - Course layout:
      - [ ] [Basic Theoretical Probability](https://www.khanacademy.org/math/probability/probability-and-combinatorics-topic)
    - Just the videos - 41 (each are simple and each are short):
      - [ ] [Probability Explained (video)](https://www.youtube.com/watch?v=uzkc-qNVoOk&list=PLC58778F28211FA19)

* ### NP, NP-Complete and Approximation Algorithms

  - Know about the most famous classes of NP-complete problems, such as traveling salesman and the knapsack problem,
    and be able to recognize them when an interviewer asks you them in disguise.
  - Know what NP-complete means.
  - [ ] [Computational Complexity (video)](https://www.youtube.com/watch?v=moPtwq_cVH8&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=23)
  - [ ] Simonson:
    - [ ] [Greedy Algs. II & Intro to NP Completeness (video)](https://youtu.be/qcGnJ47Smlo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=2939)
    - [ ] [NP Completeness II & Reductions (video)](https://www.youtube.com/watch?v=e0tGC6ZQdQE&index=16&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
    - [ ] [NP Completeness III (Video)](https://www.youtube.com/watch?v=fCX1BGT3wjE&index=17&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
    - [ ] [NP Completeness IV (video)](https://www.youtube.com/watch?v=NKLDp3Rch3M&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=18)
  - [ ] Skiena:
    - [ ] [CSE373 2012 - Lecture 23 - Introduction to NP-Completeness (video)](https://youtu.be/KiK5TVgXbFg?list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&t=1508)
    - [ ] [CSE373 2012 - Lecture 24 - NP-Completeness Proofs (video)](https://www.youtube.com/watch?v=27Al52X3hd4&index=24&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)
    - [ ] [CSE373 2012 - Lecture 25 - NP-Completeness Challenge (video)](https://www.youtube.com/watch?v=xCPH4gwIIXM&index=25&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)
  - [ ] [Complexity: P, NP, NP-completeness, Reductions (video)](https://www.youtube.com/watch?v=eHZifpgyH_4&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=22)
  - [ ] [Complexity: Approximation Algorithms (video)](https://www.youtube.com/watch?v=MEz1J9wY2iM&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=24)
  - [ ] [Complexity: Fixed-Parameter Algorithms (video)](https://www.youtube.com/watch?v=4q-jmGrmxKs&index=25&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
  - Peter Norvig discusses near-optimal solutions to traveling salesman problem:
    - [Jupyter Notebook](http://nbviewer.jupyter.org/url/norvig.com/ipython/TSP.ipynb)
  - Pages 1048 - 1140 in CLRS if you have it.

* ### Caches

  - [ ] LRU cache:
    - [ ] [The Magic of LRU Cache (100 Days of Google Dev) (video)](https://www.youtube.com/watch?v=R5ON3iwx78M)
    - [ ] [Implementing LRU (video)](https://www.youtube.com/watch?v=bq6N7Ym81iI)
    - [ ] [LeetCode - 146 LRU Cache (C++) (video)](https://www.youtube.com/watch?v=8-FZRAjR7qU)
  - [ ] CPU cache:
    - [ ] [MIT 6.004 L15: The Memory Hierarchy (video)](https://www.youtube.com/watch?v=vjYF_fAZI5E&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-&index=24)
    - [ ] [MIT 6.004 L16: Cache Issues (video)](https://www.youtube.com/watch?v=ajgC3-pyGlk&index=25&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-)

* ### Processes and Threads

  - [ ] Computer Science 162 - Operating Systems (25 videos):
    - for processes and threads see videos 1-11
    - [Operating Systems and System Programming (video)](https://archive.org/details/ucberkeley-webcast-PL-XXv-cvA_iBDyz-ba4yDskqMDY6A1w_c)
  - [What Is The Difference Between A Process And A Thread?](https://www.quora.com/What-is-the-difference-between-a-process-and-a-thread)
  - Covers:
    - Processes, Threads, Concurrency issues
      - difference between processes and threads
      - processes
      - threads
      - locks
      - mutexes
      - semaphores
      - monitors
      - how they work
      - deadlock
      - livelock
    - CPU activity, interrupts, context switching
    - Modern concurrency constructs with multicore processors
    - [Paging, segmentation and virtual memory (video)](https://www.youtube.com/watch?v=LKe7xK0bF7o&list=PLCiOXwirraUCBE9i_ukL8_Kfg6XNv7Se8&index=2)
    - [Interrupts (video)](https://www.youtube.com/watch?v=uFKi2-J-6II&list=PLCiOXwirraUCBE9i_ukL8_Kfg6XNv7Se8&index=3)
    - Process resource needs (memory: code, static storage, stack, heap, and also file descriptors, i/o)
    - Thread resource needs (shares above (minus stack) with other threads in the same process but each has its own pc, stack counter, registers, and stack)
    - Forking is really copy on write (read-only) until the new process writes to memory, then it does a full copy.
    - Context switching
      - How context switching is initiated by the operating system and underlying hardware
  - [ ] [threads in C++ (series - 10 videos)](https://www.youtube.com/playlist?list=PL5jc9xFGsL8E12so1wlMS0r0hTQoJL74M)
  - [ ] concurrency in Python (videos):
    - [ ] [Short series on threads](https://www.youtube.com/playlist?list=PL1H1sBF1VAKVMONJWJkmUh6_p8g4F2oy1)
    - [ ] [Python Threads](https://www.youtube.com/watch?v=Bs7vPNbB9JM)
    - [ ] [Understanding the Python GIL (2010)](https://www.youtube.com/watch?v=Obt-vMVdM8s)
      - [reference](http://www.dabeaz.com/GIL)
    - [ ] [David Beazley - Python Concurrency From the Ground Up: LIVE! - PyCon 2015](https://www.youtube.com/watch?v=MCs5OvhV9S4)
    - [ ] [Keynote David Beazley - Topics of Interest (Python Asyncio)](https://www.youtube.com/watch?v=ZzfHjytDceU)
    - [ ] [Mutex in Python](https://www.youtube.com/watch?v=0zaPs8OtyKY)

* ### Testing

  - To cover:
    - how unit testing works
    - what are mock objects
    - what is integration testing
    - what is dependency injection
  - [ ] [Agile Software Testing with James Bach (video)](https://www.youtube.com/watch?v=SAhJf36_u5U)
  - [ ] [Open Lecture by James Bach on Software Testing (video)](https://www.youtube.com/watch?v=ILkT_HV9DVU)
  - [ ] [Steve Freeman - Test-Driven Development (that’s not what we meant) (video)](https://vimeo.com/83960706)
    - [slides](http://gotocon.com/dl/goto-berlin-2013/slides/SteveFreeman_TestDrivenDevelopmentThatsNotWhatWeMeant.pdf)
  - [ ] Dependency injection:
    - [ ] [video](https://www.youtube.com/watch?v=IKD2-MAkXyQ)
    - [ ] [Tao Of Testing](http://jasonpolites.github.io/tao-of-testing/ch3-1.1.html)
  - [ ] [How to write tests](http://jasonpolites.github.io/tao-of-testing/ch4-1.1.html)

* ### Scheduling

  - in an OS, how it works
  - can be gleaned from Operating System videos

* ### String searching & manipulations

  - [ ] [Sedgewick - Suffix Arrays (video)](https://www.coursera.org/learn/algorithms-part2/lecture/TH18W/suffix-arrays)
  - [ ] [Sedgewick - Substring Search (videos)](https://www.coursera.org/learn/algorithms-part2/home/week/4)
    - [ ] [1. Introduction to Substring Search](https://www.coursera.org/learn/algorithms-part2/lecture/n3ZpG/introduction-to-substring-search)
    - [ ] [2. Brute-Force Substring Search](https://www.coursera.org/learn/algorithms-part2/lecture/2Kn5i/brute-force-substring-search)
    - [ ] [3. Knuth-Morris Pratt](https://www.coursera.org/learn/algorithms-part2/lecture/TAtDr/knuth-morris-pratt)
    - [ ] [4. Boyer-Moore](https://www.coursera.org/learn/algorithms-part2/lecture/CYxOT/boyer-moore)
    - [ ] [5. Rabin-Karp](https://www.coursera.org/learn/algorithms-part2/lecture/3KiqT/rabin-karp)
  - [ ] [Search pattern in text (video)](https://www.coursera.org/learn/data-structures/lecture/tAfHI/search-pattern-in-text)

  If you need more detail on this subject, see "String Matching" section in [Additional Detail on Some Subjects](#additional-detail-on-some-subjects)

* ### Tries

  - Note there are different kinds of tries. Some have prefixes, some don't, and some use string instead of bits
    to track the path.
  - I read through code, but will not implement.
  - [ ] [Sedgewick - Tries (3 videos)](https://www.coursera.org/learn/algorithms-part2/home/week/4)
    - [ ] [1. R Way Tries](https://www.coursera.org/learn/algorithms-part2/lecture/CPVdr/r-way-tries)
    - [ ] [2. Ternary Search Tries](https://www.coursera.org/learn/algorithms-part2/lecture/yQM8K/ternary-search-tries)
    - [ ] [3. Character Based Operations](https://www.coursera.org/learn/algorithms-part2/lecture/jwNmV/character-based-operations)
  - [ ] [Notes on Data Structures and Programming Techniques](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#Tries)
  - [ ] Short course videos:
    - [ ] [Introduction To Tries (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/08Xyf/core-introduction-to-tries)
    - [ ] [Performance Of Tries (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/PvlZW/core-performance-of-tries)
    - [ ] [Implementing A Trie (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/DFvd3/core-implementing-a-trie)
  - [ ] [The Trie: A Neglected Data Structure](https://www.toptal.com/java/the-trie-a-neglected-data-structure)
  - [ ] [TopCoder - Using Tries](https://www.topcoder.com/community/competitive-programming/tutorials/using-tries/)
  - [ ] [Stanford Lecture (real world use case) (video)](https://www.youtube.com/watch?v=TJ8SkcUSdbU)
  - [ ] [MIT, Advanced Data Structures, Strings (can get pretty obscure about halfway through) (video)](https://www.youtube.com/watch?v=NinWEPPrkDQ&index=16&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf)

* ### Floating Point Numbers

  - [ ] simple 8-bit: [Representation of Floating Point Numbers - 1 (video - there is an error in calculations - see video description)](https://www.youtube.com/watch?v=ji3SfClm8TU)
  - [ ] 32 bit: [IEEE754 32-bit floating point binary (video)](https://www.youtube.com/watch?v=50ZYcZebIec)

---

## Final Review

    This section will have shorter videos that you can watch pretty quickly to review most of the important concepts.
    It's nice if you want a refresher often.

- [ ] Series of 2-3 minutes short subject videos (23 videos)
  - [Videos](https://www.youtube.com/watch?v=r4r1DZcx1cM&list=PLmVb1OknmNJuC5POdcDv5oCS7_OUkDgpj&index=22)
- [ ] Series of 2-5 minutes short subject videos - Michael Sambol (18 videos):
  - [Videos](https://www.youtube.com/channel/UCzDJwLWoYCUQowF_nG3m5OQ)
- [ ] [Sedgewick Videos - Algorithms I](https://www.coursera.org/learn/algorithms-part1)
- [ ] [Sedgewick Videos - Algorithms II](https://www.coursera.org/learn/algorithms-part2)

---

## Coding Question Practice

Now that you know all the computer science topics above, it's time to practice answering coding problems.

**Coding question practice is not about memorizing answers to programming problems.**

Why you need to practice doing programming problems:

- problem recognition, and where the right data structures and algorithms fit in
- gathering requirements for the problem
- talking your way through the problem like you will in the interview
- coding on a whiteboard or paper, not a computer
- coming up with time and space complexity for your solutions
- testing your solutions

There is a great intro for methodical, communicative problem solving in an interview. You'll get this from the programming
interview books, too, but I found this outstanding:
[Algorithm design canvas](http://www.hiredintech.com/algorithm-design/)

No whiteboard at home? That makes sense. I'm a weirdo and have a big whiteboard. Instead of a whiteboard, pick up a
large drawing pad from an art store. You can sit on the couch and practice. This is my "sofa whiteboard".
I added the pen in the photo for scale. If you use a pen, you'll wish you could erase. Gets messy quick. I use a pencil
and eraser.

![my sofa whiteboard](https://d3j2pkmjtin6ou.cloudfront.net/art_board_sm_2.jpg)

Supplemental:

- [Mathematics for Topcoders](https://www.topcoder.com/community/competitive-programming/tutorials/mathematics-for-topcoders/)
- [Dynamic Programming – From Novice to Advanced](https://www.topcoder.com/community/competitive-programming/tutorials/dynamic-programming-from-novice-to-advanced/)
- [MIT Interview Materials](https://web.archive.org/web/20160906124824/http://courses.csail.mit.edu/iap/interview/materials.php)
- [Exercises for getting better at a given language](http://exercism.io/languages)

**Read and Do Programming Problems (in this order):**

- [ ] [Cracking the Coding Interview, 6th Edition](http://www.amazon.com/Cracking-Coding-Interview-6th-Programming/dp/0984782850/)
  - answers in Java

See [Book List above](#book-list)

## Coding exercises/challenges

Once you've learned your brains out, put those brains to work.
Take coding challenges every day, as many as you can.

- [How to Find a Solution](https://www.topcoder.com/community/competitive-programming/tutorials/how-to-find-a-solution/)
- [How to Dissect a Topcoder Problem Statement](https://www.topcoder.com/community/competitive-programming/tutorials/how-to-dissect-a-topcoder-problem-statement/)

Coding Interview Question Videos:

- [IDeserve (88 videos)](https://www.youtube.com/watch?v=NBcqBddFbZw&list=PLamzFoFxwoNjPfxzaWqs7cZGsPYy0x_gI)
- [Tushar Roy (5 playlists)](https://www.youtube.com/user/tusharroy2525/playlists?shelf_id=2&view=50&sort=dd)
  - Super for walkthroughs of problem solutions.
- [Nick White - LeetCode Solutions (187 Videos)](https://www.youtube.com/playlist?list=PLU_sdQYzUj2keVENTP0a5rdykRSgg9Wp-)
  - Good explanations of solution and the code.
  - You can watch several in a short time.
- [FisherCoder - LeetCode Solutions](https://youtube.com/FisherCoder)

Challenge sites:

- [LeetCode](https://leetcode.com/)
  - My favorite coding problem site. It's worth the subscription money for the 1-2 months you'll likely be preparing.
  - [LeetCode solutions from FisherCoder](https://github.com/fishercoder1534/Leetcode)
  - See Nick White Videos above for short code-throughs
- [HackerRank](https://www.hackerrank.com/)
- [TopCoder](https://www.topcoder.com/)
- [InterviewCake](https://www.interviewcake.com/)
- [Geeks for Geeks](http://www.geeksforgeeks.org/)
- [InterviewBit](https://www.interviewbit.com/invite/icjf)
- [Project Euler (math-focused)](https://projecteuler.net/index.php?section=problems)

Language-learning sites, with challenges:

- [Codewars](http://www.codewars.com)
- [Codility](https://codility.com/programmers/)
- [HackerEarth](https://www.hackerearth.com/)
- [Sphere Online Judge (spoj)](http://www.spoj.com/)
- [Codechef](https://www.codechef.com/)

Challenge repos:

- [Interactive Coding Interview Challenges in Python](https://github.com/donnemartin/interactive-coding-challenges)

Mock Interviews:

- [Gainlo.co: Mock interviewers from big companies](http://www.gainlo.co/) - I used this and it helped me relax for the phone screen and on-site interview.
- [Pramp: Mock interviews from/with peers](https://www.pramp.com/) - peer-to-peer model of practice interviews
- [Refdash: Mock interviews and expedited interviews](https://refdash.com/) - also help candidates fast track by skipping multiple interviews with tech companies.

## Once you're closer to the interview

- Cracking The Coding Interview Set 2 (videos):
  - [Cracking The Code Interview](https://www.youtube.com/watch?v=4NIb9l3imAo)
  - [Cracking the Coding Interview - Fullstack Speaker Series](https://www.youtube.com/watch?v=Eg5-tdAwclo)

## LICENSE

[CC-BY-SA-4.0](./LICENSE.txt)
