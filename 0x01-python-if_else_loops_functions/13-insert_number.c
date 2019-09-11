#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert item into sorted linked list
 * @head: pointer to head pointer
 * @number: number to insert
 * Return: pointer to inserted item, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev, *curr;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (!*head)
		return (*head = new);
	/* If new item belongs at beginning of list */
	if (number <= (*head)->n)
	{
		new->next = *head;
		return (*head = new);
	}
	/* Search for position */
	prev = *head;
	curr = prev->next;
	while (curr)
	{
		if (curr->n >= number)
			break;
		prev = curr;
	   curr = curr->next;
	}
	prev->next = new;
	new->next = curr; /* `curr` is null if new item belongs at end */
	return (new);
}
