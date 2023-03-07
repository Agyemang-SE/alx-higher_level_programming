#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle
 * @list: pointer to the linked list list
 *
 * Return: 0 for no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
listint_t *tortoise, *hare;

if (list == NULL || list->next == NULL)
{
return (0);
}

hare = list->next;
tortoise = list;
while (tortoise && hare && hare->next)
{
tortoise = tortoise->next;
hare = hare->next->next;
if (tortoise == hare)
{
return (1);
}
}
return (0);
}
