#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function inserts node in sorted linked list
 * @head: head of the singled list
 * @number: number to inserted
 * 
 * Return: address of the new node, null if failed
*/

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *prev_node, *curr_node;

    /* Allocate memory for new node */
    new_node = (listint_t *)malloc(sizeof(listint_t));
    if (new_node == NULL)
    {
        printf("Error: Unable to allocate memory for new node.\n");
        return NULL;
    }

    /* Initialize new node */
    new_node->n = number;
    new_node->next = NULL;

    /* Case 1: Empty list */
    if (*head == NULL)
    {
        *head = new_node;
        return new_node;
    }

    /* Case 2: Insert at head */
    if (number < (*head)->n)
    {
        new_node->next = *head;
        *head = new_node;
        return new_node;
    }

    /* Case 3: Insert in middle or at end */
    prev_node = *head;
    curr_node = (*head)->next;

    while (curr_node != NULL && number > curr_node->n)
    {
        prev_node = curr_node;
        curr_node = curr_node->next;
    }

    /* Insert new node */
    prev_node->next = new_node;
    new_node->next = curr_node;
    return new_node;
}
