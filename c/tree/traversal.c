#include <stdio.h>
#include <stdlib.h>

typedef struct tree {
    int data;
    struct tree *rightChild;
    struct tree *leftChild;
} tree;

void inOrderTraversal(tree *root) {
    if (root == NULL ) {
        return ;
    }

    inOrderTraversal(root->leftChild);
    printf("data : %d\n", root->data);
    inOrderTraversal(root->rightChild);
}

void preOrderTraversal(tree *root) {
    if ( root == NULL ){
        return ;
    }

    printf("data : %d\n", root->data);
    preOrderTraversal(root->leftChild);
    preOrderTraversal(root->rightChild);
 }

void postOrderTraversal(tree *root) {
    if ( root == NULL ){
        return ;
    }

    postOrderTraversal(root->leftChild);
    postOrderTraversal(root->rightChild);
    printf("data : %d\n", root->data);
 }
