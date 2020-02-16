#include <stdio.h>
#include <stdlib.h>


typedef struct tree {
    int data;
    struct tree *rightChild;
    struct tree *leftChild;
} tree;

int max(int a, int b) {
    if ( a > b) {
        return a;
    } else {
        return b;
    }
}

tree* initTree(int data) {
    // init a tree with passed argument 'data'

    tree *root = malloc(sizeof(tree));
    root->rightChild = NULL;
    root->leftChild = NULL;
    root->data = data;

    return root;
}

void insert(tree *root, int data ) {
    // insert data into root

    if ( root == NULL ) {
        root = initTree(data);
    } else {
        if (data > root->data ) {
            // if right child is empy, insert element
            // if not, call insert recursively
            if (root->rightChild == NULL ) {
                root->rightChild = initTree(data);
            } else {
                insert(root->rightChild, data);
            }
        } else {
            if ( root->leftChild == NULL ){
                root->leftChild = initTree(data);
            } else {
                insert(root->leftChild, data);
            }
        }
    }
}

int exists(tree *root, int data) {
    // check if data exists in tree
    if ( root == NULL ) {
        return 0;
    } else {
        if ( root->data == data ){
            return 1;
        } else if ( data > root->data ) {
            return exists(root->rightChild, data);
        } else {
            return exists(root->leftChild, data);
        }
    }
}

int height(tree *root) {
    // get height of tree
    if ( root == NULL ){
        return -1;
    } else {
        return 1 + max(height(root->leftChild), height(root->rightChild));
    }
}

int getMax(tree *root ) {
    // get maximum value in tree
    if ( root == NULL ){
        return 0;

    } else {
        int maxValue = root->data ;
        int maxRight = 0, maxLeft = 0; // max value in right/left child

        maxRight = getMax(root->rightChild);
        if ( maxRight > maxValue ) {
            maxValue = maxRight;
        }

        maxLeft = getMax(root->leftChild);
        if ( maxLeft > maxValue ) {
            maxValue = maxLeft;
        }

        return maxValue;
    }
}

int getMin(tree *root ) {
    // get the minimum value in given tree
    if ( root == NULL ){
        return 0;

    } else {
        int minValue = root->data ;
        int minRight = 0, minLeft = 0; // max value in right/left child

        minRight = getMin(root->rightChild);
        if ( minRight < minValue ) {
            minValue = minRight;
        }

        minLeft = getMin(root->leftChild);
        if ( minLeft < minValue ) {
            minValue = minLeft;
        }

        return minValue;
    }
}
