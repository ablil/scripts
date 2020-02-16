#include <stdio.h>
#include <stdlib.h>

typedef struct linkedList {
    int data;
    struct linkedList *next;
} linkedList;

linkedList *initList(int data) {
    linkedList *head = malloc(sizeof(linkedList));
    head->data = data;
    head->next = NULL;

    return head;
}

void displayList(linkedList *head) {
    if ( head == NULL ) {
        printf("LINKED LIST IS EMPTY !!\n");
    } else {
        while ( head != NULL ) {
            printf("data : %d\n", head->data);
            head = head->next;
        }
    }
}

void insert(linkedList *head, int data) {
    while ( head->next != NULL ) {
        // while we didnt reach the last node
        head = head->next;
    }

    // insert data
    linkedList *newNode = initList(data);
    head->next = newNode;
}

void removeFromList(linkedList **head, int data ) {
    if ( *head == NULL ) {
        return ;
    } else {
        // if data exists at the begining of list
        while ( *head != NULL && (*head)->data == data ) {
            *head = (*head)->next;
        }

        linkedList *cursor = *head;
        // if first element equal to data, shift the head of list
        if ( cursor == NULL ) {
            return;
        }

        while ( cursor->next != NULL ) {
            if ( cursor->next->data == data ) {
                cursor->next = cursor->next->next;

                // when multiple nodes have the same value data, continue
                continue;
            }
            cursor = cursor->next;

            // this condition apply when data is at the last node of list
            // if cursor is NULL, break from loop
            // otherwise you will have error from ( cursor->next != NULL )
            if (cursor == NULL ) break;
        }
    }
}

int lenght(linkedList *head) {
    if (head == NULL ) {
        return 0;
    } else {
        return 1 + lenght(head->next);
    }
}

int main() {
    printf("hello world\n");
    return 0;
}
