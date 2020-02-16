#include <stdio.h>
#include <stdlib.h>

typedef struct stack {
    int data;
    struct stack *next;
} stack;

void displayStack(stack *head) {
    if ( head == NULL ) {
        puts("STACK IS EMPTY !!!");
    } else {
        while ( head != NULL ) {
            printf("data : %d\n", head->data);
            head = head->next;
        }
    }
}

stack *initStack(int data) {
    stack *head = malloc(sizeof(stack));
    head->data = data;
    head->next = NULL;

    return head;
}

void push(stack **head, int data) {
    if ( *head == NULL ) {
        *head = initStack(data);
    } else {
        stack *newHead = initStack(data);
        newHead->next = *head;
        *head = newHead;
    }
}

int pop(stack **head) {
    if ( *head == NULL ) {
        puts("STACK IS EMPTY !!");
        return;
    } else {
        int res = (*head)->data;

        *head = (*head)->next;
        return res;
    }
}

int main () {
    printf("hello world\n");
    return 0;
}
