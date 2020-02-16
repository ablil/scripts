#include <stdio.h>
#include <stdlib.h>

typedef struct queue {
    int data;
    struct queue *next;
    struct queue *previous;
} queue;

queue *initQueue(int data) {
    queue *head = malloc(sizeof(queue));

    head->data = data;
    head->next = head;
    head->previous = head;

    return head;
}

void displayQueue(queue *head) {
    if ( head == NULL ) {
        puts("QUEUE IS EMPTY");
        return ;
    } else {
        queue *first = head;

        do {
            printf("data : %d\n", head->data);
            head = head->next;
        } while ( head != first );
    }
}

void push(queue **head, int data) {
    if ( *head == NULL ) {
        *head = initQueue(data);
    } else {
        // create new node and set variable
        queue *first = *head;
        queue *last = (*head)->previous;

        queue *newNode = initQueue(data);
        newNode->next = first;
        newNode->previous = last;

        // change existing queue variable
        first->previous = newNode;
        last->next = newNode;

        // change the head of queue to be newNode
        *head = newNode;
    }
}

int pop(queue **head) {
    if ( *head == NULL ) {
        puts("QUEUE IS EMPTY");
        return;
    } else if ( (*head)->next == (*head)->previous ) {
        int res = (*head)->data;
        *head = NULL;
        return res;
    }else {
        int res = (*head)->previous->data;

        // before last element point to head of queue
        queue *beforeLast = (*head)->previous->previous;
        beforeLast->next = *head;

        (*head)->previous = beforeLast;
        return res;
    }
}

int main() {
    puts("hello world");
    return 0;
}
