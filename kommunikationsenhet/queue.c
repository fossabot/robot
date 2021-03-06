
/*	queue.c

	Implementation of a FIFO queue abstract data type.

	by: Steven Skiena
	begun: March 27, 2002
*/


/*
Copyright 2003 by Steven S. Skiena; all rights reserved.

Permission is granted for use in non-commerical applications
provided this copyright notice remains intact and unchanged.

This program appears in my book:

"Programming Challenges: The Programming Contest Training Manual"
by Steven Skiena and Miguel Revilla, Springer-Verlag, New York 2003.

See our website www.programming-challenges.com for additional information.

This book can be ordered from Amazon.com at

http://www.amazon.com/exec/obidos/ASIN/0387001638/thealgorithmrepo/
*/


#include "queue.h"

void init_queue(queue *q)
{
	q->first = 0;
	q->last = QUEUESIZE-1;
	q->count = 0;
}

void enqueue(queue *q, Bus_data x)
{
	q->last = (q->last+1) % QUEUESIZE;
	q->q[ q->last ] = x;
	q->count = q->count + 1;
}

Bus_data dequeue(queue *q)
{
	Bus_data x;
	x = q->q[ q->first ];
	q->first = (q->first+1) % QUEUESIZE;
	q->count = q->count - 1;
	return x;
}

bool empty(queue *q)
{
	if (q->count <= 0) return true;
	else return false;
}
